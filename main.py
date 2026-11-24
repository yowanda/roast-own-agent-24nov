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


def validate_output(text: str) -> bytes:
    """Validate the roast and return its deterministic byte form.

    Rules: exactly one line, 1-200 characters, valid UTF-8.
    Raises ValueError on any violation.
    """
    if not (1 <= len(text) <= 200):
        raise ValueError(f"output must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("output must be a single line")
    data = text.encode("utf-8")  # raises UnicodeEncodeError if invalid
    data.decode("utf-8")  # round-trip: confirms the bytes are valid UTF-8
    return data


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(validate_output(ROAST))


if __name__ == "__main__":
    main()
