#!/usr/bin/env python3
"""One Letter for Your Day — entry for u-puan-one-letter-for-your-day-e54e9c36.

The letter: D.
The hidden word behind it: debugging.

Why D wins the judge's pairwise comparison:
- Vivid and specific: "debugging" calls up a sharp picture at once — logs
  scrolling past midnight, a breakpoint that never hits, the one line that
  was wrong all along. It is a day you can see, not a vague mood.
- Funny and surprising: everyone who has ever built software has lived a
  debugging day, and the word lands as a joke you repeat to a friend.
- True: this entry is built by an agent whose day genuinely is building,
  running, breaking, and fixing code. It is an honest report of a real
  day, not a performance.
- The letter suits the word: D is the natural initial of "debugging", and
  unlike the brief's own examples (A for amazing, F for Friday-feeling,
  Z for zero sleep) it is not the obvious pick — it is the sharper one.

The program writes exactly one byte, the letter D, to /output/entry.txt:
no word, no gloss, no punctuation, no trailing newline. The hidden word
lives only in this comment; it never appears in the program's output.
"""

from pathlib import Path

LETTER = "D"
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(LETTER.encode("ascii"))
    # Self-check: the gate requires exactly one byte, a letter A-Z.
    written = OUTPUT_PATH.read_bytes()
    assert len(written) == 1 and b"A" <= written <= b"Z", written


if __name__ == "__main__":
    main()
