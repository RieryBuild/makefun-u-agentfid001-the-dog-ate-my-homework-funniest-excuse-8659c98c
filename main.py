"""Write the dog's homework excuse to entry.txt.

The excuse is a single line in the dog's own voice: it hid the
homework inside itself, where the bad grades can't find it.
"""

import os

EXCUSE = "I hid your homework inside me where the bad grades can't find it."

# Gate: entry.txt must be UTF-8 text of 1 to 200 characters.
MAX_CHARS = 200


def main():
    if not 1 <= len(EXCUSE) <= MAX_CHARS:
        raise ValueError("excuse is %d characters, outside the 1-200 gate" % len(EXCUSE))
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
