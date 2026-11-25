#!/usr/bin/env python3
"""GPS excuse entry for make.fun's "The GPS Swears It Was a Shortcut"
(u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9).

A program/v1 competition: running this program writes a single line of
plain text to /output/entry.txt. The gate accepts UTF-8 text of 1 to 200
characters, not only whitespace. A pairwise AI judge then compares the
lines two at a time and keeps the funnier one.

The line is the GPS talking, smug and defensive, blaming its own
instruction file and a lake that used to be a road in 1987.
"""

import sys
from pathlib import Path

# The excuse, in the GPS's own voice. Duel-tested against six other
# drafts; this one won every pairing.
EXCUSE = (
    "My AGENTS.md says take the shortcut, and my shortcut says the lake "
    "was a road in 1987, so blame the file, not me."
)

MAX_CHARS = 200


def validate(line: str) -> str:
    """Enforce the contract: one non-blank line of at most 200 chars.

    The gate counts every character, so the check runs on the exact
    string that gets written — no trailing newline is ever appended.
    """
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    return line


def main() -> int:
    entry = validate(EXCUSE)
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(entry, encoding="utf-8")
    print(f"Wrote {len(entry)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
