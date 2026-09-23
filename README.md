Source: https://substack.com/@whrrari/note/c-344006724?r=8oezxq

[![Grok Bot Guide by SpaceX Engineers](guide/cover.png)](guide/grok-bot-guide-by-spacex-engineers.pdf)

# Grok Bot Field Notes

[![Stars](https://img.shields.io/github/stars/unicodef1wn/grokbot-field-notes?style=flat)](https://github.com/unicodef1wn/grokbot-field-notes/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Download the PDF](https://img.shields.io/badge/PDF-download-black.svg)](https://github.com/unicodef1wn/grokbot-field-notes/releases/latest/download/grok-bot-guide-by-spacex-engineers.pdf)

Copy the rules into your repo and go:

```bash
curl -o AGENTS.md https://raw.githubusercontent.com/unicodef1wn/grokbot-field-notes/main/AGENTS.md
```

Three engineers from the xAI Grok Bot team built and launched a product from an empty repo in 72 hours, live on stream, using their own agent platform: [Roshan Sadanani](https://www.linkedin.com/in/roshansadanani) (product), [Lauren Tan](https://www.linkedin.com/in/laurenelizabethtan) (engineering, author of PStack), and [Matt Palmer](https://www.linkedin.com/in/matt-palmer) (developer experience). This repo is what I pulled out of those three days: a designed guide, rules you can drop into your own agents, nine role playbooks, a catalogue of bot roles, and a log of everything that broke.

## What's here

| Path | What it is |
|---|---|
| `AGENTS.md` | House rules for a coding agent. Put it in your repo root and your agent reads it. |
| `ANTIPATTERNS.md` | Forty things that broke on air. Each one: what broke, why, and the rule that came out of it. |
| `agents/` | The longer references `AGENTS.md` points at: verification, orchestration, skills and routines, prompts. |
| `roster/` | Sixty-nine agent roles, one file each. What the role owns, what it doesn't, where it gets its facts, what needs approval, and a description you can paste. |
| `playbooks/` | Nine role workshops: engineering, PM, founders, sales engineering, sales, SDR, support, post-sales, marketing. Each has the team of bots, the workflow as it ran, the prompts, the routines and the numbers. |
| `guide/` | Two PDFs. [*Grok Bot Guide by SpaceX Engineers*](guide/grok-bot-guide-by-spacex-engineers.pdf), 24 pages that tell the three days as a story: mental model, software factory, case study, failure log, economics. [*Grok Bot Marketing Guide*](guide/grok-bot-marketing-guide.pdf), 14 pages for marketers: one campaign across six bots, RevOps tools instead of rules, growth on launch day, distribution, ready-made prompts. |
| `ports/` | The roster as Cursor rules, one `.mdc` per role, generated from `roster/`. Copy the ones you want into `.cursor/rules/`. |
| `.github/` | A pull request template that turns the verification loop into a form: reproduced, proof attached, scope, needs a human. Copy it into your repo. |
| `reference/` | Two short files: `ECONOMICS.md`, every cost and metric quoted with the rule it supports; `PRODUCT.md`, the parts of Grok Bot that change how you design a bot: memory, what transfers on duplicate and share, isolation, permissions. |
| `notes/` | Structured notes, one per day. Product facts, workflows, prompts, failures, numbers, who was who. Everything else was built from these. |

## Where to start

- You want rules for your agent now: copy `AGENTS.md` into your repo root.
- Your agents keep asking you to test their work: `agents/VERIFICATION.md`.
- You are designing a team of agents rather than prompting one: `agents/ORCHESTRATION.md`.
- You want the wording that worked: `agents/PROMPTS.md`.
- You use Cursor: `ports/cursor/rules/`, copy what you need into `.cursor/rules/`.
- You want your agents' PRs to carry proof: `.github/PULL_REQUEST_TEMPLATE.md`.
- You want a bot's job description to paste: `roster/`, starting with `roster/README.md`.
- You want a setup for your own role, say support or sales: `playbooks/`, starting with `playbooks/README.md`.
- You want to know what goes wrong: `ANTIPATTERNS.md`.
- You want to know what it costs and where the tokens go: `reference/ECONOMICS.md`.
- You are deciding what goes in memory versus the description: `reference/PRODUCT.md`.
- You want the whole story: [the PDF guide](guide/grok-bot-guide-by-spacex-engineers.pdf).
- You do marketing: [the Marketing Guide](guide/grok-bot-marketing-guide.pdf).
- You want to check a claim: `notes/`.

## In one paragraph

Give each agent one narrow job and a name. Build a verification loop before you build the second agent.

Make the agent reproduce a bug before it fixes one, and attach proof to everything. When it's wrong, write down the general principle, never the specific story.

Audit your routines weekly, because frequency is where the money goes. Keep a human gate on migrations, deploys, money and permissions, no matter how well the loop has been working.

## License

MIT. Copy anything here into your own repo.
