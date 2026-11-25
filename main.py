#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single one-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: no network, no randomness, no clock.
"""

import os
import sys

ENTRY = "I've been on mute for the entire meeting, which is also how I plan to spend the rest of my career."


class LengthError(ValueError):
    """Entry is empty or outside the 1-200 character gate."""


class BlankError(ValueError):
    """Entry contains only whitespace."""


class MultiLineError(ValueError):
    """Entry contains a newline or carriage return."""


def validate(entry: str) -> None:
    if not 1 <= len(entry) <= 200:
        raise LengthError(
            f"entry must be 1-200 characters, got {len(entry)}"
        )
    if not entry.strip():
        raise BlankError("entry must not be only whitespace")
    if "\n" in entry or "\r" in entry:
        raise MultiLineError("entry must be a single line")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output"
    )
    os.makedirs(out_dir, exist_ok=True)

    validate(ENTRY)

    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Read-back verification: the bytes on disk must match exactly.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("read-back verification failed: entry.txt bytes differ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
