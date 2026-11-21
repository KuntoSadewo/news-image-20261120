#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news front page (1024x1024 PNG).

Deterministic: no network, no clock, no randomness. Every run writes
identical bytes for the same source.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 243, 234)
NAVY = (14, 42, 71)
GOLD = (201, 162, 39)
INK = (24, 24, 24)
RED = (178, 34, 34)
TEAL = (15, 118, 110)
GREY = (90, 90, 90)
PANEL = (255, 255, 255)
LINE = (180, 175, 160)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def panel(draw, x, y, w, h, tag, tag_color, title, body, accent):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10,
                           fill=PANEL, outline=LINE, width=2)
    draw.rounded_rectangle([x, y, x + w, y + 30], radius=10, fill=accent)
    draw.rectangle([x, y + 20, x + w, y + 30], fill=accent)
    draw.text((x + 12, y + 6), tag, font=font(BOLD, 15), fill=(255, 255, 255))
    ty = y + 40
    for ln in wrap(draw, title, font(BOLD, 20), w - 24):
        draw.text((x + 12, ty), ln, font=font(BOLD, 20), fill=INK)
        ty += 25
    ty += 4
    for ln in wrap(draw, body, font(REG, 15), w - 24):
        draw.text((x + 12, ty), ln, font=font(REG, 15), fill=(50, 50, 50))
        ty += 19


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 154], fill=GOLD)
    d.text((32, 18), "THE WORLD IN ONE DAY", font=font(BOLD, 58), fill=(255, 255, 255))
    d.text((32, 92), "FRIDAY  •  20 NOVEMBER 2026", font=font(BOLD, 30), fill=GOLD)
    d.text((32, 126), "Eight stories from one day, around the world",
           font=font(REG, 18), fill=(200, 210, 225))

    # Hero: Shenzhen summit
    hx, hy, hw, hh = 24, 170, 976, 250
    d.rounded_rectangle([hx, hy, hx + hw, hy + hh], radius=12,
                        fill=(255, 255, 255), outline=LINE, width=2)
    d.rounded_rectangle([hx, hy, hx + hw, hy + 40], radius=12, fill=RED)
    d.rectangle([hx, hy + 28, hx + hw, hy + 40], fill=RED)
    d.text((hx + 14, hy + 9), "LEAD STORY  •  SHENZHEN, CHINA",
           font=font(BOLD, 17), fill=(255, 255, 255))
    d.text((hx + 14, hy + 52), "Trump, Xi and Putin meet;",
           font=font(BOLD, 30), fill=INK)
    d.text((hx + 14, hy + 90), "joint peace declaration",
           font=font(BOLD, 30), fill=INK)
    hero_body = ("The US, Chinese and Russian leaders held a historic "
                 "three-way summit in Shenzhen and issued a joint peace "
                 "declaration. Germany warned Europe must not be left out "
                 "of any deal over its own future.")
    ty = hy + 134
    for ln in wrap(d, hero_body, font(REG, 18), 560):
        d.text((hx + 14, ty), ln, font=font(REG, 18), fill=(50, 50, 50))
        ty += 24
    # Three flags over a table, drawn as simple blocks
    fx, fy = hx + 640, hy + 60
    d.rounded_rectangle([fx - 20, fy + 120, fx + 300, fy + 150], radius=8, fill=(120, 72, 20))
    for i, (c1, c2) in enumerate([((178, 34, 34), (255, 255, 255)),
                                  ((222, 41, 16), (255, 215, 0)),
                                  ((255, 255, 255), (0, 57, 166))]):
        x0 = fx + i * 100
        d.rectangle([x0, fy, x0 + 80, fy + 55], fill=c1, outline=INK, width=2)
        d.rectangle([x0, fy + 55, x0 + 80, fy + 62], fill=c2)
        d.rectangle([x0 + 38, fy + 55, x0 + 42, fy + 122], fill=INK)
    d.text((fx - 8, fy + 158), "USA  •  CHINA  •  RUSSIA",
           font=font(BOLD, 15), fill=GREY)

    # Six panels, 2 columns x 3 rows
    px, py = 24, 436
    pw, ph, gap = 482, 146, 12
    panels = [
        ("JUSTICE  •  THE HAGUE", NAVY,
         "World court: Myanmar committed genocide",
         "The International Court of Justice ruled Myanmar's forces "
         "committed state-sponsored genocide against the Rohingya."),
        ("WAR IN UKRAINE  •  KYIV & POLAND", RED,
         "Russian missiles hit Kyiv; two land in Poland",
         "Overnight strikes hit Kyiv bridges, killing three. Poland "
         "called the border landings a deliberate provocation."),
        ("EUROPE  •  BRUSSELS", TEAL,
         "EU and UK sign new deals",
         "Britain and the EU agreed deals on food trade, carbon "
         "markets and youth mobility at their Brussels summit."),
        ("CLIMATE  •  ANTALYA", (90, 60, 120),
         "COP31 talks spill into overtime",
         "After two weeks, negotiators are deadlocked. The draft deal "
         "drops all mention of fossil fuels and adaptation finance."),
        ("WEATHER  •  EAST INDIA", (0, 110, 140),
         "Cyclone Akvan makes landfall",
         "The storm crossed the Odisha coast near Gopalpur with winds "
         "of 70-80 km/h, bringing heavy rain to eastern India."),
        ("MARKETS  •  WORLDWIDE", (120, 60, 0),
         "Shares slide as AI sell-off spreads",
         "The S&P 500 fell 3.7% into correction territory and Japan's "
         "Nikkei dropped 5.1% on fears over the cost of AI."),
    ]
    for i, (tag, color, title, body) in enumerate(panels):
        x = px + (i % 2) * (pw + gap)
        y = py + (i // 2) * (ph + gap)
        panel(d, x, y, pw, ph, tag, color, title, body, color)

    # Footer strip: also today
    fy0 = 918
    d.rounded_rectangle([24, fy0, 1000, 1000], radius=10, fill=NAVY)
    d.text((40, fy0 + 10), "ALSO TODAY:", font=font(BOLD, 18), fill=GOLD)
    d.text((40, fy0 + 38),
           "Magnitude 6.7 earthquake hits central Peru  •  BepiColombo reaches Mercury after 8 years  •  World Children's Day",
           font=font(REG, 16), fill=(255, 255, 255))

    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
