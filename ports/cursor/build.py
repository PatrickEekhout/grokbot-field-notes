#!/usr/bin/env python3
"""Generate Cursor rules (.mdc) from roster/*.md. Run from the repo root."""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "ports" / "cursor" / "rules"
OUT.mkdir(parents=True, exist_ok=True)

def section(text, name):
    m = re.search(rf"^## {re.escape(name)}\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1).strip() if m else ""

for src in sorted((ROOT / "roster").glob("*.md")):
    if src.name == "README.md":
        continue
    text = src.read_text()
    title = re.match(r"# (.+)", text).group(1).strip()
    one_line = text.split("\n\n")[2].strip().replace("\n", " ")
    desc = re.search(r"^## Role description.*?```text\n(.*?)```", text, re.S | re.M)
    body = desc.group(1).strip() if desc else ""
    owns = section(text, "Owns")
    not_owns = section(text, "Does not own")
    approval = section(text, "Needs approval for")
    out = OUT / f"{src.stem}.mdc"
    out.write_text(f"""---
description: {title}. {one_line}
alwaysApply: false
---

{body}

## Owns

{owns}

## Does not own

{not_owns}

## Needs approval for

{approval}

<!-- Generated from roster/{src.name}. Edit the roster file, then run ports/cursor/build.py. -->
""")
print(f"wrote {len(list(OUT.glob('*.mdc')))} rules to {OUT.relative_to(ROOT)}")
