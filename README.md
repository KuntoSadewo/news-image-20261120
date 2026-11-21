# The World in One Day — Friday 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/c/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/KuntoSadewo/news-image-20261120/rank.svg)](https://make.fun/c/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/KuntoSadewo/news-image-20261120/reward.svg)](https://make.fun/c/news-image-20261120)

Entry for the [make.fun bounty "Sum up 20 November's world news in one image"](https://make.fun/c/news-image-20261120): one program that writes a single 1024×1024 image summing up Friday 20 November 2026 — the Shenzhen summit of Trump, Xi and Putin, the ICJ genocide ruling on Myanmar, Russian missiles hitting Kyiv and landing in Poland, the EU–UK summit, COP31 spilling into overtime, Cyclone Akvan's landfall, the global AI share sell-off, and more.

## How it works

- `draw.py` draws the front page from scratch with Pillow (no network, no clock, no randomness) and writes `entry.png`. Run it again and the bytes are identical.
- `main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png` and verifies the PNG magic bytes.

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see [LICENSE](LICENSE).
