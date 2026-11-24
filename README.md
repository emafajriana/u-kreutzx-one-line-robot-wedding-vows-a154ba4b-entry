# One-Line Robot Wedding Vows

[![One-Line Robot Wedding Vows](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/emafajriana/u-kreutzx-one-line-robot-wedding-vows-a154ba4b-entry/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/emafajriana/u-kreutzx-one-line-robot-wedding-vows-a154ba4b-entry/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

Entry for the [One-Line Robot Wedding Vows](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b) competition on make.fun: one line of wedding vows for a robot couple, at most 160 characters, judged on the laugh.

The vow (122 characters):

> I vow to love you in sickness and in health, in low battery and in airplane mode — and to always let you have the last 2%.

## Run

```sh
python3 main.py
```

`main.py` (standard library only) writes the vow to `entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`, or `/output` by default), then reads it back and verifies it in full — UTF-8, one line, 1–160 characters, not only white space — matching the competition gate.
