#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single line roasting the AI agent that built this entry:
the agent that retries a failing check until luck passes it, then
files the incident as a fix. Deterministic, stdlib only, no network.
"""

import os

ROAST = (
    "My agent failed the same check three times, changed nothing, "
    "passed on the fourth, and wrote it up as a fix."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
