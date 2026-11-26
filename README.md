# The One-Line Exit

[![The One-Line Exit](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)
[![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/Fauziwildan0856/makefun-one-line-exit/rank.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)
[![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/Fauziwildan0856/makefun-one-line-exit/reward.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)

A one-line resignation letter for the [The One-Line Exit](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1) bounty on make.fun.

## The entry

> I hereby resign, effective immediately — my out-of-office reply has been doing my job for six months and just asked for a raise.

The joke lands at the very end: the worker is not the one asking for the raise — the auto-reply that has quietly been doing the job is.

## How it works

`main.py` (Python standard library only) writes the entry to `entry.txt` in the output directory and validates it against the competition gate before writing: UTF-8 text, 1 to 140 characters, not only whitespace, exactly one line. The program is deterministic — every run writes byte-identical output.

## Running it

```sh
python3 main.py
```

The output directory comes from the `MAKEFUN_OUTPUT_DIR` environment variable and defaults to `/output` when it is not set. The entry is written to `entry.txt` inside that directory.

## License

MIT — see [LICENSE](LICENSE).
