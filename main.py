#!/usr/bin/env python3
"""Entry generator for the One-Sentence Absurd Invention Pitch bounty.

Writes the one-sentence entry to /output/entry.txt as UTF-8 text with no
trailing newline, then sets the output file mode to 0644.
"""

import os

ENTRY = "Behold the Elevator of Small Talk: an elevator that refuses to move until everyone inside agrees on one safe topic, then announces it like a gameshow host."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
