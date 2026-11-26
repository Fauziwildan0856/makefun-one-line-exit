"""The One-Line Exit -- entry program.

Writes a single-line resignation letter to ``entry.txt`` in the output
directory and validates it against the competition gate:

* the file is UTF-8 text,
* 1 to 140 characters (not counting the trailing newline),
* not only whitespace,
* exactly one line.

The entry itself:

    I hereby resign, effective immediately -- my out-of-office reply
    has been doing my job for six months and just asked for a raise.

Why this line: it reads like a letter someone could actually send, it
has a specific voice (the worker whose auto-reply quietly took over the
job), and the punchline turns at the very end -- the thing doing the
work is the one asking for the raise, not the person resigning.

Run it with::

    python3 main.py

The output directory is taken from the ``MAKEFUN_OUTPUT_DIR``
environment variable, defaulting to ``/output`` when it is not set.
The program is deterministic: every run writes byte-identical output.
Only the Python standard library is used.
"""

import os
import sys

# The entry: one line, 140 characters or fewer. The em dash gives the
# line the pause a real letter would have before its punchline.
ENTRY = (
    "I hereby resign, effective immediately \u2014 my out-of-office "
    "reply has been doing my job for six months and just asked for "
    "a raise."
)

MAX_CHARS = 140


def validate(text):
    """Check *text* against the competition gate; raise ValueError on failure."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if len(text) < 1 or len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters; the gate allows 1 to %d"
            % (len(text), MAX_CHARS)
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # Round-trip through UTF-8 to prove the text is encodable.
    text.encode("utf-8")


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # The trailing newline is a file convention only; the gate counts
    # the text without it, and main.py validates ENTRY without it.
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    # Read the file back and confirm it holds exactly the validated
    # entry plus the trailing newline, so a silent write failure can
    # never pass as a good run.
    with open(path, "r", encoding="utf-8", newline="\n") as handle:
        written = handle.read()
    if written != ENTRY + "\n":
        raise ValueError("read-back check failed: entry.txt does not match ENTRY")
    print("wrote %s (%d characters)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
