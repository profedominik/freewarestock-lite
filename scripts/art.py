"""Procedural flat-vector illustrations for each vocabulary word.

Every drawing is original, hand-coded SVG on a 512x512 canvas, released CC0.
Style: thick dark outline, flat fills, soft pastel background tile, no text
(so images stay language-neutral).
"""
import math

OUT = "#2b2d42"
SW = 8

# palette
SKIN = "#f5c9a0"
SKIN2 = "#c68c5a"
HAIR = "#6b3e26"
BLONDE = "#f2c14e"
RED = "#e63946"
DRED = "#b5172a"
BLUE = "#457b9d"
NAVY = "#1d3557"
LBLUE = "#a8dadc"
SKY = "#cfe8ff"
GREEN = "#52b788"
DGREEN = "#2d6a4f"
LGREEN = "#95d5b2"
YELLOW = "#ffd166"
ORANGE = "#f4a261"
DORANGE = "#e76f51"
PINK = "#f4a6c1"
PURPLE = "#9b5de5"
BROWN = "#a0522d"
DBROWN = "#6f3b1f"
TAN = "#d4a373"
GREY = "#adb5bd"
DGREY = "#6c757d"
WHITE = "#ffffff"
CREAM = "#fff3d6"

CATEGORY_BG = {
    "people": "#ffe5d9",
    "home": "#fdf0d5",
    "transport": "#dbeafe",
    "animals": "#e9f5db",
    "food": "#fff1e6",
    "nature": "#d8f3dc",
    "things": "#ede7f6",
    "clothes": "#fce4ec",
    "body": "#ffe8d6",
    "school": "#e0f2f1",
}
NIGHT = "#22305a"


# ---------------------------------------------------------------- primitives
def C(cx, cy, r, fill=WHITE, extra=""):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" {extra}/>'


def E(cx, cy, rx, ry, fill=WHITE, extra=""):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" {extra}/>'


def R(x, y, w, h, fill=WHITE, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>'


def P(d, fill="none", extra=""):
    return f'<path d="{d}" fill="{fill}" {extra}/>'


def PL(pts, fill=WHITE, extra=""):
    s = " ".join(f"{x},{y}" for x, y in pts)
    return f'<polygon points="{s}" fill="{fill}" {extra}/>'


def L(x1, y1, x2, y2, w=SW, color=OUT):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"/>'


def NS(s):
    """no-stroke group"""
    return f'<g stroke="none">{s}</g>'


def dot(cx, cy, r=8, fill=OUT):
    return C(cx, cy, r, fill, 'stroke="none"')


def limb(d, color, w=28):
    """thick outlined stroke (arms, handles, tails...)"""
    return (f'<path d="{d}" fill="none" stroke="{OUT}" stroke-width="{w + 2 * SW}"/>'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}"/>')


def ring(cx, cy, r, color, w=22):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{OUT}" stroke-width="{w + 2 * SW}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="{w}"/>')


def merged(shapes, fill):
    """overlapping shapes rendered as one outlined silhouette"""
    shapes = shapes.replace(f'fill="{WHITE}"', "")
    return f'<g fill="{fill}">{shapes}</g><g fill="{fill}" stroke="none">{shapes}</g>'


def rot(deg, cx, cy, s):
    return f'<g transform="rotate({deg} {cx} {cy})">{s}</g>'


def tr(x, y, s, scale=1):
    return f'<g transform="translate({x} {y}) scale({scale})">{s}</g>'


def shadow(cx=256, cy=440, rx=150, ry=16):
    return E(cx, cy, rx, ry, "#000", 'stroke="none" opacity="0.08"')


def shine(d):
    return f'<path d="{d}" fill="none" stroke="#fff" stroke-width="10" opacity="0.7"/>'


def scallop(cx, cy, rx, ry, n, start=0):
    """bumpy closed outline (wool, mane, cloud edges)"""
    pts = []
    for i in range(n):
        a = start + 2 * math.pi * i / n
        pts.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f} "
    for i in range(n):
        x2, y2 = pts[(i + 1) % n]
        x1, y1 = pts[i]
        r = math.hypot(x2 - x1, y2 - y1) * 0.62
        d += f"A{r:.1f},{r:.1f} 0 0 1 {x2:.1f},{y2:.1f} "
    return d + "Z"


def star_pts(cx, cy, ro, ri, n=5, start=-90):
    pts = []
    for i in range(2 * n):
        r = ro if i % 2 == 0 else ri
        a = math.radians(start + 180 * i / n)
        pts.append((round(cx + r * math.cos(a), 1), round(cy + r * math.sin(a), 1)))
    return pts


def eyes(cx, cy, gap, r=8):
    return dot(cx - gap, cy, r) + dot(cx + gap, cy, r)


def smile(cx, cy, w, depth=None, sw=6):
    depth = depth if depth is not None else w * 0.6
    return P(f"M{cx - w},{cy} Q{cx},{cy + depth} {cx + w},{cy}", extra=f'stroke-width="{sw}"')


def cheeks(cx, cy, gap, r=12):
    return NS(C(cx - gap, cy, r, PINK, 'opacity="0.7"') + C(cx + gap, cy, r, PINK, 'opacity="0.7"'))


def face(cx, cy, r):
    return (eyes(cx, cy - r * 0.05, r * 0.35, r * 0.09)
            + smile(cx, cy + r * 0.3, r * 0.3, r * 0.25)
            + cheeks(cx, cy + r * 0.22, r * 0.55, r * 0.12))


def svg(body, bg):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">'
        f'<rect width="512" height="512" rx="48" fill="{bg}"/>'
        f'<g stroke="{OUT}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round">'
        f"{body}</g></svg>"
    )


# ---------------------------------------------------------------- people
def person(head_y, head_r, sh_top, sh_bot, leg_bot, shirt, bottoms, kind,
           hair_back="", hair_front="", extra="", skin=SKIN, shoe=OUT):
    cx = 256
    half = head_r * 0.95
    s = ""
    s += shadow(256, leg_bot + 14, 110, 14)
    # legs
    lx1, lx2 = cx - 26, cx + 26
    leg_top = sh_bot - 20
    if kind == "pants":
        s += limb(f"M{lx1},{leg_top} L{lx1},{leg_bot - 10}", bottoms, 30)
        s += limb(f"M{lx2},{leg_top} L{lx2},{leg_bot - 10}", bottoms, 30)
    else:
        s += limb(f"M{lx1},{leg_top} L{lx1},{leg_bot - 10}", skin, 22)
        s += limb(f"M{lx2},{leg_top} L{lx2},{leg_bot - 10}", skin, 22)
    s += E(lx1 - 8, leg_bot, 26, 13, shoe) + E(lx2 + 8, leg_bot, 26, 13, shoe)
    if kind == "shorts":
        s += P(f"M{cx - 56},{sh_bot - 30} L{cx + 56},{sh_bot - 30} L{cx + 60},{sh_bot + 40} "
               f"L{cx + 4},{sh_bot + 40} L{cx},{sh_bot + 10} L{cx - 4},{sh_bot + 40} L{cx - 60},{sh_bot + 40} Z", bottoms)
    # arms
    s += limb(f"M{cx - 50},{sh_top + 22} L{cx - 86},{sh_bot - 10}", shirt, 26)
    s += limb(f"M{cx + 50},{sh_top + 22} L{cx + 86},{sh_bot - 10}", shirt, 26)
    s += C(cx - 88, sh_bot + 6, 15, skin) + C(cx + 88, sh_bot + 6, 15, skin)
    # torso
    if kind == "dress":
        s += P(f"M{cx - 48},{sh_top} L{cx + 48},{sh_top} L{cx + 86},{sh_bot + 30} "
               f"Q{cx},{sh_bot + 46} {cx - 86},{sh_bot + 30} Z", shirt)
    else:
        s += P(f"M{cx - 54},{sh_top + 10} Q{cx - 54},{sh_top} {cx - 40},{sh_top} L{cx + 40},{sh_top} "
               f"Q{cx + 54},{sh_top} {cx + 54},{sh_top + 10} L{cx + 50},{sh_bot} L{cx - 50},{sh_bot} Z", shirt)
    # neck + head
    s += hair_back
    s += R(cx - 14, head_y + head_r - 14, 28, sh_top - (head_y + head_r) + 20, skin)
    s += C(cx - half, head_y + 6, head_r * 0.2, skin) + C(cx + half, head_y + 6, head_r * 0.2, skin)
    s += C(cx, head_y, head_r, skin)
    s += face(cx, head_y + head_r * 0.12, head_r)
    s += hair_front
    s += extra
    return s


def boy():
    hy, hr = 150, 64
    hair = P(f"M{256 - hr},{hy + 4} Q{256 - hr},{hy - hr - 10} 256,{hy - hr} "
             f"Q{256 + hr + 6},{hy - hr - 6} {256 + hr},{hy + 4} Q{256 + 40},{hy - 34} 256,{hy - 30} "
             f"Q{256 - 30},{hy - 40} {256 - hr},{hy + 4} Z", HAIR)
    return person(hy, hr, 230, 330, 420, BLUE, NAVY, "shorts", hair_front=hair, shoe=RED)


def girl():
    hy, hr = 150, 64
    back = (C(176, 170, 34, BLONDE) + C(336, 170, 34, BLONDE)
            + C(196, 138, 12, RED) + C(316, 138, 12, RED))
    front = P(f"M{256 - hr - 2},{hy + 8} Q{256 - hr},{hy - hr - 10} 256,{hy - hr - 4} "
              f"Q{256 + hr},{hy - hr - 10} {256 + hr + 2},{hy + 8} Q{256 + 20},{hy - 50} 256,{hy - 34} "
              f"Q{256 - 20},{hy - 50} {256 - hr - 2},{hy + 8} Z", BLONDE)
    return person(hy, hr, 232, 330, 420, PINK, PINK, "dress", hair_back=back, hair_front=front, shoe=PURPLE)


def man():
    hy, hr = 120, 54
    hair = P(f"M{256 - hr},{hy} Q{256 - hr},{hy - hr - 8} 256,{hy - hr - 2} "
             f"Q{256 + hr},{hy - hr - 8} {256 + hr},{hy} L{256 + hr - 6},{hy - 20} "
             f"Q256,{hy - 34} {256 - hr + 6},{hy - 20} Z", OUT)
    tie = PL([(256, 192), (266, 204), (262, 270), (256, 282), (250, 270), (246, 204)], RED)
    collar = PL([(232, 188), (256, 206), (240, 220)], WHITE) + PL([(280, 188), (256, 206), (272, 220)], WHITE)
    beard = P(f"M{256 - 28},{hy + 34} Q256,{hy + 26} {256 + 28},{hy + 34}", extra='stroke-width="10"')
    return person(hy, hr, 188, 320, 440, "#4a6fa5", "#33415c", "pants",
                  hair_front=hair, extra=collar + tie + beard, shoe=DBROWN)


def woman():
    hy, hr = 124, 54
    back = P(f"M{256 - hr - 14},{hy + 10} Q{256 - hr - 20},{hy - hr - 20} 256,{hy - hr - 12} "
             f"Q{256 + hr + 20},{hy - hr - 20} {256 + hr + 14},{hy + 10} L{256 + hr + 18},{hy + 96} "
             f"Q256,{hy + 110} {256 - hr - 18},{hy + 96} Z", HAIR)
    front = P(f"M{256 - hr},{hy + 6} Q{256 - hr + 4},{hy - hr - 6} 256,{hy - hr - 2} "
              f"Q{256 + hr - 4},{hy - hr - 6} {256 + hr},{hy + 6} Q{256 + 24},{hy - 40} {256 - 10},{hy - 30} "
              f"Q{256 - 30},{hy - 20} {256 - hr},{hy + 6} Z", HAIR)
    necklace = P("M236,196 Q256,214 276,196", extra=f'stroke="{YELLOW}" stroke-width="6"')
    return person(hy, hr, 192, 320, 440, PURPLE, PURPLE, "dress",
                  hair_back=back, hair_front=front, extra=necklace, shoe=RED)


def baby():
    s = shadow(256, 440, 140, 16)
    # sitting body (onesie)
    s += E(256, 360, 110, 80, LBLUE)
    s += limb("M190,330 L150,380", LBLUE, 34) + limb("M322,330 L362,380", LBLUE, 34)
    s += C(146, 388, 20, SKIN) + C(366, 388, 20, SKIN)
    s += E(196, 428, 40, 22, LBLUE) + E(316, 428, 40, 22, LBLUE)
    # head
    s += C(170, 210, 20, SKIN) + C(342, 210, 20, SKIN)
    s += C(256, 200, 92, SKIN)
    s += P("M246,112 Q240,90 262,84 Q284,82 280,100", extra='stroke-width="7"')
    s += eyes(256, 196, 34, 9) + cheeks(256, 226, 56, 14)
    # pacifier
    s += E(256, 246, 24, 14, "#7ad1c9") + C(256, 246, 7, WHITE)
    return s


# ---------------------------------------------------------------- home
def house():
    s = shadow(256, 432, 170)
    s += R(318, 130, 38, 80, DRED)
    s += R(140, 236, 232, 192, CREAM)
    s += PL([(112, 250), (256, 116), (400, 250)], RED)
    s += R(232, 326, 52, 102, BROWN, 6) + dot(274, 380, 5)
    for x in (160, 300):
        s += R(x, 270, 52, 52, LBLUE, 4) + L(x + 26, 270, x + 26, 322, 6) + L(x, 296, x + 52, 296, 6)
    s += C(256, 200, 20, LBLUE)
    s += NS(R(80, 428, 352, 10, GREEN, 5))
    return s


def door():
    s = shadow(256, 444, 150)
    s += R(150, 68, 212, 372, CREAM, 10)
    s += R(170, 86, 172, 354, BROWN, 8)
    s += R(194, 112, 124, 120, "none", 6, f'stroke="{DBROWN}" stroke-width="6"')
    s += R(194, 262, 124, 150, "none", 6, f'stroke="{DBROWN}" stroke-width="6"')
    s += C(318, 250, 13, YELLOW)
    s += R(130, 430, 252, 16, GREY, 4)
    return s


def window():
    s = R(108, 80, 296, 330, WHITE, 10)
    s += R(126, 98, 260, 294, SKY, 4)
    s += NS(C(330, 150, 30, YELLOW) + E(190, 160, 44, 18, WHITE))
    s += L(256, 98, 256, 392, 12) + L(126, 245, 386, 245, 12)
    s += shine("M150,200 L190,140") + shine("M290,360 L330,300")
    # curtains
    s += P("M100,72 L170,72 Q140,220 172,410 L100,410 Z", RED)
    s += P("M412,72 L342,72 Q372,220 340,410 L412,410 Z", RED)
    s += R(90, 400, 332, 26, CREAM, 6)
    s += R(84, 60, 344, 16, BROWN, 8)
    return s


def bed():
    s = shadow(256, 420, 180)
    s += R(92, 170, 46, 250, BROWN, 12)
    s += R(380, 250, 40, 170, BROWN, 12)
    s += R(130, 284, 260, 66, WHITE, 10)
    s += R(118, 344, 290, 30, BROWN, 6)
    s += E(186, 270, 48, 26, WHITE)
    s += P("M228,262 L396,262 L396,344 L228,344 Q212,300 228,262 Z", BLUE)
    s += P("M250,262 L250,344", extra=f'stroke="{LBLUE}" stroke-width="6"')
    return s


def chair():
    s = shadow(256, 428, 120)
    s += R(176, 268, 22, 160, BROWN, 6) + R(314, 268, 22, 160, BROWN, 6)
    s += R(176, 100, 160, 140, BROWN, 18)
    s += R(196, 120, 120, 100, TAN, 10)
    s += R(160, 236, 192, 40, DBROWN, 10)
    s += R(176, 236, 22, 18, BROWN) + R(314, 236, 22, 18, BROWN)
    return s


def table():
    s = shadow(256, 436, 180)
    s += R(122, 250, 26, 180, BROWN, 6) + R(364, 250, 26, 180, BROWN, 6)
    s += R(150, 340, 212, 16, DBROWN, 4)
    s += R(92, 212, 328, 44, TAN, 10)
    s += R(92, 240, 328, 16, BROWN, 6)
    return s


def lamp():
    s = shadow(256, 432, 100)
    s += NS(PL([(180, 230), (332, 230), (400, 430), (112, 430)], "#fff4b8", 'opacity="0.6"'))
    s += E(256, 422, 80, 18, DGREY)
    s += R(246, 220, 20, 200, GREY, 6)
    s += PL([(196, 90), (316, 90), (356, 232), (156, 232)], YELLOW)
    s += L(180, 120, 332, 120, 5, ORANGE)
    s += R(240, 232, 32, 28, DGREY, 4)
    return s


# ---------------------------------------------------------------- transport
def wheel(cx, cy, r=40):
    return C(cx, cy, r, OUT) + C(cx, cy, r * 0.42, GREY)


def car():
    s = shadow(262, 382, 180)
    s += P("M84,340 L84,290 Q86,262 116,258 L170,252 L212,198 Q222,186 242,186 L328,186 "
           "Q348,186 360,200 L398,252 L414,254 Q442,260 442,290 L442,340 Z", RED)
    s += PL([(188, 250), (224, 204), (282, 204), (282, 250)], LBLUE)
    s += PL([(298, 204), (346, 204), (380, 250), (298, 250)], LBLUE)
    s += L(290, 260, 290, 330, 6) + L(310, 276, 330, 276, 6)
    s += C(428, 284, 10, YELLOW) + R(84, 280, 16, 18, "#ffb3b3", 3)
    s += wheel(160, 340) + wheel(368, 340)
    return s


def bus():
    s = shadow(256, 396, 190)
    s += R(64, 140, 384, 230, YELLOW, 26)
    s += R(64, 300, 384, 22, ORANGE)
    for x in (88, 160, 232):
        s += R(x, 168, 58, 66, LBLUE, 8)
    s += R(310, 168, 60, 130, LBLUE, 8) + L(340, 168, 340, 298, 6)
    s += R(388, 168, 44, 90, LBLUE, 8)
    s += C(432, 334, 10, WHITE) + R(64, 334, 14, 16, RED, 3)
    s += wheel(140, 372, 40) + wheel(372, 372, 40)
    return s


def bike():
    s = shadow(256, 420, 190)
    for cx in (148, 364):
        s += C(cx, 330, 82, "none", 'stroke-width="10"')
        for a in range(0, 180, 45):
            dx, dy = 70 * math.cos(math.radians(a)), 70 * math.sin(math.radians(a))
            s += L(cx - dx, 330 - dy, cx + dx, 330 + dy, 3, DGREY)
        s += C(cx, 330, 10, GREY)
    frame = "M148,330 L226,228 L252,330 Z M226,228 L340,228 L364,330 M252,330 L340,228"
    s += f'<path d="{frame}" fill="none" stroke="{OUT}" stroke-width="22"/>'
    s += f'<path d="{frame}" fill="none" stroke="{RED}" stroke-width="10"/>'
    s += L(226, 228, 220, 200, 10) + E(212, 196, 30, 10, OUT)
    s += L(340, 228, 330, 190, 10) + L(310, 186, 352, 186, 12)
    s += C(252, 330, 18, GREY) + L(252, 330, 270, 356, 8)
    return s


def boat():
    s = R(0, 360, 512, 152, LBLUE, 0, 'stroke="none"')
    s += P("M0,372 Q32,356 64,372 T128,372 T192,372 T256,372 T320,372 T384,372 T448,372 T512,372",
           extra=f'stroke="{BLUE}" stroke-width="6"')
    s += L(256, 96, 256, 330, 10)
    s += PL([(266, 104), (266, 310), (392, 310)], WHITE)
    s += PL([(246, 140), (246, 310), (138, 310)], CREAM)
    s += PL([(256, 96), (256, 72), (292, 84)], RED)
    s += P("M100,320 L412,320 L372,396 L142,396 Z", RED)
    s += R(118, 334, 278, 14, WHITE, 0, 'stroke="none"')
    s += P("M40,430 Q80,414 120,430 M360,450 Q400,434 440,450", extra=f'stroke="{BLUE}" stroke-width="6"')
    return s


def train():
    s = shadow(256, 412, 190)
    s += NS(C(150, 104, 22, "#e9ecef") + C(176, 78, 28, "#e9ecef") + C(214, 58, 32, "#e9ecef"))
    s += R(130, 136, 40, 90, OUT, 6) + R(120, 126, 60, 20, DGREY, 4)
    s += R(96, 222, 230, 126, GREEN, 16)
    s += R(300, 150, 120, 198, RED, 10) + R(290, 136, 140, 26, DRED, 6)
    s += R(322, 178, 76, 64, LBLUE, 8)
    s += PL([(96, 300), (96, 370), (56, 370)], GREY)
    s += C(96, 262, 14, YELLOW)
    s += R(80, 346, 350, 18, DGREY, 6)
    s += wheel(150, 374, 34) + wheel(236, 374, 34) + wheel(360, 370, 42)
    s += L(150, 374, 360, 370, 8)
    return s


def plane():
    s = NS(E(110, 120, 60, 22, WHITE) + E(400, 400, 70, 24, WHITE))
    s += PL([(240, 238), (310, 238), (262, 176), (226, 176)], "#7fa7c9")
    s += PL([(96, 246), (70, 150), (118, 150), (170, 246)], BLUE)
    s += P("M70,270 Q70,240 110,236 L380,236 Q446,240 458,266 Q446,292 380,294 L110,294 Q70,292 70,270 Z", WHITE)
    s += P("M404,240 Q438,246 452,262 L412,262 Z", NAVY)
    for x in range(150, 380, 34):
        s += C(x, 262, 9, LBLUE, 'stroke-width="5"')
    s += PL([(214, 272), (318, 272), (240, 388), (196, 388)], BLUE)
    s += PL([(76, 274), (140, 274), (96, 316), (70, 316)], "#7fa7c9")
    return s


# ---------------------------------------------------------------- animals
def dog():
    s = shadow(256, 444, 130)
    s += limb("M330,380 Q392,360 390,300", TAN, 22)
    s += E(256, 360, 92, 80, TAN)
    s += E(256, 370, 46, 56, CREAM, 'stroke="none"')
    s += E(214, 430, 32, 18, CREAM) + E(298, 430, 32, 18, CREAM)
    s += R(206, 266, 100, 20, RED, 10) + C(256, 292, 10, YELLOW)
    s += C(256, 196, 80, TAN)
    s += rot(18, 182, 196, E(182, 196, 28, 58, DBROWN))
    s += rot(-18, 330, 196, E(330, 196, 28, 58, DBROWN))
    s += E(256, 236, 46, 32, CREAM)
    s += P("M256,246 L256,258 M236,258 Q256,272 276,258")
    s += P("M246,262 Q246,290 256,290 Q266,290 266,262 Z", PINK, 'stroke-width="5"')
    s += E(256, 226, 17, 12, OUT)
    s += eyes(256, 184, 30, 10)
    return s


def cat():
    s = shadow(256, 444, 120)
    s += limb("M320,400 Q410,400 400,320 Q396,290 376,296", ORANGE, 22)
    s += E(256, 360, 84, 84, ORANGE)
    s += E(256, 378, 44, 54, CREAM, 'stroke="none"')
    s += E(220, 434, 28, 16, ORANGE) + E(292, 434, 28, 16, ORANGE)
    s += PL([(190, 170), (196, 96), (246, 140)], ORANGE) + PL([(322, 170), (316, 96), (266, 140)], ORANGE)
    s += NS(PL([(200, 152), (203, 116), (228, 140)], PINK) + PL([(312, 152), (309, 116), (284, 140)], PINK))
    s += C(256, 210, 76, ORANGE)
    s += P("M226,150 L232,172 M256,144 L256,168 M286,150 L280,172", extra=f'stroke="{DORANGE}" stroke-width="7"')
    s += E(226, 204, 9, 14, OUT, 'stroke="none"') + E(286, 204, 9, 14, OUT, 'stroke="none"')
    s += PL([(246, 230), (266, 230), (256, 242)], PINK, 'stroke-width="5"')
    s += P("M256,242 Q244,258 234,250 M256,242 Q268,258 278,250", extra='stroke-width="5"')
    s += P("M150,226 L216,236 M152,250 L216,246 M362,226 L296,236 M360,250 L296,246", extra='stroke-width="4"')
    return s


def bird():
    s = limb("M60,370 Q256,340 460,380", DBROWN, 18)
    s += NS(E(410, 350, 26, 12, GREEN) + E(110, 352, 24, 11, GREEN))
    s += PL([(140, 250), (64, 210), (78, 290)], BLUE)
    s += L(236, 330, 228, 368, 7) + L(272, 330, 270, 368, 7)
    s += E(256, 264, 112, 84, "#4ea8de")
    s += E(296, 286, 54, 40, CREAM, 'stroke="none"')
    s += P("M168,248 Q230,226 270,270 Q220,320 168,248 Z", BLUE)
    s += PL([(360, 230), (420, 246), (360, 262)], ORANGE)
    s += C(326, 226, 15, WHITE) + dot(330, 226, 8)
    return s


def fish():
    s = NS(C(420, 150, 14, WHITE, 'opacity=".8"') + C(446, 110, 9, WHITE, 'opacity=".8"') + C(430, 80, 6, WHITE, 'opacity=".8"'))
    s += C(420, 150, 14, "none", 'stroke-width="4"') + C(446, 110, 9, "none", 'stroke-width="4"')
    s += PL([(130, 260), (56, 186), (56, 334)], DORANGE)
    s += P("M220,190 Q250,130 300,176 Z", DORANGE)
    s += E(250, 260, 150, 94, ORANGE)
    s += P("M200,176 Q174,260 200,344", extra=f'stroke="{WHITE}" stroke-width="18"')
    s += P("M280,172 Q258,260 280,348", extra=f'stroke="{WHITE}" stroke-width="18"')
    s += P("M200,176 Q174,260 200,344 M280,172 Q258,260 280,348", extra='stroke-width="4" opacity=".4"')
    s += P("M240,290 Q260,320 230,330 Z", DORANGE)
    s += C(340, 236, 18, WHITE) + dot(344, 236, 10)
    s += P("M372,286 Q386,290 394,280", extra='stroke-width="6"')
    return s


def horse():
    s = shadow(250, 430, 160)
    s += limb("M126,246 Q86,300 104,380", DBROWN, 26)
    for x in (156, 192, 296, 330):
        s += R(x, 296, 26, 120, BROWN, 8) + R(x - 2, 404, 30, 20, OUT, 5)
    s += E(244, 268, 124, 62, BROWN)
    s += PL([(318, 250), (342, 144), (394, 148), (372, 280)], BROWN)
    s += rot(40, 402, 168, E(402, 168, 58, 30, BROWN))
    s += PL([(354, 128), (362, 94), (380, 128)], BROWN)
    s += limb("M340,140 Q326,196 316,248", DBROWN, 20)
    s += dot(380, 150, 7) + dot(430, 202, 5)
    return s


def cow():
    s = shadow(250, 432, 170)
    s += limb("M108,250 Q90,300 96,340", WHITE, 10) + C(96, 350, 12, OUT)
    for x in (130, 166, 290, 324):
        s += R(x, 300, 26, 116, WHITE, 8) + R(x - 2, 404, 30, 20, OUT, 5)
    s += E(196, 336, 22, 16, PINK)
    s += E(226, 274, 132, 70, WHITE)
    s += NS(E(186, 252, 34, 24, OUT) + E(270, 300, 30, 22, OUT) + E(138, 296, 20, 16, OUT) + E(296, 238, 18, 14, OUT))
    s += P("M340,166 Q330,136 346,124 M424,166 Q434,136 418,124", extra='stroke-width="10"')
    s += rot(-20, 326, 190, E(326, 190, 30, 14, WHITE)) + rot(20, 438, 190, E(438, 190, 30, 14, WHITE))
    s += E(382, 216, 56, 64, WHITE)
    s += NS(E(400, 190, 22, 18, OUT))
    s += E(382, 262, 46, 30, PINK)
    s += dot(366, 262, 6) + dot(398, 262, 6)
    s += eyes(382, 210, 22, 8)
    return s


# ---------------------------------------------------------------- food
def apple():
    s = shadow(256, 420, 120)
    s += P("M256,170 C200,130 118,160 118,262 C118,366 200,422 256,400 C312,422 394,366 394,262 C394,160 312,130 256,170 Z", RED)
    s += limb("M256,174 Q252,136 268,104", DBROWN, 12)
    s += P("M266,146 Q300,100 346,118 Q304,166 266,146 Z", GREEN)
    s += shine("M164,250 Q166,210 194,190")
    return s


def banana():
    s = shadow(270, 410, 150)
    s += P("M134,146 Q104,404 404,348 L408,326 Q196,330 166,148 Z", YELLOW)
    s += P("M150,180 Q150,330 330,340", extra=f'stroke="{ORANGE}" stroke-width="6"')
    s += R(132, 120, 34, 30, DBROWN, 6)
    s += P("M400,330 L420,340 L408,350 Z", DBROWN)
    return s


def bread():
    s = shadow(256, 410, 170)
    s += P("M104,300 Q104,166 256,166 Q408,166 408,300 L408,372 Q408,394 386,394 L126,394 Q104,394 104,372 Z", TAN)
    s += P("M104,300 Q104,166 256,166 Q408,166 408,300 Q256,318 104,300 Z", "#c08552")
    for x in (180, 250, 320):
        s += P(f"M{x - 20},{232} Q{x},{204} {x + 22},{214}", extra=f'stroke="{CREAM}" stroke-width="10"')
    return s


def egg():
    s = shadow(256, 420, 110)
    s += P("M256,104 C332,104 372,236 372,300 C372,372 320,412 256,412 C192,412 140,372 140,300 C140,236 180,104 256,104 Z", "#f6e3c4")
    s += shine("M190,250 Q196,190 226,150")
    s += NS(P("M330,300 C330,350 300,386 256,392 C310,370 330,340 330,300 Z", "#000", 'opacity=".08"'))
    return s


def milk():
    s = shadow(256, 430, 170)
    # carton
    s += PL([(130, 170), (210, 170), (240, 130), (160, 130)], "#e9ecef")
    s += PL([(130, 170), (210, 170), (210, 420), (130, 420)], WHITE)
    s += PL([(210, 170), (240, 130), (250, 150), (250, 410), (210, 420)], "#dee2e6")
    s += R(130, 250, 80, 90, BLUE, 0) + P("M170,268 Q190,300 170,320 Q150,300 170,268 Z", WHITE)
    # glass
    s += PL([(290, 220), (400, 220), (388, 420), (302, 420)], "#f8f9fa")
    s += NS(PL([(296, 250), (394, 250), (388, 416), (302, 416)], WHITE))
    s += PL([(290, 220), (400, 220), (388, 420), (302, 420)], "none")
    s += P("M296,250 L394,250", extra='stroke-width="5"')
    s += shine("M312,280 L318,390")
    return s


def water():
    s = shadow(290, 430, 120)
    s += P("M150,120 Q200,190 200,236 Q200,286 150,286 Q100,286 100,236 Q100,190 150,120 Z", "#4ea8de")
    s += shine("M122,236 Q122,212 138,194")
    s += PL([(220, 180), (380, 180), (360, 424), (240, 424)], "#eef7fb")
    s += NS(PL([(226, 240), (374, 240), (360, 420), (240, 420)], "#90cdf4"))
    s += PL([(220, 180), (380, 180), (360, 424), (240, 424)], "none")
    s += P("M226,240 Q263,226 300,240 T374,240", extra=f'stroke="{BLUE}" stroke-width="6"')
    s += shine("M250,260 L262,400")
    return s


def cake():
    s = shadow(256, 426, 180)
    s += E(256, 412, 170, 20, WHITE)
    s += R(110, 290, 292, 120, "#e9c46a", 14)
    s += R(150, 200, 212, 100, "#e9c46a", 14)
    drip = "M110,312 L110,300 Q110,290 124,290 L388,290 Q402,290 402,300 L402,312 Q382,340 362,312 Q342,340 322,312 Q302,340 282,312 Q262,340 242,312 Q222,340 202,312 Q182,340 162,312 Q142,340 122,312 Z"
    s += P(drip, PINK)
    s += P("M150,222 L150,210 Q150,200 164,200 L348,200 Q362,200 362,210 L362,222 Q344,246 326,222 Q308,246 290,222 Q272,246 256,222 Q238,246 220,222 Q202,246 184,222 Q166,246 150,222 Z", PINK)
    for x in (206, 256, 306):
        s += R(x - 8, 140, 16, 60, LBLUE, 4)
        s += P(f"M{x},{104} Q{x + 14},{124} {x},{136} Q{x - 14},{124} {x},{104} Z", ORANGE)
    s += NS(C(160, 360, 8, RED) + C(220, 370, 8, BLUE) + C(290, 360, 8, GREEN) + C(350, 372, 8, PURPLE))
    return s


# ---------------------------------------------------------------- nature
def sun():
    s = ""
    for i in range(12):
        s += rot(i * 30, 256, 256, PL([(240, 110), (272, 110), (256, 56)], ORANGE))
    s += C(256, 256, 130, YELLOW)
    s += shine("M170,230 Q180,180 220,160")
    return s


def moon():
    s = NS("".join(PL(star_pts(x, y, r, r * 0.45), "#fff4b8") for x, y, r in
                   [(120, 110, 18), (410, 140, 14), (390, 400, 20), (110, 390, 12), (440, 280, 10)]))
    s += P("M300,96 A170,170 0 1 0 420,340 A140,140 0 1 1 300,96 Z", "#fde68a")
    return s


def star():
    s = NS("".join(C(x, y, r, "#fff4b8") for x, y, r in [(90, 100, 4), (420, 90, 5), (440, 420, 4), (80, 400, 5), (300, 460, 3)]))
    s += PL(star_pts(256, 266, 180, 80), YELLOW)
    return s


def tree():
    s = shadow(256, 438, 160)
    s += P("M226,438 L232,300 L280,300 L286,438 Z", BROWN)
    s += P("M256,330 L210,290 M262,350 L304,300", extra='stroke-width="10"')
    s += merged(C(256, 160, 90) + C(170, 230, 74) + C(342, 230, 74) + C(256, 270, 80), GREEN)
    s += NS(C(200, 180, 10, RED) + C(320, 200, 10, RED) + C(260, 250, 10, RED) + C(180, 270, 10, RED) + C(350, 280, 10, RED))
    return s


def flower():
    s = NS(R(0, 410, 512, 102, LGREEN))
    s += limb("M256,260 Q246,350 256,440", GREEN, 14)
    s += P("M252,370 Q190,330 170,360 Q200,400 252,380 Z", GREEN)
    s += P("M260,330 Q320,290 344,320 Q312,360 260,342 Z", GREEN)
    for i in range(6):
        a = math.radians(i * 60 - 90)
        s += C(256 + 62 * math.cos(a), 190 + 62 * math.sin(a), 42, PINK)
    s += C(256, 190, 42, YELLOW)
    s += NS(C(244, 180, 6, ORANGE) + C(268, 186, 6, ORANGE) + C(254, 204, 6, ORANGE))
    return s


def cloud():
    s = NS(C(420, 110, 46, YELLOW))
    s += merged(C(170, 290, 70) + C(250, 230, 90) + C(340, 260, 74) + C(400, 310, 50) + R(120, 280, 320, 80, rx=40), WHITE)
    return s


# ---------------------------------------------------------------- things
def ball():
    s = shadow(256, 420, 120)
    s += C(256, 256, 146, RED)
    s += P("M256,110 Q170,256 256,402 Q342,256 256,110 Z", WHITE)
    s += P("M256,110 Q216,256 256,402 Q296,256 256,110 Z", YELLOW)
    s += P("M110,256 Q256,206 402,256", extra='stroke-width="6"')
    s += C(256, 256, 146, "none")
    s += shine("M160,190 Q180,150 216,134")
    return s


def book():
    s = shadow(256, 420, 170)
    s += P("M256,186 Q190,156 94,172 L94,392 Q190,372 256,402 Q322,372 418,392 L418,172 Q322,156 256,186 Z", BLUE)
    s += P("M256,172 Q190,142 110,158 L110,372 Q190,352 256,382 Z", WHITE)
    s += P("M256,172 Q322,142 402,158 L402,372 Q322,352 256,382 Z", "#fdfdfd")
    for i in range(5):
        y = 196 + i * 30
        s += P(f"M132,{y} Q190,{y - 14} 236,{y + 4}", extra=f'stroke="{GREY}" stroke-width="5"')
        s += P(f"M276,{y + 4} Q322,{y - 14} 380,{y}", extra=f'stroke="{GREY}" stroke-width="5"')
    s += R(300, 120, 20, 70, RED, 0)
    return s


def pen():
    s = shadow(256, 420, 130)
    p = (R(110, 234, 42, 44, NAVY, 10) + R(140, 232, 216, 48, BLUE, 10)
         + R(150, 216, 120, 18, GREY, 6) + R(340, 232, 26, 48, DGREY, 4)
         + PL([(366, 238), (414, 256), (366, 274)], CREAM) + PL([(404, 252), (420, 256), (404, 260)], OUT))
    s += rot(-35, 256, 256, p)
    return s


def phone():
    s = shadow(256, 432, 110)
    s += R(172, 84, 168, 340, OUT, 28)
    s += R(186, 120, 140, 262, SKY, 6)
    cols = [RED, GREEN, YELLOW, PURPLE, ORANGE, BLUE, PINK, DGREEN, DORANGE]
    for i, c in enumerate(cols):
        s += R(202 + (i % 3) * 40, 140 + (i // 3) * 44, 28, 28, c, 7, 'stroke="none"')
    s += R(236, 98, 40, 8, DGREY, 4, 'stroke="none"')
    s += C(256, 403, 11, DGREY, 'stroke="none"')
    return s


def cup():
    s = shadow(240, 420, 140)
    s += P("M180,100 Q160,80 180,60 M240,110 Q220,85 240,60 M300,100 Q280,80 300,60", extra=f'stroke="{GREY}" stroke-width="7"')
    s += ring(340, 280, 50, "#2a9d8f", 22)
    s += P("M150,170 L330,170 L318,380 Q316,410 286,410 L194,410 Q164,410 162,380 Z", "#2a9d8f")
    s += E(240, 170, 90, 22, "#7b4b2a")
    s += NS(C(240, 300, 32, WHITE, 'opacity=".9"'))
    s += P("M240,318 C200,290 216,270 240,286 C264,270 280,290 240,318 Z", RED, 'stroke="none"')
    return s


def key():
    s = shadow(256, 410, 140)
    k = (R(210, 238, 210, 30, BLONDE, 8) + R(340, 262, 22, 46, BLONDE, 4) + R(380, 262, 22, 34, BLONDE, 4)
         + C(160, 252, 72, BLONDE) + C(150, 252, 24, CREAM))
    s += rot(-20, 256, 256, k)
    return s


def bag():
    s = shadow(256, 424, 160)
    s += limb("M196,226 Q196,108 256,108 Q316,108 316,226", DBROWN, 16)
    s += P("M146,220 L366,220 L396,406 Q398,420 384,420 L128,420 Q114,420 116,406 Z", ORANGE)
    s += P("M146,220 L366,220 L360,290 Q256,320 152,290 Z", DORANGE)
    s += R(238, 286, 36, 30, YELLOW, 6)
    return s


def clock():
    s = C(256, 256, 170, RED)
    s += C(256, 256, 144, WHITE)
    for i in range(12):
        a = math.radians(i * 30)
        r1 = 116 if i % 3 else 104
        s += L(256 + r1 * math.sin(a), 256 - r1 * math.cos(a), 256 + 128 * math.sin(a), 256 - 128 * math.cos(a), 8 if i % 3 == 0 else 5)
    s += L(256, 256, 196, 210, 14) + L(256, 256, 334, 186, 10)
    s += L(256, 256, 256, 360, 4, RED)
    s += C(256, 256, 14, OUT)
    return s


# ---------------------------------------------------------------- clothes
def hat():
    s = shadow(256, 380, 190)
    s += E(256, 330, 196, 52, BLONDE)
    s += P("M146,328 Q146,160 256,160 Q366,160 366,328 Q256,350 146,328 Z", BLONDE)
    s += P("M150,284 Q256,300 362,284 L364,322 Q256,342 148,322 Z", RED)
    s += P("M200,190 Q200,220 230,230 M290,180 Q300,210 320,230", extra=f'stroke="{ORANGE}" stroke-width="5"')
    return s


def shoe():
    s = shadow(260, 396, 180)
    s += P("M92,340 L104,232 Q150,220 192,244 L250,276 Q316,254 364,284 Q432,304 430,350 L92,350 Z", RED)
    s += R(84, 340, 354, 40, WHITE, 18)
    s += P("M104,232 Q150,220 192,244 L200,300 Q150,310 100,290 Z", DRED)
    for i in range(4):
        x = 214 + i * 28
        s += L(x, 260 + i * 2, x + 14, 290 - i * 4, 6, WHITE)
    s += P("M350,300 Q390,312 410,340", extra=f'stroke="{WHITE}" stroke-width="8"')
    return s


def shirt():
    s = shadow(256, 436, 140)
    s += P("M192,110 L140,132 L84,204 L138,250 L170,218 L170,424 L342,424 L342,218 L374,250 L428,204 L372,132 L320,110 Q256,166 192,110 Z", GREEN)
    s += P("M192,110 Q256,166 320,110", extra='stroke-width="10"')
    s += P("M120,190 L156,226 M392,190 L356,226", extra=f'stroke="{DGREEN}" stroke-width="8"')
    s += PL(star_pts(256, 290, 46, 20), YELLOW)
    return s


# ---------------------------------------------------------------- body
def hand():
    s = R(192, 400, 136, 112, BLUE, 0)
    for x, top in ((174, 136), (220, 104), (266, 112), (312, 144)):
        s += R(x, top, 44, 200, SKIN, 22)
    s += rot(-38, 150, 320, R(128, 250, 46, 130, SKIN, 23))
    s += R(170, 240, 190, 186, SKIN, 64)
    s += P("M220,330 Q260,350 300,320", extra=f'stroke="{SKIN2}" stroke-width="6"')
    s += NS(R(178, 150, 30, 26, "#fde2e4", 12) + R(226, 118, 32, 26, "#fde2e4", 12) + R(272, 126, 32, 26, "#fde2e4", 12) + R(318, 158, 30, 26, "#fde2e4", 12))
    return s


def eye():
    s = P("M150,150 Q256,90 362,150", extra='stroke-width="18"')
    s += P("M76,276 Q256,116 436,276 Q256,436 76,276 Z", WHITE)
    s += C(256, 276, 86, "#3d8bd9")
    s += C(256, 276, 40, OUT)
    s += NS(C(282, 248, 16, WHITE) + C(232, 302, 7, WHITE))
    s += P("M76,276 Q256,116 436,276 Q256,436 76,276 Z", "none")
    for x1, y1, x2, y2 in ((140, 220, 120, 190), (196, 186, 186, 152), (256, 176, 256, 140), (316, 186, 326, 152), (372, 220, 392, 190)):
        s += L(x1, y1, x2, y2, 8)
    return s


# ---------------------------------------------------------------- A1 animals
def pig():
    s = shadow(256, 440, 140)
    for x in (186, 222, 290, 326):
        s += R(x - 14, 360, 28, 66, PINK, 8)
    s += E(256, 330, 140, 92, PINK)
    s += P("M396,300 Q430,290 420,310 Q410,330 432,320", extra='stroke-width="7"')
    s += PL([(192, 166), (190, 108), (236, 142)], PINK) + PL([(320, 166), (322, 108), (276, 142)], PINK)
    s += C(256, 222, 84, PINK)
    s += E(256, 250, 40, 28, "#f7b9cf")
    s += E(242, 250, 7, 11, OUT, 'stroke="none"') + E(270, 250, 7, 11, OUT, 'stroke="none"')
    s += eyes(256, 200, 34, 9)
    s += cheeks(256, 236, 60, 12)
    return s


def sheep():
    s = shadow(256, 440, 140)
    for x in (176, 216, 296, 336):
        s += R(x - 12, 340, 24, 90, OUT, 8)
    s += P(scallop(250, 290, 150, 96, 14), WHITE)
    s += P(scallop(250, 290, 100, 56, 10), "none", f'stroke="{GREY}" stroke-width="5"')
    s += rot(-30, 330, 200, E(330, 200, 30, 13, OUT))
    s += rot(30, 432, 200, E(432, 200, 30, 13, OUT))
    s += E(380, 230, 48, 64, "#3d405b")
    s += P(scallop(380, 170, 46, 24, 7), WHITE)
    s += C(362, 222, 9, WHITE, 'stroke="none"') + C(398, 222, 9, WHITE, 'stroke="none"')
    s += dot(364, 223, 5) + dot(400, 223, 5)
    return s


def duck():
    s = R(0, 360, 512, 152, LBLUE, 0, 'stroke="none"')
    s += P("M40,380 Q80,366 120,380 M380,400 Q420,386 460,400", extra=f'stroke="{BLUE}" stroke-width="6"')
    s += P("M100,300 Q90,250 130,240 L170,250 Q260,220 380,300 Q380,400 250,400 Q120,400 100,300 Z", YELLOW)
    s += P("M180,290 Q250,260 300,310 Q240,350 180,290 Z", "#f7c548")
    s += C(330, 200, 70, YELLOW)
    s += P("M390,206 Q450,200 452,222 Q420,240 386,232 Z", ORANGE)
    s += dot(340, 186, 10) + C(343, 183, 3, WHITE, 'stroke="none"')
    return s


def rabbit():
    s = shadow(256, 444, 130)
    s += C(352, 390, 26, WHITE)
    s += E(256, 360, 96, 84, "#d6d6d6")
    s += E(256, 380, 50, 50, WHITE, 'stroke="none"')
    s += E(214, 432, 34, 16, "#d6d6d6") + E(298, 432, 34, 16, "#d6d6d6")
    s += rot(-10, 216, 110, E(216, 110, 28, 84, "#d6d6d6")) + rot(10, 296, 110, E(296, 110, 28, 84, "#d6d6d6"))
    s += NS(rot(-10, 216, 116, E(216, 116, 12, 60, PINK)) + rot(10, 296, 116, E(296, 116, 12, 60, PINK)))
    s += C(256, 220, 72, "#d6d6d6")
    s += eyes(256, 206, 30, 9)
    s += PL([(246, 230), (266, 230), (256, 240)], PINK, 'stroke-width="5"')
    s += P("M256,240 L256,250 M240,256 Q256,262 256,250 Q256,262 272,256", extra='stroke-width="5"')
    s += R(246, 254, 20, 16, WHITE, 3, 'stroke-width="4"')
    s += cheeks(256, 238, 44, 11)
    return s


def elephant():
    s = shadow(240, 440, 170)
    for x in (130, 176, 270, 312):
        s += R(x, 300, 38, 128, "#9aa5b1", 12)
    s += limb("M92,260 Q70,300 80,330", "#9aa5b1", 10)
    s += E(220, 270, 134, 86, "#9aa5b1")
    s += limb("M392,220 Q430,300 404,370 Q396,392 420,396", "#9aa5b1", 40)
    s += C(360, 196, 72, "#9aa5b1")
    s += P("M330,130 Q250,130 250,210 Q250,290 330,276 Q300,210 330,130 Z", "#b8c2cc")
    s += P("M392,250 Q420,268 444,250", WHITE, 'stroke-width="6"')
    s += dot(384, 182, 9)
    return s


def lion():
    s = P(scallop(256, 250, 176, 176, 16), DORANGE)
    s += P(scallop(256, 250, 150, 150, 14, 0.2), ORANGE, f'stroke="{DORANGE}" stroke-width="4"')
    s += C(170, 150, 30, YELLOW) + C(342, 150, 30, YELLOW)
    s += NS(C(170, 150, 14, ORANGE) + C(342, 150, 14, ORANGE))
    s += C(256, 256, 116, YELLOW)
    s += E(256, 306, 54, 40, CREAM)
    s += P("M234,276 L278,276 L256,300 Z", DBROWN)
    s += P("M256,300 L256,316 M232,326 Q256,338 256,316 Q256,338 280,326", extra='stroke-width="6"')
    s += eyes(256, 236, 46, 11)
    s += P("M196,212 L226,220 M316,212 L286,220", extra='stroke-width="6"')
    return s


def frog():
    s = R(0, 380, 512, 132, LBLUE, 0, 'stroke="none"')
    s += P("M100,420 A170,46 0 1 0 420,420 L260,420 Z", DGREEN)
    s += E(160, 400, 60, 26, GREEN) + E(352, 400, 60, 26, GREEN)
    s += E(256, 320, 130, 104, GREEN)
    s += E(256, 350, 80, 64, LGREEN, 'stroke="none"')
    s += C(196, 200, 48, GREEN) + C(316, 200, 48, GREEN)
    s += C(196, 196, 28, WHITE) + C(316, 196, 28, WHITE)
    s += dot(200, 198, 14) + dot(312, 198, 14)
    s += P("M186,280 Q256,330 326,280", extra='stroke-width="9"')
    s += cheeks(256, 282, 96, 14)
    s += E(196, 410, 40, 18, GREEN) + E(316, 410, 40, 18, GREEN)
    return s


def butterfly():
    s = limb("M250,154 Q220,90 190,80", OUT, 1) + limb("M262,154 Q292,90 322,80", OUT, 1)
    s += C(190, 80, 10, OUT) + C(322, 80, 10, OUT)
    for flip in (1, -1):
        g = (P("M256,240 Q170,90 90,140 Q50,240 256,260 Z", PURPLE)
             + P("M256,262 Q100,270 120,370 Q180,420 256,280 Z", PINK)
             + C(150, 180, 22, YELLOW) + C(170, 330, 16, YELLOW))
        s += g if flip == 1 else f'<g transform="translate(512 0) scale(-1 1)">{g}</g>'
    s += E(256, 260, 16, 100, OUT)
    s += C(256, 156, 20, OUT)
    return s


# ---------------------------------------------------------------- A1 food
def orange():
    s = shadow(256, 420, 150)
    s += C(200, 270, 130, ORANGE)
    s += NS("".join(C(200 + dx, 270 + dy, 4, DORANGE) for dx, dy in [(-60, -40), (-20, 30), (40, -60), (60, 40), (-50, 70), (10, -10), (80, -10)]))
    s += P("M200,140 Q210,110 196,92", extra='stroke-width="8"')
    s += P("M204,124 Q250,80 290,104 Q246,146 204,124 Z", GREEN)
    s += C(368, 340, 82, ORANGE) + C(368, 340, 66, "#ffd6a5", 'stroke-width="5"')
    for i in range(8):
        a = math.radians(i * 45)
        s += L(368, 340, 368 + 62 * math.cos(a), 340 + 62 * math.sin(a), 5, CREAM)
    s += shine("M118,240 Q124,200 150,180")
    return s


def carrot():
    s = shadow(256, 430, 130)
    s += P("M246,150 Q200,70 160,80 Q200,120 230,160 Z", GREEN)
    s += P("M256,150 Q260,60 300,50 Q290,110 270,160 Z", DGREEN)
    s += P("M266,156 Q330,90 360,110 Q320,150 280,170 Z", GREEN)
    s += P("M190,170 Q256,140 322,170 Q300,300 262,430 Q256,440 250,430 Q212,300 190,170 Z", ORANGE)
    for y, x1, x2 in ((210, 200, 240), (260, 280, 304), (310, 230, 256), (360, 262, 280)):
        s += L(x1, y, x2, y + 6, 6, DORANGE)
    return s


def tomato():
    s = shadow(256, 420, 150)
    s += P("M256,170 C150,150 96,220 100,290 C104,370 180,410 256,408 C332,410 408,370 412,290 C416,220 362,150 256,170 Z", RED)
    s += PL(star_pts(256, 172, 70, 24, 5), GREEN)
    s += limb("M256,170 Q252,140 266,122", DGREEN, 10)
    s += shine("M150,260 Q160,214 196,196")
    return s


def cheese():
    s = shadow(256, 410, 180)
    s += PL([(90, 260), (396, 156), (430, 250), (90, 260)], "#fde68a")
    s += PL([(90, 260), (430, 250), (430, 380), (90, 390)], YELLOW)
    s += NS(E(170, 310, 24, 18, "#f5b942") + E(260, 340, 32, 24, "#f5b942") + E(360, 300, 20, 16, "#f5b942") + E(380, 356, 16, 12, "#f5b942")
            + E(260, 216, 20, 8, "#f5b942") + E(340, 196, 16, 6, "#f5b942"))
    return s


def pizza():
    s = shadow(256, 430, 190)
    s += C(256, 256, 180, "#e0a458")
    s += C(256, 256, 150, "#f6d365", 'stroke-width="6"')
    s += NS("".join(C(256 + r * math.cos(math.radians(a)), 256 + r * math.sin(math.radians(a)), 22, RED)
                    for r, a in [(90, 20), (90, 140), (90, 260), (50, 80), (50, 200), (50, 320), (110, 80), (110, 200), (110, 320)]))
    s += NS("".join(E(256 + 70 * math.cos(math.radians(a)), 256 + 70 * math.sin(math.radians(a)), 10, 6, GREEN) for a in (50, 170, 290)))
    for a in range(0, 360, 60):
        s += L(256, 256, 256 + 150 * math.cos(math.radians(a)), 256 + 150 * math.sin(math.radians(a)), 5)
    return s


def ice_cream():
    s = PL([(176, 250), (336, 250), (256, 460)], "#e0a458")
    s += P("M200,300 L300,300 M214,350 L290,350 M190,270 L296,390 M322,270 L230,400", extra=f'stroke="{DBROWN}" stroke-width="5"')
    s += C(256, 170, 76, CREAM)
    s += P(scallop(256, 240, 96, 30, 9), PINK)
    s += P("M168,236 Q170,170 210,150 Q256,130 300,150 Q344,170 344,236 Z", PINK)
    s += C(256, 92, 22, RED) + P("M256,72 Q262,50 280,44", extra='stroke-width="6"')
    s += shine("M200,200 Q206,174 226,164")
    return s


def grapes():
    s = shadow(256, 450, 110)
    s += limb("M256,120 Q250,90 270,70", DBROWN, 12)
    s += P("M266,108 Q330,60 380,90 Q340,140 266,108 Z", GREEN)
    rows = [(4, 150), (4, 210), (3, 270), (2, 330), (1, 390)]
    for n, y in rows:
        for i in range(n):
            x = 256 + (i - (n - 1) / 2) * 60
            s += C(x, y, 34, PURPLE)
            s += NS(C(x - 10, y - 12, 7, WHITE, 'opacity=".5"'))
    return s


def strawberry():
    s = shadow(256, 440, 120)
    s += P("M256,420 C170,380 110,280 120,210 C128,150 200,140 256,160 C312,140 384,150 392,210 C402,280 342,380 256,420 Z", RED)
    s += NS("".join(E(x, y, 5, 8, YELLOW) for x, y in [(180, 220), (230, 210), (290, 214), (340, 222), (200, 280), (256, 270), (316, 280), (230, 340), (286, 340), (256, 390)]))
    s += PL(star_pts(256, 160, 80, 28, 6), GREEN)
    s += limb("M256,150 Q252,116 266,100", DGREEN, 10)
    return s


# ---------------------------------------------------------------- A1 home / things
def sofa():
    s = shadow(256, 420, 190)
    s += R(120, 396, 20, 30, DBROWN, 4) + R(372, 396, 20, 30, DBROWN, 4)
    s += R(110, 150, 292, 150, "#e76f51", 30)
    s += R(150, 270, 106, 64, "#f08a6c", 14) + R(256, 270, 106, 64, "#f08a6c", 14)
    s += R(70, 220, 70, 180, "#e76f51", 30) + R(372, 220, 70, 180, "#e76f51", 30)
    s += R(118, 330, 276, 70, "#e76f51", 10)
    s += R(180, 180, 70, 60, YELLOW, 16)
    return s


def television():
    s = shadow(256, 430, 140)
    s += P("M200,380 L312,380 L340,420 L172,420 Z", DGREY)
    s += R(240, 350, 32, 40, DGREY)
    s += R(70, 100, 372, 260, OUT, 22)
    s += R(92, 120, 328, 216, SKY, 6)
    s += NS(PL([(92, 336), (190, 230), (260, 300), (320, 240), (420, 336)], GREEN) + C(360, 170, 26, YELLOW))
    return s


def computer():
    s = shadow(256, 430, 200)
    s += R(132, 92, 248, 196, DGREY, 16)
    s += R(150, 110, 212, 160, SKY, 4)
    s += NS(R(170, 130, 80, 50, WHITE, 4) + R(262, 130, 80, 20, BLUE, 4) + R(262, 160, 80, 20, GREEN, 4) + R(170, 196, 172, 54, WHITE, 4))
    s += P("M112,288 L400,288 L452,384 Q456,400 440,400 L72,400 Q56,400 60,384 Z", GREY)
    for r in range(3):
        for c in range(9):
            s += R(130 + c * 28 + r * 6, 302 + r * 22, 20, 14, "#e9ecef", 3, 'stroke-width="3"')
    s += R(220, 368, 72, 22, "#e9ecef", 4, 'stroke-width="4"')
    return s


def umbrella():
    s = limb("M256,160 L256,390 Q256,430 222,430 Q194,430 194,404", DBROWN, 12)
    s += P("M70,250 Q70,90 256,86 Q442,90 442,250 Q410,226 380,250 Q350,226 318,250 Q288,226 256,250 Q224,226 194,250 Q162,226 132,250 Q102,226 70,250 Z", RED)
    s += P("M256,86 Q194,140 194,250 Z", YELLOW) + P("M256,86 Q318,140 318,250 Z", YELLOW)
    s += P("M256,86 Q194,140 194,250 M256,86 Q318,140 318,250 M256,86 Q140,120 132,250 M256,86 Q372,120 380,250", extra='stroke-width="6"')
    s += C(256, 80, 10, OUT)
    s += NS("".join(P(f"M{x},{y} Q{x + 6},{y + 14} {x},{y + 18} Q{x - 6},{y + 14} {x},{y} Z", "#4ea8de") for x, y in [(110, 300), (400, 320), (140, 380), (360, 400), (90, 440)]))
    return s


def glasses():
    s = P("M100,230 L50,200 L44,240", extra='stroke-width="12"') + P("M412,230 L462,200 L468,240", extra='stroke-width="12"')
    s += P("M210,250 Q256,220 302,250", extra='stroke-width="14"')
    s += C(152, 262, 74, "#d6efff", 'stroke-width="16"') + C(360, 262, 74, "#d6efff", 'stroke-width="16"')
    s += shine("M118,240 L150,206") + shine("M326,240 L358,206")
    return s


def plate():
    s = shadow(256, 420, 180, 20)
    s += C(256, 256, 172, WHITE)
    s += C(256, 256, 118, "#f8f9fa", f'stroke="{GREY}" stroke-width="6"')
    s += P("M196,180 Q230,160 270,164", extra=f'stroke="{LBLUE}" stroke-width="10"')
    s += C(256, 256, 172, "none", f'stroke="{LBLUE}" stroke-width="4" stroke-dasharray="2 18"')
    return s


def spoon():
    s = shadow(256, 430, 110)
    sp = R(242, 220, 28, 230, GREY, 14) + E(256, 156, 64, 92, GREY) + E(256, 156, 44, 70, "#ced4da", 'stroke="none"')
    s += rot(30, 256, 280, sp)
    s += shine("M238,110 Q230,140 236,170")
    return s


def fork():
    s = shadow(256, 440, 110)
    f = (R(242, 240, 28, 210, GREY, 14)
         + P("M184,80 L184,190 Q184,250 256,250 Q328,250 328,190 L328,80", GREY)
         + R(184, 64, 22, 130, GREY, 10) + R(226, 64, 22, 130, GREY, 10)
         + R(266, 64, 22, 130, GREY, 10) + R(306, 64, 22, 130, GREY, 10)
         + R(186, 150, 140, 60, GREY, 0, 'stroke="none"'))
    s += rot(-25, 256, 280, f)
    return s


def bottle():
    s = shadow(256, 444, 110)
    s += R(226, 56, 60, 46, RED, 8)
    s += P("M236,100 L276,100 L276,150 Q346,190 346,250 L346,410 Q346,440 316,440 L196,440 Q166,440 166,410 L166,250 Q166,190 236,150 Z", "#74c69d")
    s += R(166, 270, 180, 100, CREAM)
    s += NS(PL(star_pts(256, 320, 30, 14), RED))
    s += shine("M196,240 L196,260 M196,390 L196,410")
    return s


def dress():
    s = shadow(256, 444, 150)
    s += P("M200,80 L210,150 M312,80 L302,150", extra='stroke-width="12"')
    s += P("M200,140 Q256,170 312,140 L322,240 L412,420 Q256,450 100,420 L190,240 Z", RED)
    s += P("M190,240 Q256,262 322,240", extra='stroke-width="10"')
    s += NS("".join(C(x, y, 9, WHITE) for x, y in [(160, 380), (220, 330), (256, 400), (300, 320), (350, 380), (236, 200), (280, 210)]))
    return s


def sock():
    s = shadow(240, 440, 130)
    s += P("M206,70 L326,70 L326,300 Q326,330 350,350 L400,384 Q430,410 404,436 Q384,452 350,436 L210,360 Q180,340 190,300 L206,250 Z", WHITE)
    s += R(206, 70, 120, 40, BLUE)
    s += NS(R(206, 150, 120, 26, BLUE) + R(206, 210, 120, 26, BLUE))
    s += P("M206,70 L326,70 L326,300 Q326,330 350,350 L400,384 Q430,410 404,436 Q384,452 350,436 L210,360 Q180,340 190,300 L206,250 Z")
    s += P("M350,350 Q350,390 400,384 Q430,410 404,436 Q384,452 350,436 Z", RED)
    s += P("M190,300 Q230,280 236,330 L210,360 Q180,340 190,300 Z", RED)
    return s


def trousers():
    s = shadow(256, 450, 140)
    s += P("M160,80 L352,80 L384,436 L284,436 L256,190 L228,436 L128,436 Z", "#3a6ea5")
    s += R(156, 70, 200, 40, "#2c5282")
    s += R(240, 76, 32, 28, BLONDE, 4, 'stroke-width="5"')
    s += P("M256,110 L256,180 M176,110 Q200,150 230,110 M336,110 Q312,150 282,110", extra=f'stroke="{YELLOW}" stroke-width="5" stroke-dasharray="10 8"')
    s += P("M140,410 L224,410 M288,410 L372,410", extra=f'stroke="{YELLOW}" stroke-width="5" stroke-dasharray="10 8"')
    return s


def scarf():
    s = shadow(256, 450, 120)
    s += rot(8, 216, 320, R(186, 200, 64, 220, RED, 10))
    s += rot(-6, 300, 300, R(270, 190, 64, 190, RED, 10))
    for x, y, a in ((216, 400, 8), (300, 370, -6)):
        s += rot(a, x, y, P(f"M{x - 28},{y} L{x + 28},{y}", extra=f'stroke="{WHITE}" stroke-width="14"') +
                 P(f"M{x - 28},{y - 40} L{x + 28},{y - 40}", extra=f'stroke="{WHITE}" stroke-width="14"'))
    s += rot(8, 216, 320, "".join(L(x, 420, x - 2, 444, 6) for x in (194, 210, 226, 242)))
    s += rot(-6, 300, 300, "".join(L(x, 380, x + 2, 404, 6) for x in (278, 294, 310, 326)))
    s += P("M140,150 Q256,240 372,150 L372,200 Q256,290 140,200 Z", RED)
    s += P("M150,166 Q256,252 362,166", extra=f'stroke="{WHITE}" stroke-width="10"')
    return s


# ---------------------------------------------------------------- A1 nature
def mountain():
    s = NS(R(0, 0, 512, 512, SKY, 48)) + NS(C(410, 110, 40, YELLOW))
    s += PL([(-10, 440), (150, 220), (300, 440)], "#7d8597")
    s += PL([(120, 440), (300, 110), (500, 440)], "#5c677d")
    s += PL([(300, 110), (250, 200), (276, 186), (300, 210), (326, 186), (352, 200)], WHITE)
    s += PL([(150, 220), (118, 264), (140, 256), (160, 270), (182, 262)], WHITE)
    s += NS(R(0, 430, 512, 82, GREEN))
    return s


def sea():
    s = NS(C(380, 140, 50, YELLOW))
    s += P("M150,120 L170,136 L190,120 M210,90 L226,104 L242,90", extra='stroke-width="6"')
    cols = ["#90e0ef", "#48cae4", "#0096c7", "#0077b6"]
    for i, c in enumerate(cols):
        y = 240 + i * 60
        d = f"M-20,{y} " + " ".join(f"Q{x + 32},{y - 30} {x + 64},{y}" for x in range(-20, 532, 64)) + f" L540,540 L-20,540 Z"
        s += P(d, c)
    return s


def cloud_shape(cx, cy, scale, fill):
    return tr(cx, cy, merged(C(-80, 20, 56) + C(0, -20, 76) + C(80, 10, 60) + R(-130, 10, 260, 70, rx=35), fill), scale)


def rain():
    s = cloud_shape(256, 170, 1.1, "#ced4da")
    for x, y in [(150, 300), (220, 330), (290, 300), (360, 330), (180, 400), (260, 420), (340, 400), (120, 380), (400, 410)]:
        s += P(f"M{x},{y - 10} Q{x + 22},{y + 26} {x},{y + 40} Q{x - 22},{y + 26} {x},{y - 10} Z", "#4ea8de", 'stroke-width="5"')
    return s


def flake(cx, cy, r, w=8, color=WHITE):
    s = ""
    for i in range(6):
        a = math.radians(i * 60)
        s += L(cx, cy, cx + r * math.cos(a), cy + r * math.sin(a), w, color)
        mx, my = cx + r * 0.6 * math.cos(a), cy + r * 0.6 * math.sin(a)
        for da in (-45, 45):
            b = a + math.radians(da)
            s += L(mx, my, mx + r * 0.3 * math.cos(b), my + r * 0.3 * math.sin(b), w, color)
    return s


def snow():
    s = NS(R(0, 0, 512, 512, "#bde0fe", 48))
    s += P("M-10,400 Q130,350 260,390 Q390,430 520,380 L520,520 L-10,520 Z", WHITE)
    for x, y, r, w in ((256, 210, 110, 10), (100, 110, 34, 6), (410, 120, 40, 6), (90, 300, 28, 5), (420, 300, 30, 5)):
        s += flake(x, y, r, w + 10, BLUE) + flake(x, y, r, w, WHITE)
    return s


def rainbow():
    cols = [RED, ORANGE, YELLOW, GREEN, "#4ea8de", PURPLE]
    s = f'<path d="M66,360 A190,190 0 0 1 446,360" fill="none" stroke="{OUT}" stroke-width="{len(cols) * 22 + 16}"/>'
    for i, c in enumerate(cols):
        r = 190 + (2.5 - i) * 22
        s += f'<path d="M{256 - r},360 A{r},{r} 0 0 1 {256 + r},360" fill="none" stroke="{c}" stroke-width="22"/>'
    s += cloud_shape(80, 360, 0.7, WHITE) + cloud_shape(432, 360, 0.7, WHITE)
    return s


def leaf():
    s = limb("M150,400 Q120,440 100,450", DGREEN, 12)
    s += P("M150,400 C110,280 170,120 410,90 C420,300 300,420 150,400 Z", GREEN)
    s += P("M150,400 Q260,260 400,100", extra=f'stroke="{DGREEN}" stroke-width="8"')
    for t in (0.3, 0.5, 0.7):
        x, y = 150 + t * 250, 400 - t * 300
        s += P(f"M{x},{y} L{x - 50},{y - 70}", extra=f'stroke="{DGREEN}" stroke-width="5"')
        s += P(f"M{x},{y} L{x + 70},{y + 30}", extra=f'stroke="{DGREEN}" stroke-width="5"')
    return s


def fire():
    s = shadow(256, 440, 170)
    s += P("M256,60 C300,140 380,170 370,280 C362,370 300,410 256,410 C212,410 150,370 142,280 C136,200 200,190 196,120 C230,150 236,190 256,200 C270,160 250,110 256,60 Z", DORANGE)
    s += P("M256,180 C290,230 330,260 320,320 C312,380 280,400 256,400 C232,400 196,380 192,330 C188,280 230,260 230,220 C246,240 250,250 256,256 C262,230 256,200 256,180 Z", ORANGE)
    s += P("M256,290 C280,320 290,340 286,364 C282,390 270,398 256,398 C242,398 228,390 226,366 C224,340 246,320 256,290 Z", YELLOW)
    s += rot(-14, 256, 410, R(110, 392, 292, 40, BROWN, 18)) + rot(14, 256, 410, R(110, 392, 292, 40, DBROWN, 18))
    return s


# ---------------------------------------------------------------- A1 transport
def truck():
    s = shadow(256, 400, 200)
    s += R(60, 140, 250, 200, "#2a9d8f", 10)
    s += P("M310,190 L390,190 Q410,190 420,210 L452,270 L452,340 L310,340 Z", RED)
    s += PL([(330, 206), (386, 206), (420, 266), (330, 266)], LBLUE)
    s += R(60, 330, 392, 22, DGREY, 6)
    s += C(446, 300, 9, YELLOW)
    s += wheel(130, 360, 38) + wheel(220, 360, 38) + wheel(380, 360, 38)
    return s


def helicopter():
    s = L(80, 120, 440, 120, 14) + R(244, 120, 24, 50, DGREY)
    s += L(180, 380, 160, 400, 8) + L(320, 380, 340, 400, 8) + L(120, 404, 380, 404, 12)
    s += limb("M150,260 L50,230", YELLOW, 30)
    s += P("M54,190 L70,270", extra='stroke-width="12"')
    s += E(270, 264, 130, 100, YELLOW)
    s += P("M290,180 Q390,180 396,270 L290,270 Z", LBLUE)
    s += L(220, 362, 210, 384, 8) + L(320, 362, 330, 384, 8)
    s += R(170, 290, 90, 14, ORANGE, 6, 'stroke="none"')
    return s


def motorbike():
    s = shadow(256, 418, 200)
    for cx in (140, 380):
        s += C(cx, 350, 64, OUT) + C(cx, 350, 34, GREY)
    s += L(380, 350, 330, 190, 14) + L(310, 180, 350, 186, 14)
    s += P("M150,300 L210,260 L330,250 L360,300 L250,330 Z", DGREY)
    s += P("M190,250 Q240,200 320,220 L330,256 L200,270 Z", RED)
    s += P("M120,244 Q160,224 220,240 L216,262 L130,266 Z", OUT)
    s += R(200, 300, 80, 50, GREY, 10)
    s += limb("M150,340 L250,346", DGREY, 10)
    s += C(362, 220, 18, YELLOW)
    return s


# ---------------------------------------------------------------- A1 body (face based)
def big_face(target):
    s = ""
    ear_r = 50 if target == "ear" else 30
    s += C(108, 270, ear_r, SKIN) + C(404, 270, ear_r, SKIN)
    s += P("M100,260 Q108,240 118,270" if target == "ear" else "", extra=f'stroke="{SKIN2}" stroke-width="6"')
    s += C(256, 270, 150, SKIN)
    s += P("M106,240 Q100,110 256,104 Q412,110 406,240 Q370,160 256,170 Q160,170 106,240 Z", HAIR)
    s += eyes(256, 250, 58, 12)
    if target == "nose":
        s += P("M256,236 L222,316 Q256,340 290,316 Z", "#f0b48a", 'stroke-width="8"')
    else:
        s += P("M256,262 L244,300 Q256,306 268,300", extra='stroke-width="6"')
    if target == "mouth":
        s += P("M190,334 Q256,320 322,334 Q256,410 190,334 Z", RED, 'stroke-width="8"')
        s += P("M210,340 L302,340 L296,352 L216,352 Z", WHITE, 'stroke="none"')
    else:
        s += smile(256, 338, 36, 20)
    s += cheeks(256, 310, 92, 18)
    pos = {"nose": (256, 290, 64), "mouth": (256, 352, 84), "ear": (404, 270, 74)}[target]
    s += C(*pos, "none", f'stroke="{RED}" stroke-width="8" stroke-dasharray="18 12"')
    return s


def nose():
    return big_face("nose")


def mouth():
    return big_face("mouth")


def ear():
    return big_face("ear")


def foot():
    s = shadow(256, 450, 110)
    s += P("M200,170 Q190,120 236,120 L330,130 Q366,140 360,200 L346,330 Q340,440 270,440 Q196,440 196,360 Q200,260 200,170 Z", SKIN)
    for x, y, r in ((228, 104, 30), (282, 100, 22), (318, 108, 18), (346, 122, 15), (366, 142, 13)):
        s += C(x, y, r, SKIN)
    s += NS("".join(E(x, y - r * 0.3, r * 0.5, r * 0.4, "#fde2e4") for x, y, r in ((228, 104, 30), (282, 100, 22), (318, 108, 18))))
    s += P("M250,380 Q280,390 300,374", extra=f'stroke="{SKIN2}" stroke-width="6"')
    return s


def tooth():
    s = shadow(256, 440, 110)
    s += P("M140,170 Q140,90 210,96 Q240,100 256,116 Q272,100 302,96 Q372,90 372,170 Q372,250 344,320 Q330,420 300,420 Q276,420 268,350 Q262,320 256,320 Q250,320 244,350 Q236,420 212,420 Q182,420 168,320 Q140,250 140,170 Z", WHITE)
    s += eyes(256, 200, 44, 11) + smile(256, 236, 30, 22) + cheeks(256, 228, 74, 14)
    s += shine("M170,150 Q176,120 200,114")
    for x, y in ((404, 120), (110, 300), (420, 300)):
        s += PL(star_pts(x, y, 20, 8, 4), YELLOW, 'stroke-width="5"')
    return s


# ---------------------------------------------------------------- A1 school / things
def pencil():
    s = shadow(256, 420, 140)
    p = (R(96, 234, 40, 44, PINK, 10) + R(130, 230, 40, 52, GREY, 2)
         + R(166, 230, 190, 52, YELLOW, 0) + L(166, 256, 356, 256, 5, "#e9b949")
         + PL([(356, 230), (420, 256), (356, 282)], "#f1d1a6") + PL([(400, 248), (424, 256), (400, 264)], OUT))
    s += rot(-35, 256, 256, p)
    return s


def scissors():
    s = PL([(196, 330), (376, 92), (396, 110), (228, 342)], "#ced4da")
    s += PL([(316, 330), (136, 92), (116, 110), (284, 342)], "#ced4da")
    s += C(256, 254, 12, DGREY)
    s += ring(186, 380, 44, RED, 22) + ring(326, 380, 44, RED, 22)
    return s


def guitar():
    g = (R(240, 40, 32, 230, DBROWN, 4) + R(230, 20, 52, 60, OUT, 10)
         + "".join(C(x, y, 6, GREY) for x in (222, 290) for y in (34, 52, 70))
         + merged(C(256, 300, 74) + C(256, 400, 96), ORANGE)
         + C(256, 320, 28, OUT) + R(224, 410, 64, 16, DBROWN, 4)
         + "".join(L(248 + i * 5, 60, 248 + i * 5, 416, 2, "#eee") for i in range(4)))
    return shadow(256, 470, 110) + rot(30, 256, 256, tr(0, -10, g))


def kite():
    s = P("M256,330 Q220,380 270,410 Q320,440 280,490", extra='stroke-width="5"')
    for x, y in ((236, 374), (284, 446)):
        s += PL([(x - 20, y - 14), (x, y), (x - 20, y + 14)], RED, 'stroke-width="5"') + PL([(x + 20, y - 14), (x, y), (x + 20, y + 14)], YELLOW, 'stroke-width="5"')
    s += PL([(256, 60), (380, 190), (256, 330), (132, 190)], "none")
    s += NS(PL([(256, 60), (380, 190), (256, 190)], RED) + PL([(256, 60), (132, 190), (256, 190)], YELLOW)
            + PL([(132, 190), (256, 330), (256, 190)], BLUE) + PL([(380, 190), (256, 330), (256, 190)], GREEN))
    s += PL([(256, 60), (380, 190), (256, 330), (132, 190)], "none")
    s += L(256, 60, 256, 330, 6) + L(132, 190, 380, 190, 6)
    s += P("M380,190 Q440,300 470,480", extra='stroke-width="3"')
    return s


def gift():
    s = shadow(256, 436, 170)
    s += P("M256,170 Q190,80 160,120 Q150,160 256,170 Z", YELLOW) + P("M256,170 Q322,80 352,120 Q362,160 256,170 Z", YELLOW)
    s += R(120, 240, 272, 190, "#e63980", 8)
    s += R(100, 176, 312, 72, "#f05b9b", 10)
    s += R(236, 176, 40, 254, YELLOW, 0)
    s += C(256, 172, 18, YELLOW)
    return s


def balloon():
    s = ""
    for cx, cy, c, ex in ((176, 190, RED, 260), (336, 170, BLUE, 260), (256, 130, YELLOW, 256)):
        s += P(f"M{cx},{cy + 104} Q{cx + 10},{cy + 180} {ex},{430}", extra='stroke-width="4"')
    for cx, cy, c in ((176, 190, RED), (336, 170, BLUE), (256, 130, YELLOW)):
        s += PL([(cx, cy + 96), (cx - 12, cy + 112), (cx + 12, cy + 112)], c, 'stroke-width="5"')
        s += E(cx, cy, 72, 92, c)
        s += shine(f"M{cx - 40},{cy - 20} Q{cx - 36},{cy - 56} {cx - 10},{cy - 70}")
    s += R(240, 424, 32, 24, PINK, 6)
    return s


DRAW = {
    "boy": boy, "girl": girl, "man": man, "woman": woman, "baby": baby,
    "house": house, "door": door, "window": window, "bed": bed, "chair": chair, "table": table, "lamp": lamp,
    "car": car, "bus": bus, "bike": bike, "boat": boat, "train": train, "plane": plane,
    "dog": dog, "cat": cat, "bird": bird, "fish": fish, "horse": horse, "cow": cow,
    "apple": apple, "banana": banana, "bread": bread, "egg": egg, "milk": milk, "water": water, "cake": cake,
    "sun": sun, "moon": moon, "star": star, "tree": tree, "flower": flower, "cloud": cloud,
    "ball": ball, "book": book, "pen": pen, "phone": phone, "cup": cup, "key": key, "bag": bag, "clock": clock,
    "hat": hat, "shoe": shoe, "shirt": shirt, "hand": hand, "eye": eye,
    "pig": pig, "sheep": sheep, "duck": duck, "rabbit": rabbit, "elephant": elephant, "lion": lion, "frog": frog, "butterfly": butterfly,
    "orange": orange, "carrot": carrot, "tomato": tomato, "cheese": cheese, "pizza": pizza, "ice-cream": ice_cream, "grapes": grapes, "strawberry": strawberry,
    "sofa": sofa, "television": television, "computer": computer, "umbrella": umbrella, "glasses": glasses,
    "plate": plate, "spoon": spoon, "fork": fork, "bottle": bottle,
    "dress": dress, "sock": sock, "trousers": trousers, "scarf": scarf,
    "mountain": mountain, "sea": sea, "rain": rain, "snow": snow, "rainbow": rainbow, "leaf": leaf, "fire": fire,
    "truck": truck, "helicopter": helicopter, "motorbike": motorbike,
    "nose": nose, "mouth": mouth, "ear": ear, "foot": foot, "tooth": tooth,
    "pencil": pencil, "scissors": scissors, "guitar": guitar, "kite": kite, "gift": gift, "balloon": balloon,
}

BG_OVERRIDE = {"moon": NIGHT, "star": NIGHT, "cloud": SKY, "rain": "#dde5ee", "sea": SKY, "rainbow": SKY,
               "kite": SKY, "balloon": SKY, "plane": SKY, "helicopter": SKY, "butterfly": "#e9f5db"}


def render(slug, category):
    bg = BG_OVERRIDE.get(slug, CATEGORY_BG.get(category, "#f1f3f5"))
    return svg(DRAW[slug](), bg)
