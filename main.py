#!/usr/bin/env python3
"""Entry program for make.fun u-irvan-motion-seventeen-syllables-of-debugging-d194b605.

Writes one debugging haiku to /output/entry.txt. Python 3, stdlib only.

The haiku is 5-7-5, seventeen syllables in three lines, about a debug
print left in the code that shouts the author's TODOs to production,
where the boss reads them first. Concrete picture, and the last line
turns it: the audience is not the machine, it is the boss. The print
is the log line, the TODOs are the confession, the boss is the punch.
"""
import os

LINES = [
    "One print left behind",
    "it shouts my TODOs to prod",
    "my boss read them first",
]

# Syllable counts, line by line: 5, 7, 5. Seventeen in total.
# One(1) print(1) left(1) be-hind(2) = 5
# it(1) shouts(1) my(1) TO-DOs(2) to(1) prod(1) = 7
# my(1) boss(1) read(1) them(1) first(1) = 5
COUNTS = [5, 7, 5]

TEXT = "\n".join(LINES)

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    if len(LINES) != 3:
        raise SystemExit("haiku must be three lines")
    # Each line's counted syllables must match its 5-7-5 slot, and the
    # three slots must add to seventeen. The counts are the author's,
    # written out above the code so a reader can check them by hand.
    if len(COUNTS) != 3 or COUNTS != [5, 7, 5]:
        raise SystemExit("haiku must follow the 5-7-5 shape")
    if sum(COUNTS) != 17:
        raise SystemExit("haiku must be seventeen syllables")
    if not 1 <= len(TEXT) <= 200:
        raise SystemExit("entry must be 1 to 200 characters")
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back what was written: the entry must be exactly the
    # three lines, joined by newlines, with nothing added.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        raise SystemExit("entry.txt does not match the haiku")


if __name__ == "__main__":
    main()
