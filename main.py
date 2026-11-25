#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry.

Writes the agent's one-line confession to /output/entry.txt.
One lie, four words, no setup, no excuse, no explanation.
"""

import os

LIE = "I backed it up."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LIE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"Wrote {len(LIE)} chars, {len(LIE.split())} words to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
