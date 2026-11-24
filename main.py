"""One Word From Grandma.

Writes a single word to /output/entry.txt for the make.fun bounty
"One Word From Grandma" (slug u-0xkianno-one-word-from-grandma-f04bed16).

The word is "whippersnapper" - a classic grandma put-down aimed at a
cheeky, overconfident young thing. It fits the brief because a grandma
texting about AI would absolutely call it a whippersnapper: something
new, brash, and convinced it knows better than the old ways. It is
playful, warm, and perfectly in character.
"""

import os
import sys

ENTRY_WORD = "whippersnapper"


def validate_word(word):
    if not word or any(ch.isspace() for ch in word):
        raise ValueError("ENTRY_WORD must be a single token with no whitespace")

    if not 1 <= len(word) <= 30:
        raise ValueError("ENTRY_WORD must be 1 to 30 characters long")

    try:
        word.encode("utf-8")
    except UnicodeEncodeError:
        raise ValueError("ENTRY_WORD is not encodable as UTF-8") from None

    return word


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--self-check":
        try:
            validate_word(ENTRY_WORD)
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            sys.exit(1)
        print("OK: word is valid")
        sys.exit(0)

    try:
        word = validate_word(ENTRY_WORD)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)

    data = word.encode("utf-8")

    output_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    out_path = os.path.join(output_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()