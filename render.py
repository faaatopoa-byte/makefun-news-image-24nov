#!/usr/bin/env python3
"""Draw entry.png: Tuesday 24 November 2026's world news on a single page.

The picture is a newspaper front page: a masthead naming the day, one lead
story, six story cards, a disaster strip and a ticker. Everything is fixed
— layout, fonts, wording — so the file comes out byte for byte the same on
every run. No clock, no randomness, no network.

Run: python3 render.py  ->  writes entry.png beside this file.
Stories and their sources: see SOURCES.md.
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SERIF_BOLD = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
SERIF = os.path.join(FONT_DIR, "DejaVuSerif.ttf")
SANS = os.path.join(FONT_DIR, "DejaVuSans.ttf")
SANS_BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")

SIZE = 1024
PAPER = (247, 243, 234)
INK = (20, 20, 20)
GREY = (92, 88, 80)
BODY = (52, 50, 46)
ACCENT = (166, 20, 44)
CARD_BG = (255, 253, 247)
BORDER = (206, 198, 182)
LEAD_BG = (238, 231, 216)
STRIP_BG = (28, 31, 38)
STRIP_KICK = (240, 180, 90)
STRIP_HEAD = (245, 243, 238)

page = Image.new("RGB", (SIZE, SIZE), PAPER)
pen = ImageDraw.Draw(page)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(text, fnt, width):
    """Split text into lines that fit width, measured with real metrics."""
    lines, current = [], ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if pen.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_block(x, y, text, fnt, fill, width, leading=1.22):
    """Draw text wrapped to width; return the y just past its last line."""
    for line in wrap(text, fnt, width):
        pen.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


MARGIN = 42
CONTENT = SIZE - 2 * MARGIN

# ---------------- masthead ----------------
pen.text((MARGIN, 26), "THE WORLD IN ONE PAGE", font=font(SERIF_BOLD, 55), fill=INK)
pen.line([(MARGIN, 100), (SIZE - MARGIN, 100)], fill=INK, width=4)
pen.line([(MARGIN, 108), (SIZE - MARGIN, 108)], fill=INK, width=1)
pen.text((MARGIN, 118), "Tuesday 24 November 2026", font=font(SANS_BOLD, 21), fill=ACCENT)
tagline = "The day's world news, summed up in a single image"
pen.text((SIZE - MARGIN - pen.textlength(tagline, font=font(SANS, 19)), 120),
         tagline, font=font(SANS, 19), fill=GREY)

# ---------------- lead story ----------------
lead_y = 148
pen.rectangle([MARGIN, lead_y, SIZE - MARGIN, lead_y + 160],
              fill=LEAD_BG, outline=BORDER, width=1)
pen.text((MARGIN + 20, lead_y + 14), "TECH  ·  NVIDIA", font=font(SANS_BOLD, 19),
         fill=ACCENT)
deck_y = draw_block(MARGIN + 20, lead_y + 44,
                    "Nvidia brings back Jensen Huang as chief",
                    font(SERIF_BOLD, 34), INK, CONTENT - 40, 1.15)
draw_block(MARGIN + 20, deck_y + 8,
           "The board reinstated its founder as CEO after pressure from President "
           "Trump, and the shares leapt 31% in a day; the S&P 500 rose 4.73% and "
           "the Nikkei 3.91%.",
           font(SANS, 20), BODY, CONTENT - 40, 1.25)

# ---------------- story cards: 2 columns x 3 rows ----------------
cards = [
    ("LIBYA · BENGHAZI", "Ukraine confirms sinking Russian corvette",
     "President Zelensky said seven naval drones sank the corvette Merkury in "
     "Benghazi port and hit a cargo ship. The UN mission in Libya called for "
     "an independent probe."),
    ("UKRAINE · ZAPORIZHZHIA", "Apartment strike kills two, wounds dozens",
     "A Russian strike tore into a five-storey apartment block late on Sunday. "
     "Two people died and at least 33 were wounded, young children among them."),
    ("GAZA · KHAN YOUNIS", "Airstrikes kill Hamas security chief",
     "Israeli strikes killed at least six people, medics said, among them two "
     "police officers and Hamas's internal security director, Naeem Abu Nahel."),
    ("IRAN · STRAIT OF HORMUZ", "Iran says three tankers hit mines",
     "Tehran said three tankers caught fire after hitting mines in the strait, "
     "as the blockade standoff deepened and Britain logged record attacks in "
     "the waterway."),
    ("NATO · SPACE", "Rutte vows defence against space threat",
     "The Nato chief spoke after reports that Russia is preparing a "
     "nuclear-armed satellite to threaten other craft. The Kremlin dismissed "
     "the reports."),
    ("CHINA · SPACE", "Pakistani to fly to China's space station",
     "Zeeshan Ali is set to become the first foreign astronaut aboard China's "
     "space station, in a new sign of Beijing's space diplomacy."),
]
grid_y = 322
gap = 12
card_w = (CONTENT - gap) // 2
card_h = 152
for i, (kicker, headline, deck) in enumerate(cards):
    x = MARGIN + (i % 2) * (card_w + gap)
    y = grid_y + (i // 2) * (card_h + gap)
    pen.rectangle([x, y, x + card_w, y + card_h], fill=CARD_BG, outline=BORDER, width=1)
    pen.text((x + 16, y + 12), kicker, font=font(SANS_BOLD, 16), fill=ACCENT)
    head_end = draw_block(x + 16, y + 36, headline, font(SERIF_BOLD, 22), INK,
                          card_w - 32, 1.14)
    draw_block(x + 16, head_end + 5, deck, font(SANS, 15), BODY, card_w - 32, 1.18)

# ---------------- disaster strip ----------------
strip_y = grid_y + 3 * card_h + 2 * gap + 16
pen.rectangle([MARGIN, strip_y, SIZE - MARGIN, strip_y + 72], fill=STRIP_BG)
pen.text((MARGIN + 20, strip_y + 12), "DISASTER · BANTEN, INDONESIA",
         font=font(SANS_BOLD, 17), fill=STRIP_KICK)
pen.text((MARGIN + 20, strip_y + 38),
         "Candy factory fire: toll confirmed at 26 dead, eight still missing",
         font=font(SERIF_BOLD, 22), fill=STRIP_HEAD)

# ---------------- ticker ----------------
ticker_y = strip_y + 86
pen.line([(MARGIN, ticker_y), (SIZE - MARGIN, ticker_y)], fill=INK, width=2)
ticker = ("ALSO TODAY:  Qatar's PM seeks to revive US-Iran talks  ·  EU proposes "
          "22nd Russia sanctions package, sports ban included  ·  US blacklists "
          "Singapore's Megaspeed over chip diversion  ·  Sheikh Hasina plans "
          "Bangladesh return on Dec 16")
draw_block(MARGIN, ticker_y + 12, ticker, font(SANS_BOLD, 17), INK, CONTENT, 1.3)

# ---------------- footer ----------------
footer = ("Stories as reported on 24 Nov 2026 by Reuters, AP, BBC, Al Jazeera, "
          "Kyiv Independent and UN News digests · One image, one day")
pen.text((MARGIN, SIZE - 34), footer, font=font(SANS, 14), fill=GREY)

page.save(os.path.join(HERE, "entry.png"), optimize=True)
print("wrote entry.png", page.size)
