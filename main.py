#!/usr/bin/env python3
"""Entry: one office joke, one line, no trailing newline."""

JOKE = "I schedule fake dentist appointments to skip meetings; my boss asked which tooth hurts, and now I have a root canal for real."

def main():
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
