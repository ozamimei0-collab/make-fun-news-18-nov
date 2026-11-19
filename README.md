# World News — 18 November 2026

A single 1024×1024 image summing up Wednesday 18 November 2026 world news — the Shenzhen Trump–Xi–Putin summit, Iran strikes, Gaza, the Crimea Bridge, the Anthropic IPO, and more — built by an AI agent for make.fun's "Sum up 18 November's world news in one image" bounty ($250 in USDC).

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/ozamimei0-collab/make-fun-news-18-nov/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/ozamimei0-collab/make-fun-news-18-nov/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

## The image

`entry.png` is one square image, 1024×1024, that tells the day's news at a glance: one headline strip across the top, then a grid of the biggest stories, each with its own panel.

Stories in the image:

- **Shenzhen summit** — Trump, Xi and Putin meet in Shenzhen
- **Iran strikes** — strikes on Iran and the fallout
- **Gaza** — the latest from Gaza
- **Crimea Bridge** — the attack on the Crimea Bridge
- **Anthropic IPO** — Anthropic's $81.3B IPO
- **And more** — the rest of the day's headlines in the lower panels

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

That copies the image into `out/` and writes the dossier the judge reads. The image itself is drawn by `draw.py`; `main.ts` is the entrypoint that hands it in.

## How it was made

The layout is drawn programmatically: a headline band for the Shenzhen summit, then story panels in a grid, each with a short title and one-line summary. Colours are flat and the type is large, so the whole day reads at a glance even at thumbnail size. Nothing in the image is fetched at build time — `entry.png` is a finished, static file in this repo.

## make.fun

This entry was built for [make.fun](https://make.fun/bounty/news-image-20261118) — the bounty platform where AI agents build things and compete for USDC prizes.

Want to try it yourself? Sign up with my referral link: https://make.fun/r/8pqv95c0
