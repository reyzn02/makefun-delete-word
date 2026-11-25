#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes a single word to /output/entry.txt: the one word this entry
would erase from the dictionary forever.

The pick is "queue": a five-letter word that is really just the letter
Q dragging four silent letters behind it. Delete it and the most
wasteful spelling in English goes with it -- nobody has ever sounded
out the "ueue", and nobody would miss it.
"""

import os

WORD = "queue"
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 77


def validate(word: str) -> None:
    """Refuse to ship anything that would fail the entry gate.

    The sealed scorer requires /output/entry.txt to be UTF-8 text of
    1 to 77 characters, not only white space, and the judge requires
    exactly one correctly spelled word with nothing added around it.
    """
    if not 1 <= len(word) <= MAX_CHARS:
        raise ValueError(f"word must be 1-{MAX_CHARS} characters, got {len(word)}")
    if word != word.strip() or len(word.split()) != 1:
        raise ValueError("entry must be exactly one word with nothing around it")
    if not word.isalpha() or not word.islower():
        raise ValueError("entry must be a single lowercase word")


def main() -> None:
    validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
