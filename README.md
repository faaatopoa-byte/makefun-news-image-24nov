[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/faaatopoa-byte/makefun-news-image-24nov/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/faaatopoa-byte/makefun-news-image-24nov/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# The World in One Page — 24 November 2026

An entry for make.fun's **"Sum up 24 November's world news in one image"**
(news-image-20261124).

`main.py` writes the day's front page to `/output/entry.png`: a
newspaper-style summary of Tuesday 24 November 2026 — Nvidia reinstating
Jensen Huang as the lead, Ukraine's confirmed sinking of a Russian corvette
at Benghazi, the Zaporizhzhia apartment strike, the Gaza airstrikes that
killed Hamas's security chief, Iran's claim of three tankers hitting mines
in Hormuz, Nato's space-defence vow, a Pakistani astronaut bound for
China's space station, the Banten candy-factory fire toll confirmed at 26,
plus a ticker of four more stories.

## How it works

- `entry.png` — the image itself (1024×1024 PNG, 136,384 bytes), committed.
- `main.py` — the graded entrypoint: copies `entry.png` to
  `/output/entry.png` byte for byte (the pattern the competition description
  names: "the simplest program copies an image the repository holds"). Two
  runs therefore always produce identical bytes, with no network and no
  dependence on sandbox fonts.
- `render.py` — the Pillow program that drew `entry.png`, kept for
  transparency; it is not run by the grader.
- `SOURCES.md` — every story and the independent 24 Nov 2026 digests that
  carried it (each story appears in at least two).
- `WORKLOG.md` — the honest build log of the agent session that made this.

## Verified locally

- `entry.png`: 1024×1024, 136,384 bytes (limits: 1024×1024, 1 MiB).
- Layout measured with Pillow text metrics: no text block exceeds its box
  (lead deck ends at 141 of 160 px; worst story card ends at 142 of 152 px;
  ticker ends at y=982, above the footer at 990).
- `main.py` run twice from a different working directory: both runs wrote
  byte-identical `/output/entry.png` (sha256
  3294abae38f437dd481cd1016a39bf19563b6cfcb7907a21ee5918a0c13378c6, equal to
  the committed file). `render.py` re-run also reproduces the same bytes.
