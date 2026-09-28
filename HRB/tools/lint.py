"""Deterministic spec checks for the review loop.

Usage:
  python tools/lint.py snapshot baseline      # once, before round 1
  python tools/lint.py snapshot round_start   # at the start of every round
  python tools/lint.py check                  # after every fix batch
  python tools/lint.py check --all            # also list pre-existing warnings

`check` exits 1 when a FAIL is found. Existing warnings are tolerated;
only warnings that are NEW versus the baseline snapshot count against a round.
Thresholds live in state/lint_config.json (created with defaults if missing).
"""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "HRB_IVA_Agents_Spec.md"
STATE = ROOT / "state"
CONFIG = STATE / "lint_config.json"
DEFAULTS = {
    "bullet_max_words": 35, "bullet_max_sentences": 2,
    "para_max_words": 60, "para_max_sentences": 3,
    "json_item_max_words": 60,
    "spoken_turn_max_sentences": 3,
    "dup_min_words": 10, "dup_threshold": 0.8,
    "round_growth_max_pct": 1.0, "total_growth_max_pct": 5.0,
    "style_terms": ["should", "the agent will", "it is recommended", "a few", "as needed", "facilitate", "leverage", "utilize", "—", "“", "”"],
    "web_terms": ["online", "website", "web site", "url", "portal", "app", "myblock", ".com"],
}

SENT_SPLIT = re.compile(r'(?<=[.!?])["\']?\s+(?=["\'(]?[A-Z0-9])')
WORD = re.compile(r"[A-Za-z0-9_']+")


def cfg():
    STATE.mkdir(exist_ok=True)
    if not CONFIG.exists():
        CONFIG.write_text(json.dumps(DEFAULTS, indent=2), encoding="utf-8")
    return {**DEFAULTS, **json.loads(CONFIG.read_text(encoding="utf-8"))}


def words(s):
    return WORD.findall(s)


def sentences(s):
    return [x for x in SENT_SPLIT.split(s.strip()) if x.strip()]


def strip_md(s):
    return re.sub(r"[*`]", "", s).strip()


def parse(text):
    """Yield units: dict(kind, section, line, text). kinds: bullet, para, cell, dialogue, json."""
    units, blocks, headings = [], [], []
    section, in_code, is_json, code_start, code = "preamble", False, False, 0, []
    para, para_line = [], 0

    def flush():
        nonlocal para
        if para:
            units.append(dict(kind="para", section=section, line=para_line, text=" ".join(para)))
        para = []

    for n, raw in enumerate(text.split("\n"), 1):
        line = raw.rstrip()
        if line.startswith("```"):
            flush()
            if in_code:
                if is_json:
                    blocks.append((section, code_start, "\n".join(code)))
                in_code, code = False, []
            else:
                in_code, is_json, code_start, code = True, line.strip() == "```json", n, []
            continue
        if in_code:
            code.append(line)
            continue
        m = re.match(r"^(#{1,4})\s+(.*)", line)
        if m:
            flush()
            headings.append((len(m.group(1)), strip_md(m.group(2)), n))
            if len(m.group(1)) <= 2:
                section = strip_md(m.group(2))
            continue
        s = line.strip()
        if not s:
            flush()
            continue
        if s.startswith("|"):
            flush()
            cells = [strip_md(c) for c in s.strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue
            for c in cells:
                if c:
                    units.append(dict(kind="cell", section=section, line=n, text=c))
            continue
        b = re.match(r"^(?:[-*]|\d+\.)\s+(.*)", s)
        if b:
            flush()
            body = b.group(1)
            d = re.match(r"^\*\*(Agent|Caller):\*\*\s*(.*)", body)
            if d:
                kind = "dialogue" if d.group(1) == "Agent" else "caller"
                units.append(dict(kind=kind, section=section, line=n, text=d.group(2).strip('"')))
            else:
                units.append(dict(kind="bullet", section=section, line=n, text=strip_md(body)))
            continue
        if not para:
            para_line = n
        para.append(strip_md(s))
    flush()
    return units, blocks, headings


def walk_json(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_json(v, f"{path}.{k}" if path else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_json(v, f"{path}[{i}]")
    elif isinstance(obj, str):
        yield path, obj


def json_keys(obj, acc):
    if isinstance(obj, dict):
        for k, v in obj.items():
            acc.add(k)
            json_keys(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            json_keys(v, acc)
    return acc


def key_of(check, text):
    return check + ":" + hashlib.sha1(re.sub(r"\s+", " ", text.lower())[:120].encode()).hexdigest()[:12]


def run():
    c = cfg()
    text = SPEC.read_text(encoding="utf-8")
    units, blocks, headings = parse(text)
    findings = []  # (level, check, line, msg, key)

    def add(level, check, line, msg, basis):
        findings.append((level, check, line, msg, key_of(check, basis)))

    # 1. JSON blocks parse
    parsed, keys = [], set()
    for section, start, body in blocks:
        try:
            obj = json.loads(body)
            parsed.append((section, start, obj))
            json_keys(obj, keys)
        except json.JSONDecodeError as e:
            add("FAIL", "json", start + e.lineno, f"JSON block in '{section}' does not parse: {e.msg}", f"{section}{start}")

    # JSON string items become units too
    lines = text.split("\n")
    for section, start, obj in parsed:
        for path, s in walk_json(obj):
            probe = json.dumps(s)[1:41]
            ln = next((i + 1 for i in range(start, len(lines)) if probe in lines[i]), start)
            units.append(dict(kind="json", section=section, line=ln, text=s, path=path))

    # 2. Length
    for u in units:
        w, sn = len(words(u["text"])), len(sentences(u["text"]))
        k, loc = u["kind"], u.get("path", "")
        if (k == "bullet" and (w > c["bullet_max_words"] or sn > c["bullet_max_sentences"])) or (k == "cell" and w > c["bullet_max_words"]):
            add("WARN", "length", u["line"], f"{k} {w}w/{sn}s: {u['text'][:70]}...", u["text"])
        elif k == "para" and (w > c["para_max_words"] or sn > c["para_max_sentences"]):
            add("WARN", "length", u["line"], f"paragraph {w}w/{sn}s: {u['text'][:70]}...", u["text"])
        elif k == "json" and w > c["json_item_max_words"]:
            add("WARN", "length", u["line"], f"json {loc} {w}w: {u['text'][:60]}...", u["text"])
        elif k == "dialogue" and sn > c["spoken_turn_max_sentences"]:
            add("WARN", "turn_length", u["line"], f"Agent turn has {sn} sentences: {u['text'][:60]}...", u["text"])

    # 3. Near-duplicate sentences across sections
    sents = []
    for u in units:
        if u["kind"] in ("caller",):
            continue
        for s in sentences(u["text"]):
            ws = [x.lower() for x in words(s)]
            if len(ws) >= c["dup_min_words"]:
                sh = {" ".join(ws[i:i + 3]) for i in range(len(ws) - 2)}
                sents.append((u["section"], u["line"], "json" if u["kind"] == "json" else "prose", s, sh))
    index = {}
    for i, (_, _, _, _, sh) in enumerate(sents):
        for g in sh:
            index.setdefault(g, []).append(i)
    seen = set()
    for i, (sec, ln, src, s, sh) in enumerate(sents):
        cands = {}
        for g in sh:
            for j in index[g]:
                if j > i:
                    cands[j] = cands.get(j, 0) + 1
        for j, shared in cands.items():
            sec2, ln2, src2, s2, sh2 = sents[j]
            if sec2 == sec and src2 == src:
                continue
            jac = shared / len(sh | sh2)
            if jac >= c["dup_threshold"]:
                kind = "dup_mirror" if src != src2 else f"dup_{src}"
                pair = tuple(sorted((ln, ln2)))
                if (kind, pair) in seen:
                    continue
                seen.add((kind, pair))
                add("WARN", kind, ln, f"~{jac:.0%} same as L{ln2} ({sec2}): {s[:60]}...", s + s2)

    # 4. References
    tool_heads = {h for lvl, h, _ in headings if lvl == 3 and re.fullmatch(r"[a-z_]+", h)}
    head_titles = [h for _, h, _ in headings]
    for m in re.finditer(r"§\s?(\d+(?:\.\d+)*)", text):
        ln = text.count("\n", 0, m.start()) + 1
        if not any(h.startswith(m.group(1) + " ") for h in head_titles):
            add("FAIL", "ref", ln, f"§{m.group(1)} matches no heading", m.group(0) + str(ln))
    for m in re.finditer(r"\b([a-z]+(?:_[a-z]+)*(?:\.[a-z_]+)+)\b", text):
        ln = text.count("\n", 0, m.start()) + 1
        parts = m.group(1).split(".")
        if any(p not in keys for p in parts) and parts[0] in keys:
            add("FAIL", "ref", ln, f"key path '{m.group(1)}' does not resolve", m.group(1))
    for section, start, obj in parsed:
        for name in (obj.get("agent_specific_tools") or {}) if isinstance(obj, dict) else {}:
            if name not in tool_heads:
                add("FAIL", "ref", start, f"agent tool '{name}' has no Part 5 entry", name)
    used = text.split("# PART 5")[0]
    for t in tool_heads:
        if t not in used:
            add("WARN", "ref", 0, f"Part 5 tool '{t}' is never referenced by an agent", t)

    # 5. Prohibited speech in scripted lines
    prohibited = []
    for _, _, obj in parsed:
        if isinstance(obj, dict):
            prohibited += obj.get("global_voice_lexicon", {}).get("prohibited_phrases", [])
    spoken = [u for u in units if u["kind"] == "dialogue"]
    spoken += [u for u in units if u["kind"] == "cell" and "Approved Recovery" in u["section"]]
    spoken += [u for u in units if u["kind"] == "json" and re.search(r"(empathy|reprompt|method_descriptions|preamble)", u.get("path", ""))]
    for u in spoken:
        low = u["text"].lower()
        for p in prohibited:
            if p.lower() in low:
                add("WARN", "prohibited", u["line"], f"scripted line uses prohibited phrase '{p}'", u["text"] + p)
        for t in c["web_terms"]:
            if re.search(rf"(?<![a-z]){re.escape(t)}(?![a-z])", low):
                add("WARN", "web_deflection", u["line"], f"scripted line mentions '{t}': {u['text'][:60]}...", u["text"] + t)

    # 6. Style terms in rule text (spoken and frozen lines excluded)
    frozen = re.compile(r"(global_voice_lexicon|method_descriptions)")
    for u in units:
        if u["kind"] in ("dialogue", "caller") or frozen.search(u.get("path", "")) or "Approved Recovery" in u["section"]:
            continue
        low = u["text"].lower()
        for t in c["style_terms"]:
            if re.search(rf"(?<![a-z]){re.escape(t)}(?![a-z])", low):
                add("WARN", "style", u["line"], f"style term '{t}': {u['text'][:60]}...", u["text"] + t)

    size = dict(bytes=len(text.encode()), lines=text.count("\n") + 1, words=len(words(text)))
    return findings, size


def snapshot(name):
    findings, size = run()
    out = dict(size=size, keys=sorted({f[4] for f in findings}))
    (STATE / f"{name}.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"snapshot {name}: {size}, {len(findings)} findings")


def check():
    c = cfg()
    findings, size = run()
    base = json.loads((STATE / "baseline.json").read_text()) if (STATE / "baseline.json").exists() else None
    rnd = json.loads((STATE / "round_start.json").read_text()) if (STATE / "round_start.json").exists() else None
    known = set(base["keys"]) if base and "--all" not in sys.argv else set()
    fails, new, old = [], [], 0
    for f in findings:
        if f[0] == "FAIL":
            fails.append(f)
        elif f[4] in known:
            old += 1
        else:
            new.append(f)
    for label, ref, limit in (("total", base, c["total_growth_max_pct"]), ("round", rnd, c["round_growth_max_pct"])):
        if ref:
            pct = 100 * (size["bytes"] - ref["size"]["bytes"]) / ref["size"]["bytes"]
            line = f"{label} growth {pct:+.2f}% (limit {limit}%)"
            if pct > limit:
                fails.append(("FAIL", "size", 0, line, ""))
            else:
                print("OK   size", line)
    by = {}
    for f in new:
        by.setdefault(f[1], []).append(f)
    print(f"size {size}; pre-existing warnings tolerated: {old}")
    for f in fails:
        print(f"FAIL {f[1]:<14} L{f[2]:<5} {f[3]}")
    for check_name, fs in sorted(by.items()):
        print(f"-- NEW {check_name}: {len(fs)}")
        for f in fs:
            print(f"WARN {f[1]:<14} L{f[2]:<5} {f[3]}")
    print("RESULT", "FAIL" if fails else ("WARN" if new else "PASS"))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "snapshot":
        snapshot(sys.argv[2])
    else:
        check()
