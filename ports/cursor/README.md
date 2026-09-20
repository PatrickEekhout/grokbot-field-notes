# Cursor rules

The sixty-nine roster roles as Cursor rules, one `.mdc` per role, generated
from `roster/`. Each rule carries the paste-ready description, what the role
owns, what it doesn't, and what needs approval. Placeholders like `{NAME}`
and `{PRODUCT}` are yours to fill.

## Install

Copy the rules you want into your project:

```bash
mkdir -p .cursor/rules
cp ports/cursor/rules/chief-of-staff.mdc ports/cursor/rules/pr-reviewer.mdc .cursor/rules/
```

They ship with `alwaysApply: false`, so they load when you `@` them in a
chat or attach them to an agent, not on every request. Set `alwaysApply:
true` on the one rule you want in every conversation, usually
`chief-of-staff` or `pr-reviewer`.

`AGENTS.md` in the repo root is still the base layer; Cursor reads it on its
own. These rules sit on top of it.

## Regenerate

The roster is the source. Edit a file in `roster/`, then:

```bash
python3 ports/cursor/build.py
```
