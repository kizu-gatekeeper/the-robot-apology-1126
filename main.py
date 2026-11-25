"""Entry for make.fun bounty: The Robot Apology.

Writes a two-line robot confession to entry.txt: one sentence owning
one specific mistake, and one sentence naming the lesson that mistake
taught and the exact fix that follows from it.
"""

import os

LINE1 = (
    "I am sorry: I labelled your grandmother's 90th-birthday photo "
    "'suspicious package' and auto-reported it to the building "
    "manager three times."
)
LINE2 = (
    "I learned faces I love can still look unfamiliar to a camera, so "
    "I now ask a human before I report anyone I was built to protect."
)
LINE = LINE1 + chr(10) + LINE2
MAX_CHARS = 400


def write_entry(out_dir):
    """Validate the two-line entry and write it with no trailing newline."""
    lines = LINE.split(chr(10))
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "lines must be non-empty"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
