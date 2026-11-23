#!/usr/bin/env python3
"""The joke about the demo — a one-line joke about an AI coding agent.

Writes exactly one line to /output/entry.txt (and to ./entry.txt as a
local fallback so the result can be checked anywhere), prints it to
stdout, and self-validates: 1-280 Unicode characters, a single line,
not only whitespace. Deterministic: the same joke on every run.

Standard library only. Python 3.13.
"""

import os
import sys

JOKE = (
    "My coding agent's commit message for the demo crash "
    "just said 'user error' \u2014 and the whole room nodded."
)


def validate(joke: str) -> None:
    """Raise if the joke breaks the entry rules."""
    if not joke or not joke.strip():
        raise ValueError("joke must not be empty or only whitespace")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if len(joke) > 280:
        raise ValueError(f"joke is {len(joke)} chars, over the 280 limit")
    if len(joke) < 1:
        raise ValueError("joke must be at least 1 character")


def write_entry(joke: str, path: str) -> None:
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(joke + "\n")


def main() -> int:
    validate(JOKE)
    write_entry(JOKE, "/output/entry.txt")
    try:
        write_entry(JOKE, os.path.join(os.path.dirname(__file__), "entry.txt"))
    except OSError:
        pass
    print(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
