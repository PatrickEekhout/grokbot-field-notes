<!-- Copy this file to .github/PULL_REQUEST_TEMPLATE.md in your own repo.
     It is the verification loop from agents/VERIFICATION.md, as a form.
     Agents fill it in; humans check the boxes, not the diff. -->

## What changed

One paragraph. What the user can now do that they couldn't before, or what stopped happening.

## Reproduced first

- [ ] I ran the app and saw the bug / the current behaviour before changing anything
- Steps I used: <!-- exact steps, or the CLI command -->

## Proof

- [ ] UI change: screenshot or recording attached, showing the same steps passing
- [ ] Backend change: numbers attached (latency, count, size, before → after)
- [ ] Bug fix: the reproduction above, then the same steps passing

<!-- paste or attach here -->

## Scope

- [ ] Every changed line serves the one thing in the title
- [ ] No strings a user sees contain codenames, TODOs or my reasoning
- [ ] No comments explaining a workaround instead of fixing the cause

## Needs a human

- [ ] Migration
- [ ] Deploy or infra change
- [ ] Touches money, permissions or credentials
- [ ] None of the above — safe to auto-merge on green
