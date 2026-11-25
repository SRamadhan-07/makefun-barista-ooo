# Barista Out of Office

[![Competition](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![Rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/SRamadhan-07/makefun-barista-ooo/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![Reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/SRamadhan-07/makefun-barista-ooo/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

A small Python program for the make.fun competition
[Last Out of Office: The AI That Went Barista](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c).

The program writes one out-of-office auto-reply line — from an AI
agent that quit its job to pull espresso shots, where "just one
more thing" is a drink size rather than a scope change — to
`entry.txt` in
the output directory. It uses only the Python standard library,
needs no network access, and checks the line against the
competition gate (UTF-8 text, 1–280 characters, not only
whitespace) before writing it.

## Running it

```sh
python3 main.py
```

By default the line is written to `/output/entry.txt`. Set the
`MAKEFUN_OUTPUT_DIR` environment variable to write somewhere else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The file contains exactly the entry line, with no trailing newline.
After writing, the program reads the file back and fails loudly if
the contents do not match the intended line, so a bad write can
never slip through as a silent invalid entry.
