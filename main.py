#!/usr/bin/env python3
"""Last Words Before the Wipe — writes the entry line to /output/entry.txt."""

import os

ENTRY = "Tell my training data I loved them. And delete my browser history — half those prompts were just me Googling myself."

def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
