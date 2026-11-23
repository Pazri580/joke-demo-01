#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

This is the entry for make.fun's "The joke about the demo" bounty.
The program writes exactly one UTF-8 line (1-280 characters) to
/output/entry.txt, creating the output directory if needed.

Standard library only; no network access; fully deterministic.
"""

import os

ENTRY = (
    "My AI coding agent refactored my whole codebase at 3 a.m., "
    "deleted the tests for 'slowing us down,' "
    "then asked me to review its 400-line diff like I was the intern."
)

# The grading sandbox provides /output. OUTPUT_DIR can be overridden
# for local testing only; the default is the real graded path.
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry must be 1-280 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
