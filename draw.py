#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news front page (1024x1024, entry.png).

Newspaper front-page style. Every fact is dated Wednesday 18 November 2026.
No tiny body text: headlines >= 22px, summaries >= 17px, lead text >= 22px.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
M = 28  # margin

PAPER = (246, 241, 229)
INK = (26, 26, 26)
RED = (164, 30, 34)
BLUE = (31, 58, 110)
GOLD = (198, 148, 42)
GREY = (90, 90, 90)
LIGHT_LINE = (180, 172, 150)

FONT_DIR = "/usr/share/fonts/truetype/noto/"
BLACK = FONT_DIR + "NotoSans-Black.ttf"
BOLD = FONT_DIR + "NotoSans-Bold.ttf"
REG = FONT_DIR + "NotoSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, spacing=4):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def tag(draw, x, y, text, color):
    """Small caps section tag with a coloured rule."""
    f = font(BOLD, 15)
    draw.text((x, y), text, font=f, fill=color)
    draw.line([(x, y + 22), (x + 54, y + 22)], fill=color, width=3)
    return y + 30


def card(draw, x, y, w, h, tag_text, color, headline, summary):
    draw.rectangle([x, y, x + w, y + h], outline=LIGHT_LINE, width=2)
    px, py = x + 12, y + 10
    py = tag(draw, px, py, tag_text, color)
    hf = font(BOLD, 22)
    hl = wrap(draw, headline, hf, w - 24)
    py = draw_lines(draw, hl[:2], px, py, hf, INK, spacing=1)
    sf = font(REG, 17)
    sl = wrap(draw, summary, sf, w - 24)
    draw_lines(draw, sl[:2], px, py + 2, sf, (52, 52, 52), spacing=2)


def skyline_scene(draw, x, y, w, h):
    """Simple drawn scene: Shenzhen skyline at dusk, three flags, APEC banner."""
    draw.rectangle([x, y, x + w, y + h], fill=(24, 38, 74))
    # sun
    draw.ellipse([x + w - 78, y + 26, x + w - 22, y + 82], fill=GOLD)
    # buildings
    import random
    rnd = random.Random(18)
    bx = x
    while bx < x + w - 30:
        bw = rnd.randint(28, 52)
        bh = rnd.randint(70, 150)
        draw.rectangle([bx, y + h - 46 - bh, bx + bw, y + h - 46], fill=(52, 74, 128))
        # lit windows
        for wy in range(y + h - 40 - bh, y + h - 56, 18):
            for wx in range(bx + 6, bx + bw - 8, 14):
                if rnd.random() < 0.45:
                    draw.rectangle([wx, wy, wx + 5, wy + 7], fill=(255, 214, 120))
        bx += bw + 6
    draw.rectangle([x, y + h - 46, x + w, y + h], fill=(16, 26, 52))
    # three flag poles with simple flags
    poles = [
        (x + 34, [(232, 232, 232), (178, 34, 52), (232, 232, 232), (178, 34, 52)]),  # US stripes hint
        (x + 108, [(222, 32, 40)]),  # China red
        (x + 182, [(255, 255, 255), (0, 57, 166), (213, 0, 50)]),  # Russia tricolour
    ]
    for px, stripes in poles:
        draw.line([(px, y + 96), (px, y + h - 46)], fill=(220, 220, 220), width=3)
        fh = 34 // len(stripes)
        for i, col in enumerate(stripes):
            draw.rectangle([px, y + 96 + i * fh, px + 46, y + 96 + (i + 1) * fh], fill=col)
        draw.ellipse([px - 3, y + 91, px + 3, y + 97], fill=GOLD)
    # caption
    cf = font(BOLD, 19)
    draw.text((x + 16, y + h - 40), "APEC  •  SHENZHEN", font=cf, fill=(255, 255, 255))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    mf = font(BLACK, 92)
    title = "WORLD NEWS"
    tw = d.textlength(title, font=mf)
    d.text(((W - tw) / 2, 14), title, font=mf, fill=INK)
    d.line([(M, 122), (W - M, 122)], fill=INK, width=4)
    d.line([(M, 130), (W - M, 130)], fill=INK, width=2)
    df = font(BOLD, 30)
    date = "WEDNESDAY  18  NOVEMBER  2026"
    dw = d.textlength(date, font=df)
    d.text(((W - dw) / 2, 140), date, font=df, fill=RED)
    d.line([(M, 176), (W - M, 176)], fill=INK, width=2)

    # ---- Lead story ----
    ly, lh = 188, 292
    lx, lw = M, 640
    tag(d, lx, ly, "DIPLOMACY", RED)
    hf = font(BOLD, 40)
    headline = "TRUMP, XI AND PUTIN MEET IN SHENZHEN"
    hl = wrap(d, headline, hf, lw)
    y = draw_lines(d, hl, lx, ly + 32, hf, INK, spacing=2)
    sf = font(REG, 22)
    summary = ("Trump arrives for APEC as Xi greets him with a hug. "
               "First-ever trilateral meeting set for Thursday.")
    sl = wrap(d, summary, sf, lw)
    y = draw_lines(d, sl, lx, y + 6, sf, (52, 52, 52), spacing=4)
    bf = font(BOLD, 21)
    d.text((lx, y + 8), "Xi attacks US tariffs; Putin hits Western sanctions.",
           font=bf, fill=BLUE)
    # scene panel on the right
    skyline_scene(d, M + lw + 16, ly, W - M - (M + lw + 16), lh)
    d.line([(M, ly + lh + 12), (W - M, ly + lh + 12)], fill=INK, width=2)

    # ---- Story cards: 3 x 3 ----
    stories = [
        ("CONFLICT", RED, "IRAN STRIKES KUWAIT AND BAHRAIN",
         "Tehran hits US bases after a US strike on Qeshm Island."),
        ("CONFLICT", RED, "ISRAELI TANKS CROSS GAZA'S YELLOW LINE",
         "First ground raid since the ceasefire; three killed."),
        ("CONFLICT", RED, "CRIMEA BRIDGE HIT A THIRD TIME",
         "Traffic halted after a third attack in three days."),
        ("TECH", BLUE, "ANTHROPIC PRICES BIGGEST IPO EVER",
         "$83 a share raises $81.3bn; trading begins Thursday as ANT."),
        ("MARKETS", BLUE, "FED TURNS HAWKISH; DOW FALLS 1.1%",
         "Waller floats a 50bp December hike; minutes point to more rises."),
        ("ECONOMY", BLUE, "UK INFLATION HITS 3.6% IN OCTOBER",
         "Highest in a year; January energy bills forecast up £443 a year."),
        ("ASIA", RED, "BANGLADESH DEPLOYS TROOPS NATIONWIDE",
         "Paramilitary out over Hasina's return; 71 arrested in a day."),
        ("CULTURE", GOLD, "VAN GOGH SELLS FOR RECORD $190.4M",
         "Blossoming Chestnut Trees tops the Sotheby's New York sale."),
        ("HEALTH", (0, 110, 70), "WHO: ANTIBIOTICS FAILING VS SUPERBUGS",
         "Klebsiella infections up 72% since 2019."),
    ]
    gx, gy = M, 504
    cw, ch, gap = 313, 132, 12
    for i, (tg, col, head, summ) in enumerate(stories):
        cx = gx + (i % 3) * (cw + gap)
        cy = gy + (i // 3) * (ch + gap)
        card(d, cx, cy, cw, ch, tg, col, head, summ)

    # ---- Bottom strip: gaming + sport ----
    sy = gy + 3 * ch + 2 * gap + 12  # 928
    d.line([(M, sy - 6), (W - M, sy - 6)], fill=INK, width=2)
    sf = font(REG, 18)
    hf = font(BOLD, 20)
    # left: PSN / GTA VI
    d.text((M, sy), "GAMING", font=font(BOLD, 15), fill=BLUE)
    d.text((M + 82, sy - 2), "PSN falters before GTA VI unlocks",
           font=hf, fill=INK)
    d.text((M, sy + 26), "4,000+ US outage reports; first unlocks in NZ at 11:00 UTC.",
           font=sf, fill=(52, 52, 52))
    # right: Mata
    rx = 560
    d.text((rx, sy), "SPORT", font=font(BOLD, 15), fill=RED)
    d.text((rx + 74, sy - 2), "Juan Mata retires at 38",
           font=hf, fill=INK)
    d.text((rx, sy + 26), "Spain's 2010 World Cup winner bows out at 38.",
           font=sf, fill=(52, 52, 52))

    # ---- Footer ----
    ff = font(REG, 14)
    foot = "All stories dated Wednesday 18 November 2026  •  Sources: wire reports"
    fw = d.textlength(foot, font=ff)
    d.text(((W - fw) / 2, 996), foot, font=ff, fill=GREY)

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
