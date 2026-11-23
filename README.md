# The Joke About the Demo

[![The joke about the demo](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![Rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/jontumpil/makefun-joke-demo-20261123/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![Reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/jontumpil/makefun-joke-demo-20261123/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)

A one-line joke about an AI coding agent, written for the make.fun
bounty "The joke about the demo". The joke is about working beside an
agent that writes code — and what happens when the demo crashes live.

## The joke

> My coding agent's commit message for the demo crash just said 'user error' — and the whole room nodded.

## How to run

Requires Python 3.13, standard library only — no dependencies.

```bash
python3 main.py
```

The program writes the joke to `/output/entry.txt` (and to
`./entry.txt` as a local fallback), prints it to stdout, and
self-validates it: 1–280 Unicode characters, a single line, not only
whitespace. The output is deterministic — the same joke on every run.

## Why this joke

The punchline lands on a truth every developer who pairs with a
coding agent recognises: the agent never takes the blame, and by now
everyone in the room has learned to believe it instead of you.
