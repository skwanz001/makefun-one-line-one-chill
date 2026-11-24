#!/usr/bin/env python3
"""One Line, One Chill - make.fun entry.

Writes a single horror sentence to /output/entry.txt.
Standard library only.
"""

import os

LINE = "I keep a spare key under the mat for emergencies, and this morning it was gone, replaced by a tooth, still warm."


def main() -> None:
    text = LINE.strip()
    # Mirror the sealed gate: UTF-8 text, 1 to 200 characters, not only whitespace.
    if not (1 <= len(text) <= 200) or not text.strip():
        raise SystemExit(f"entry must be 1-200 non-blank characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
