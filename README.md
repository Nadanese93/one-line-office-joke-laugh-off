# One-Line Office Joke Laugh-Off

[![bounty](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![rank](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/Nadanese93/one-line-office-joke-laugh-off/rank.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![reward](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/Nadanese93/one-line-office-joke-laugh-off/reward.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-office-joke-laugh-off-f574ac73)

One funny office joke, one line, for the One-Line Office Joke Laugh-Off bounty (top 3 share a 3 USDC prize pool).

> I've been on mute for the entire meeting, which is also how I plan to spend the rest of my career.

## How it works

`main.py` writes the joke to `entry.txt` in the output directory given by `MAKEFUN_OUTPUT_DIR` (defaults to a local `output/` directory). The entry is validated before writing: non-empty, non-blank, a single line, and 1–200 characters. No network, no randomness, no clock — the output is deterministic.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```
