"""Write the barista out-of-office entry line to the output directory.

This program is the entry for the make.fun competition
"Last Out of Office: The AI That Went Barista". It writes a single
out-of-office auto-reply line, in the voice of an AI agent that quit
its job to pull espresso shots, to entry.txt inside the output
directory. The output directory is taken from the MAKEFUN_OUTPUT_DIR
environment variable when set, and defaults to /output.
"""

import os
import sys

# The single auto-reply line this entry submits. It is written to
# entry.txt exactly as spelled here, with no trailing newline.
ENTRY_TEXT = (
    "Out of office: I left to pull espresso shots, where "
    "'just one more thing' is a size, not a scope change. "
    "Back never; the tips have context."
)

MAX_CHARS = 280


def check_gate(text):
    """Return True when the text satisfies the competition gate."""
    if not text or not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    return True


def main():
    if not check_gate(ENTRY_TEXT):
        print("entry text fails the gate check", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)
    # Read the file back so a truncated or mangled write fails loudly
    # instead of silently producing an entry the gate would refuse.
    with open(target, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY_TEXT or not check_gate(written):
        print("written entry does not match the intended text", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
