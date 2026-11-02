"""B1 illustrations. Same style and helpers as art.py / art_a2.py; registers into art.DRAW."""
import math

import art
from art import (OUT, SKIN, HAIR, BLONDE, RED, DRED, BLUE, NAVY, LBLUE, SKY, GREEN, DGREEN, LGREEN, YELLOW,
                 ORANGE, DORANGE, PINK, PURPLE, BROWN, DBROWN, TAN, GREY, DGREY, WHITE, CREAM, NIGHT,
                 C, E, R, P, PL, L, NS, dot, limb, ring, merged, rot, tr, shadow, shine, scallop, star_pts,
                 eyes, smile, cheeks, wheel, cloud_shape)
from art_a2 import clip, nf, patterned, sky, water, pine, GOLD, SAND

CONCRETE = "#ced4da"


def ground(color=CONCRETE, y=420):
    return NS(R(0, y, 512, 512 - y, color))


def window_grid(x, y, cols, rows, w, h, gx, gy, fill=LBLUE, extra='stroke-width="4"'):
    return "".join(R(x + c * (w + gx), y + r * (h + gy), w, h, fill, 2, extra) for c in range(cols) for r in range(rows))


def awning(x, y, w, h, c1, c2, cid):
    n = 8
    shape = P(f"M{x},{y} L{x + w},{y} L{x + w},{y + h} " +
              " ".join(f"Q{x + w - (i + .5) * w / n},{y + h + 22} {x + w - (i + 1) * w / n},{y + h}" for i in range(n)) + " Z")
    stripes = "".join(R(x + i * w / n, y - 4, w / n / 2, h + 40, c2) for i in range(n))
    return patterned(cid, shape, c1, stripes)


def shop(wall, awn, sign_icon, cid, window_content=""):
    s = sky() + ground()
    s += R(64, 140, 384, 290, wall, 6)
    s += R(50, 120, 412, 30, DGREY, 6)
    s += R(146, 156, 220, 60, WHITE, 12) + sign_icon
    s += awning(80, 236, 352, 34, awn, WHITE, cid)
    s += R(96, 300, 150, 110, LBLUE, 4) + window_content
    s += R(290, 296, 96, 134, DBROWN, 4) + dot(372, 366, 6, YELLOW)
    s += R(270, 426, 136, 10, GREY, 2)
    return s


# ---------------------------------------------------------------- places
def skyscraper():
    s = sky() + ground("#adb5bd", 440)
    s += R(60, 220, 110, 220, "#8fa3b8") + window_grid(76, 236, 3, 6, 20, 20, 12, 12, "#d6e4f0", 'stroke="none"')
    s += R(342, 180, 110, 260, "#9aa5b1") + window_grid(356, 196, 3, 8, 22, 18, 12, 12, "#d6e4f0", 'stroke="none"')
    s += L(256, 40, 256, 12, 8) + C(256, 10, 7, RED)
    s += PL([(206, 80), (256, 40), (306, 80)], "#5c7c99")
    s += R(186, 80, 140, 360, "#6c9bc6")
    for x in range(198, 320, 28):
        s += R(x, 96, 18, 330, "#a9d0f5", 2, 'stroke="none"')
    s += "".join(L(186, y, 326, y, 4) for y in range(120, 440, 40))
    s += R(186, 80, 140, 360, "none")
    return s


def tunnel():
    s = sky()
    s += P("M-10,440 L60,220 Q140,120 256,110 Q380,120 450,220 L522,440 Z", "#74c69d")
    s += P("M150,440 L150,330 Q150,230 256,230 Q362,230 362,330 L362,440 Z", "#a98467")
    s += P("M176,440 L176,334 Q176,256 256,256 Q336,256 336,334 L336,440 Z", "#2b2d42")
    s += PL([(176, 440), (336, 440), (420, 512), (92, 512)], DGREY, 'stroke="none"')
    s += P("M256,446 L256,470 M256,486 L256,512", extra=f'stroke="{YELLOW}" stroke-width="8"')
    s += NS(C(226, 330, 6, YELLOW) + C(286, 330, 6, YELLOW))
    s += pine(70, 260, 90, DGREEN) + pine(440, 270, 90, DGREEN)
    return s


def small_boat(x, y, c, mast=True):
    s = P(f"M{x - 60},{y} L{x + 60},{y} L{x + 40},{y + 34} L{x - 40},{y + 34} Z", c)
    if mast:
        s += L(x, y, x, y - 110, 6) + PL([(x + 4, y - 104), (x + 4, y - 10), (x + 56, y - 10)], WHITE)
    return s


def harbour():
    s = sky() + water(320, "#4ea8de", "#2a7fc1")
    s += small_boat(130, 330, RED) + small_boat(380, 350, YELLOW) + small_boat(250, 300, WHITE, False)
    s += R(0, 400, 512, 30, "#a0522d")
    s += "".join(R(x, 430, 16, 82, "#6f3b1f", 2) for x in (30, 150, 270, 390, 490))
    s += "".join(L(x, 400, x, 430, 4) for x in range(40, 512, 40))
    s += "".join(R(x, 380, 22, 22, DGREY, 6) for x in (90, 330))
    s += P("M101,384 Q120,360 130,340", extra='stroke-width="4"')
    return s


def factory():
    s = sky() + ground()
    s += NS(C(140, 70, 24, "#dee2e6") + C(170, 50, 30, "#dee2e6") + C(380, 80, 22, "#dee2e6") + C(410, 56, 28, "#dee2e6"))
    s += R(120, 100, 40, 160, "#9aa5b1") + R(360, 110, 40, 150, "#9aa5b1")
    s += R(116, 112, 48, 14, RED, 0) + R(356, 122, 48, 14, RED, 0)
    s += P("M60,430 L60,260 L140,200 L140,260 L220,200 L220,260 L300,200 L300,260 L380,200 L380,260 L452,210 L452,430 Z", "#b56576")
    s += window_grid(90, 300, 5, 1, 50, 40, 22, 0, "#ffd166")
    s += R(210, 360, 92, 70, DGREY, 4) + "".join(L(210, y, 302, y, 3) for y in range(372, 430, 12))
    return s


def museum():
    St = "#e9ecef"
    s = sky() + ground("#adb5bd", 430)
    s += PL([(70, 160), (256, 70), (442, 160)], St)
    s += C(256, 130, 18, YELLOW)
    s += R(70, 160, 372, 30, St)
    for x in range(98, 430, 66):
        s += R(x, 196, 36, 190, WHITE) + R(x - 6, 190, 48, 12, St) + R(x - 6, 380, 48, 12, St)
    s += R(60, 392, 392, 18, St) + R(44, 410, 424, 20, St)
    return s


def library():
    cols = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, "#2a9d8f", PINK, NAVY]
    s = shadow(256, 456, 210)
    s += R(60, 60, 392, 390, "#8b5a2b", 10)
    k = 0
    for row in range(3):
        y0 = 80 + row * 122
        s += R(76, y0, 360, 104, "#5e3a1a", 4)
        x = 84
        while x < 420:
            w = 22 + (k * 7) % 14
            h = 72 + (k * 13) % 26
            if x + w > 428:
                break
            if k % 7 == 5:
                s += rot(-14, x, y0 + 100, R(x, y0 + 104 - h, w, h, cols[k % 9], 3, 'stroke-width="4"'))
                x += w + 18
            else:
                s += R(x, y0 + 104 - h, w, h, cols[k % 9], 3, 'stroke-width="4"')
                s += L(x + 4, y0 + 104 - h + 14, x + w - 4, y0 + 104 - h + 14, 3, WHITE)
                x += w + 2
            k += 1
        s += R(70, y0 + 104, 372, 14, "#8b5a2b", 2)
    return s


def stadium():
    s = sky()
    for x in (60, 452):
        s += L(x, 60, x, 300, 8) + R(x - 30, 40, 60, 30, "#e9ecef", 4) + NS(C(x - 15, 55, 6, YELLOW) + C(x + 15, 55, 6, YELLOW))
    s += E(256, 330, 236, 140, "#adb5bd")
    s += E(256, 330, 236, 140, "none", f'stroke="{RED}" stroke-width="18" stroke-dasharray="6 10"')
    s += E(256, 330, 236, 140, "none")
    s += E(256, 340, 180, 96, "#52b788")
    s += P("M256,244 L256,436", extra=f'stroke="{WHITE}" stroke-width="5"') + E(256, 340, 34, 18, "none", f'stroke="{WHITE}" stroke-width="5"')
    s += R(86, 316, 30, 48, "none", 0, f'stroke="{WHITE}" stroke-width="5"') + R(396, 316, 30, 48, "none", 0, f'stroke="{WHITE}" stroke-width="5"')
    return s


def cross(cx, cy, size, color):
    w = size * 0.34
    return R(cx - w / 2, cy - size / 2, w, size, color, 3) + R(cx - size / 2, cy - w / 2, size, w, color, 3)


def hospital():
    s = sky() + ground()
    s += R(60, 170, 120, 260, "#e9ecef") + R(332, 170, 120, 260, "#e9ecef")
    s += R(160, 110, 192, 320, WHITE)
    s += window_grid(76, 190, 3, 5, 24, 24, 12, 22) + window_grid(348, 190, 3, 5, 24, 24, 12, 22)
    s += window_grid(180, 230, 4, 3, 30, 26, 12, 20)
    s += R(206, 120, 100, 90, WHITE, 8, 'stroke="none"') + NS(cross(256, 165, 74, RED))
    s += R(206, 350, 100, 80, "#a8dadc") + L(256, 350, 256, 430, 5)
    s += R(196, 340, 120, 14, "#457b9d", 3)
    return s


def pharmacy():
    win = NS(R(110, 340, 26, 46, "#fff", 4) + R(146, 326, 24, 60, "#ffd6a5", 4) + R(180, 350, 40, 36, "#caffbf", 6))
    return shop("#d8f3dc", "#2a9d8f", NS(cross(256, 186, 48, "#2a9d8f")), "aw1", win) + R(150, 318, 100, 6, "none")


def bakery():
    icon = E(256, 190, 50, 22, TAN, 'stroke-width="5"') + P("M232,182 L240,196 M252,180 L260,196 M272,182 L280,196", extra=f'stroke="{CREAM}" stroke-width="5"')
    win = (E(140, 380, 30, 14, TAN, 'stroke-width="4"') + E(200, 380, 30, 14, "#c08552", 'stroke-width="4"')
           + C(170, 340, 18, "#e9c46a", 'stroke-width="4"') + C(216, 340, 14, PINK, 'stroke-width="4"'))
    return shop("#ffe5d9", "#e76f51", icon, "aw2", win)


def cart(x, y, sc=1, color=RED):
    return tr(x, y, P("M-50,-30 L-36,-30 L-26,20 L36,20 L46,-14 L-30,-14", extra=f'stroke="{color}" stroke-width="7"')
              + C(-18, 32, 7, OUT) + C(30, 32, 7, OUT), sc)


def supermarket():
    win = NS("".join(C(120 + i * 26, 360, 11, c) for i, c in enumerate((RED, ORANGE, YELLOW, GREEN, RED))) + R(110, 380, 120, 10, "#adb5bd"))
    s = shop("#e3f2fd", RED, cart(256, 186, 0.9), "aw3", win)
    s += cart(120, 450, 0.9, BLUE)
    return s


def restaurant():
    icon = (L(236, 166, 236, 206, 6) + P("M226,166 L226,182 Q236,190 246,182 L246,166", extra='stroke-width="5"')
            + P("M276,166 Q290,176 286,190 L276,192 L276,206", extra='stroke-width="6"'))
    win = NS(E(170, 380, 60, 8, WHITE)) + R(140, 336, 60, 24, "none", 0, 'stroke="none"') + C(126, 352, 10, RED, 'stroke-width="4"') + C(214, 352, 10, RED, 'stroke-width="4"')
    return shop("#fff1e6", "#9d0208", icon, "aw4", win)


def post_office():
    icon = R(226, 170, 60, 34, CREAM, 3, 'stroke-width="5"') + P("M226,172 L256,192 L286,172", extra='stroke-width="5"')
    s = shop("#fff3b0", "#ffb703", icon, "aw5", NS(R(110, 330, 50, 34, CREAM) + R(170, 350, 60, 40, "#f4a261")))
    s += R(26, 330, 38, 90, RED, 8) + R(34, 350, 22, 6, OUT, 2) + R(40, 420, 10, 10, OUT)
    return s


def police_station():
    s = sky() + ground()
    s += R(64, 150, 384, 280, "#457b9d", 6) + R(50, 130, 412, 30, NAVY, 6)
    s += R(236, 92, 40, 40, "#3a86ff", 10) + R(228, 124, 56, 12, OUT, 3)
    s += NS(PL([(206, 92), (236, 104), (236, 118)], "#ffe066", 'opacity=".8"') + PL([(306, 92), (276, 104), (276, 118)], "#ffe066", 'opacity=".8"'))
    s += C(256, 206, 36, WHITE) + PL(star_pts(256, 206, 28, 12, 6), GOLD, 'stroke-width="5"')
    s += window_grid(92, 270, 2, 2, 50, 50, 16, 16) + window_grid(320, 270, 2, 2, 50, 50, 16, 16)
    s += R(214, 300, 84, 130, "#1d3557", 4) + L(256, 300, 256, 430, 4)
    return s


def fire_station():
    Br = "#c1121f"
    s = sky() + ground()
    s += R(200, 60, 112, 90, Br) + PL([(190, 60), (256, 20), (322, 60)], DGREY) + C(256, 104, 20, YELLOW)
    s += R(50, 150, 412, 280, Br, 4) + R(40, 136, 432, 24, DGREY, 4)
    s += NS("".join(R(60 + (r % 2) * 20 + c * 40, 170 + r * 18, 30, 4, "#9d0208") for r in range(4) for c in range(10)))
    s += R(80, 250, 160, 180, "#e9ecef", 6) + "".join(L(80, y, 240, y, 4) for y in range(272, 430, 22))
    s += R(272, 250, 160, 180, "#343a40", 6)
    s += R(292, 300, 120, 130, RED, 10) + R(306, 316, 92, 40, LBLUE, 4) + NS(C(310, 380, 8, YELLOW) + C(394, 380, 8, YELLOW)) + R(292, 400, 120, 14, GREY, 2)
    return s


# ---------------------------------------------------------------- science
def laboratory():
    s = shadow(256, 440, 200)
    s += R(60, 410, 392, 24, "#adb5bd", 4)
    s += P("M116,150 L170,150 L170,250 L230,390 Q236,410 214,410 L72,410 Q50,410 56,390 L116,250 Z", "#f1f8ff")
    s += NS(P("M90,320 L196,320 L226,392 Q230,404 214,404 L72,404 Q58,404 62,392 Z", "#80ed99"))
    s += P("M116,150 L170,150 L170,250 L230,390 Q236,410 214,410 L72,410 Q50,410 56,390 L116,250 Z", "none")
    s += R(108, 140, 70, 16, GREY, 4)
    s += NS(C(120, 360, 10, WHITE, 'opacity=".8"') + C(150, 290, 8, WHITE, 'opacity=".8"') + C(160, 250, 6, WHITE, 'opacity=".8"'))
    s += R(270, 300, 170, 26, "#8d6e63", 4)
    for i, c in enumerate((RED, "#4ea8de", YELLOW)):
        x = 292 + i * 50
        s += P(f"M{x},{170} L{x + 30},{170} L{x + 30},{360} Q{x + 15},{386} {x},{360} Z", "#f1f8ff")
        s += NS(P(f"M{x + 3},{260 + i * 20} L{x + 27},{260 + i * 20} L{x + 27},{358} Q{x + 15},{380} {x + 3},{358} Z", c))
        s += P(f"M{x},{170} L{x + 30},{170} L{x + 30},{360} Q{x + 15},{386} {x},{360} Z", "none")
    s += R(270, 300, 170, 26, "#8d6e63", 4) + R(282, 326, 12, 84, "#8d6e63") + R(416, 326, 12, 84, "#8d6e63")
    return s


def microscope():
    s = shadow(256, 444, 150)
    s += R(150, 400, 220, 40, DGREY, 12)
    s += P("M300,400 L300,300 Q300,220 240,190", extra='stroke-width="44"') + P("M300,400 L300,300 Q300,220 240,190", extra=f'stroke="#e9ecef" stroke-width="30"')
    s += R(150, 300, 150, 18, DGREY, 4)
    s += R(200, 284, 60, 14, LBLUE, 2, 'stroke-width="4"')
    s += rot(-30, 230, 170, R(200, 60, 58, 220, WHITE, 10) + R(196, 40, 66, 30, DGREY, 6) + R(212, 270, 34, 40, DGREY, 4))
    s += C(312, 330, 16, GREY)
    return s


def telescope():
    s = NS(R(0, 0, 512, 512, NIGHT, 48))
    s += NS("".join(PL(star_pts(x, y, r, r * .45), "#fff4b8") for x, y, r in ((420, 80, 16), (330, 50, 8), (460, 200, 10), (80, 90, 9), (150, 50, 6))))
    s += NS(C(380, 140, 34, "#fde68a"))
    s += L(256, 300, 160, 450, 10) + L(256, 300, 352, 450, 10) + L(256, 300, 256, 460, 10)
    s += rot(-30, 256, 270, R(120, 236, 300, 64, "#e9ecef", 14) + R(390, 226, 60, 84, "#3a86ff", 10) + R(90, 248, 40, 40, DGREY, 6) + R(220, 230, 40, 76, DGREY, 4))
    return s


def satellite():
    s = NS(R(0, 0, 512, 512, NIGHT, 48))
    s += P("M-20,420 Q256,340 532,420 L532,532 L-20,532 Z", "#4ea8de")
    s += NS(P("M60,430 Q120,400 180,420 Q160,450 80,450 Z", "#74c69d") + P("M330,410 Q400,390 440,420 Q400,440 340,436 Z", "#74c69d"))
    s += NS("".join(C(x, y, 3, "#fff4b8") for x, y in ((60, 60), (450, 90), (420, 260), (90, 280), (300, 40))))
    p = (R(50, 160, 140, 80, "#1e6091", 4) + "".join(L(50 + i * 28, 160, 50 + i * 28, 240, 3, "#9ad1f5") for i in range(1, 5)) + L(50, 200, 190, 200, 3, "#9ad1f5")
         + R(322, 160, 140, 80, "#1e6091", 4) + "".join(L(322 + i * 28, 160, 322 + i * 28, 240, 3, "#9ad1f5") for i in range(1, 5)) + L(322, 200, 462, 200, 3, "#9ad1f5")
         + L(190, 200, 210, 200, 8) + L(302, 200, 322, 200, 8)
         + R(210, 150, 92, 100, GOLD, 8) + "".join(L(210, y, 302, y, 3, "#c98a2b") for y in (175, 200, 225))
         + P("M226,150 Q256,90 286,150 Z", "#e9ecef") + L(256, 120, 256, 90, 5) + C(256, 86, 6, RED))
    s += rot(-15, 256, 200, p)
    return s


def robot():
    s = shadow(256, 450, 140)
    s += R(190, 360, 44, 80, GREY, 8) + R(278, 360, 44, 80, GREY, 8) + R(180, 424, 64, 20, DGREY, 6) + R(268, 424, 64, 20, DGREY, 6)
    s += limb("M170,250 L120,330", GREY, 26) + limb("M342,250 L392,330", GREY, 26)
    s += C(116, 340, 20, DGREY) + C(396, 340, 20, DGREY)
    s += R(166, 220, 180, 150, "#4ea8de", 20)
    s += R(206, 250, 100, 60, "#e9ecef", 8) + NS(C(226, 280, 9, RED) + C(256, 280, 9, YELLOW) + C(286, 280, 9, GREEN))
    s += R(230, 186, 52, 40, GREY)
    s += R(176, 80, 160, 116, "#4ea8de", 26)
    s += R(196, 104, 120, 60, NIGHT, 14) + C(226, 134, 14, "#80ffdb", 'stroke="none"') + C(286, 134, 14, "#80ffdb", 'stroke="none"')
    s += L(256, 80, 256, 44, 7) + C(256, 40, 12, RED)
    s += R(160, 116, 18, 40, GREY, 6) + R(334, 116, 18, 40, GREY, 6)
    return s


def solar_panel():
    s = sky() + NS(C(410, 100, 50, YELLOW)) + ground("#95d5b2", 400)
    s += "".join(rot(a, 410, 100, L(410, 30, 410, 10, 8, ORANGE)) for a in range(0, 360, 45))
    s += L(200, 300, 180, 430, 12) + L(320, 300, 340, 430, 12)
    s += PL([(90, 330), (380, 330), (440, 200), (150, 200)], "#1e6091")
    for i in range(1, 6):
        s += L(90 + i * 290 / 6, 330, 150 + i * 290 / 6, 200, 4, "#9ad1f5")
    for j in (1, 2):
        y = 330 - j * 130 / 3
        s += L(90 + j * 60 / 3, y, 380 + j * 60 / 3, y, 4, "#9ad1f5")
    s += PL([(90, 330), (380, 330), (440, 200), (150, 200)], "none")
    return s


def wind_turbine():
    s = sky() + P("M-10,460 Q150,380 300,430 Q420,460 522,410 L522,522 L-10,522 Z", "#74c69d")
    s += PL([(244, 180), (268, 180), (280, 450), (232, 450)], WHITE)
    for a in (0, 120, 240):
        s += rot(a + 10, 256, 170, P("M250,170 Q236,100 256,30 Q276,100 262,170 Z", WHITE))
    s += C(256, 170, 18, "#e9ecef")
    s += tr(130, 70, PL([(110, 180), (118, 180), (124, 400), (104, 400)], WHITE) + "".join(rot(a + 40, 114, 176, P("M111,176 Q104,140 114,104 Q124,140 117,176 Z", WHITE)) for a in (0, 120, 240)) + C(114, 176, 8, "#e9ecef"), 0.8)
    return s


def recycle_arrow(cx, cy, r, color):
    """three chasing arrows around a circle"""
    s = ""
    for a in (0, 120, 240):
        a0, a1 = math.radians(a + 12), math.radians(a + 92)
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        s += f'<path d="M{x0:.1f},{y0:.1f} A{r},{r} 0 0 1 {x1:.1f},{y1:.1f}" fill="none" stroke="{color}" stroke-width="{r * .26:.0f}" stroke-linecap="butt"/>'
        t = a1 + math.pi / 2
        hx, hy = math.cos(t), math.sin(t)
        nx, ny = math.cos(a1), math.sin(a1)
        h = r * 0.32
        s += PL([(round(x1 + nx * h, 1), round(y1 + ny * h, 1)), (round(x1 - nx * h, 1), round(y1 - ny * h, 1)),
                 (round(x1 + hx * h * 1.3, 1), round(y1 + hy * h * 1.3, 1))], color, 'stroke="none"')
    return s


def recycling_bin():
    s = shadow(256, 450, 140)
    s += P("M140,150 L372,150 L350,436 L162,436 Z", "#2a9d8f")
    s += R(120, 120, 272, 40, "#21867a", 10) + R(226, 98, 60, 26, "#21867a", 8)
    s += recycle_arrow(256, 300, 70, WHITE)
    s += C(180, 446, 12, OUT) + C(332, 446, 12, OUT)
    return s


# ---------------------------------------------------------------- health
def wheelchair():
    s = shadow(256, 450, 180)
    s += C(220, 330, 110, "none", 'stroke-width="14"') + C(220, 330, 92, "none", f'stroke="{GREY}" stroke-width="6"')
    s += "".join(L(220 - 90 * math.cos(math.radians(a)), 330 - 90 * math.sin(math.radians(a)), 220 + 90 * math.cos(math.radians(a)), 330 + 90 * math.sin(math.radians(a)), 3, DGREY) for a in range(0, 180, 30))
    s += C(220, 330, 14, DGREY)
    s += P("M160,110 L180,250 L340,250 L360,370 L400,370", extra='stroke-width="20"')
    s += P("M160,110 L180,250 L340,250 L360,370 L400,370", extra=f'stroke="#3a86ff" stroke-width="10"')
    s += P("M140,110 L180,110", extra='stroke-width="16"')
    s += R(176, 230, 150, 26, "#1d3557", 8) + R(170, 120, 26, 120, "#1d3557", 8)
    s += L(340, 280, 380, 420, 8) + C(380, 426, 18, OUT)
    return s


def crutch(x):
    return (R(x - 46, 60, 92, 26, "#495057", 13) + L(x - 30, 80, x - 16, 360, 12, GREY) + L(x + 30, 80, x + 16, 360, 12, GREY)
            + R(x - 30, 220, 60, 22, "#495057", 8) + L(x, 360, x, 440, 14, GREY) + R(x - 12, 430, 24, 22, OUT, 6))


def crutches():
    return shadow(256, 450, 150) + rot(-10, 180, 256, crutch(180)) + rot(10, 332, 256, crutch(332))


def bandage():
    s = shadow(256, 420, 170)
    b = (R(70, 200, 372, 112, "#e9b98a", 56) + R(196, 214, 120, 84, "#f6d5b5", 10, 'stroke-width="5"')
         + NS("".join(C(x, y, 5, "#c98d5a") for x in (110, 140, 160, 352, 372, 400) for y in (236, 276) if not (x == 160 and y == 236))))
    s += rot(-30, 256, 256, b)
    return s


def thermometer():
    s = shadow(256, 460, 100)
    s += R(216, 50, 80, 330, WHITE, 40)
    s += C(256, 400, 56, RED)
    s += R(240, 100, 32, 300, RED, 16, 'stroke="none"')
    s += R(216, 50, 80, 330, "none", 40)
    s += "".join(L(300, y, 330 if (y // 30) % 2 == 0 else 318, y, 5) for y in range(90, 340, 30))
    s += shine("M234,90 L234,300")
    return s


def stethoscope_():
    s = shadow(256, 450, 140)
    s += limb("M170,80 L180,190 Q186,260 256,270 Q326,260 332,190 L342,80", DGREY, 12)
    s += C(168, 70, 14, OUT) + C(344, 70, 14, OUT)
    s += limb("M256,270 L256,320 Q256,400 330,380", "#3a86ff", 16)
    s += C(352, 370, 42, GREY) + C(352, 370, 26, "#e9ecef")
    return s


def syringe():
    s = shadow(256, 430, 150)
    g = (R(130, 236, 220, 52, "#f1f8ff", 10) + NS(R(220, 242, 126, 40, "#90e0ef", 4))
         + R(130, 236, 220, 52, "none", 10) + "".join(L(x, 236, x, 254, 4) for x in range(170, 340, 24))
         + R(114, 220, 16, 84, DGREY, 4) + R(50, 252, 70, 20, GREY, 4) + R(36, 232, 18, 60, DGREY, 6)
         + R(350, 248, 30, 28, GREY, 4) + L(380, 262, 470, 262, 4, DGREY))
    s += rot(-30, 256, 262, g)
    return s


def pills():
    s = shadow(256, 440, 190)
    s += R(270, 170, 150, 240, "#f4a261", 20) + R(260, 130, 170, 50, WHITE, 12)
    s += R(290, 250, 110, 90, WHITE, 8) + NS(cross(345, 295, 50, RED))
    s += rot(-30, 160, 300, R(80, 270, 80, 56, RED, 28) + R(150, 270, 80, 56, WHITE, 28) + NS(R(140, 274, 20, 48, WHITE)) + R(80, 270, 150, 56, "none", 28))
    s += C(140, 410, 34, WHITE) + L(110, 410, 170, 410, 5)
    s += C(230, 400, 26, YELLOW) + L(208, 400, 252, 400, 5)
    return s


# ---------------------------------------------------------------- jewellery / clothes
def gem(cx, cy, r, color):
    return (PL([(cx - r, cy - r * .3), (cx - r * .5, cy - r * .9), (cx + r * .5, cy - r * .9), (cx + r, cy - r * .3), (cx, cy + r)], color, 'stroke-width="5"')
            + P(f"M{cx - r},{cy - r * .3} L{cx + r},{cy - r * .3} M{cx - r * .5},{cy - r * .9} L{cx},{cy + r} L{cx + r * .5},{cy - r * .9}", extra='stroke-width="3"'))


def sparkle(cx, cy, r):
    return PL(star_pts(cx, cy, r, r * 0.3, 4), "#fff4b8", 'stroke-width="4"')


def jewellery():
    s = shadow(256, 444, 190)
    s += PL([(90, 250), (422, 250), (392, 110), (120, 110)], "#9d0208")
    s += PL([(110, 240), (402, 240), (378, 128), (134, 128)], "#e5383b", 'stroke-width="5"')
    s += R(80, 250, 352, 180, "#9d0208", 12)
    s += R(100, 250, 312, 40, "#e5383b", 6)
    s += "".join(C(140 + i * 22, 268 + 10 * math.sin(i / 2), 11, WHITE, 'stroke-width="4"') for i in range(6))
    s += ring(330, 262, 26, GOLD, 10) + gem(330, 230, 18, "#80ffdb")
    s += C(256, 380, 22, GOLD) + sparkle(130, 90, 18) + sparkle(400, 80, 14)
    return s


def necklace():
    s = P("M100,60 Q100,340 256,360 Q412,340 412,60", extra=f'stroke="{GOLD}" stroke-width="5"')
    pts = []
    for i in range(1, 26):
        t = i / 26
        x = (1 - t) ** 2 * 100 + 2 * (1 - t) * t * 256 + t * t * 412
        y = (1 - t) ** 2 * 60 + 2 * (1 - t) * t * 480 + t * t * 60
        pts.append((x, y))
    s += "".join(C(x, y, 14, WHITE, 'stroke-width="5"') for x, y in pts if abs(x - 256) > 14)
    s += L(256, 340, 256, 372, 5, GOLD)
    s += gem(256, 400, 34, "#4ea8de")
    s += sparkle(320, 420, 14) + sparkle(190, 380, 10)
    return s


def ring_():
    s = shadow(256, 440, 130)
    s += E(256, 320, 130, 110, "none", 'stroke-width="44"') + E(256, 320, 130, 110, "none", f'stroke="{GOLD}" stroke-width="30"')
    s += P("M140,300 Q150,250 190,230", extra=f'stroke="#fff4b8" stroke-width="8"')
    s += R(226, 196, 60, 22, GOLD, 4)
    s += gem(256, 160, 56, "#caf0f8")
    s += sparkle(350, 110, 22) + sparkle(160, 120, 14) + sparkle(380, 200, 10)
    return s


def bracelet():
    s = shadow(256, 430, 170)
    s += E(256, 280, 170, 100, "none", 'stroke-width="50"') + E(256, 280, 170, 100, "none", f'stroke="{GOLD}" stroke-width="36"')
    for i, c in enumerate((RED, "#4ea8de", GREEN, PURPLE, RED, "#4ea8de", GREEN)):
        a = math.radians(20 + i * 23)
        s += C(256 + 170 * math.cos(a), 280 + 100 * math.sin(a), 14, c, 'stroke-width="5"')
    s += sparkle(400, 140, 18)
    return s


def perfume():
    s = shadow(256, 444, 140)
    s += limb("M300,130 Q380,120 390,170", "#495057", 6) + C(400, 196, 30, PINK)
    s += R(226, 100, 60, 60, GOLD, 8)
    s += PL([(150, 200), (362, 200), (392, 280), (362, 430), (150, 430), (120, 280)], "#fde2e4")
    s += NS(PL([(126, 290), (386, 290), (360, 424), (152, 424)], "#f4a6c1"))
    s += PL([(150, 200), (362, 200), (392, 280), (362, 430), (150, 430), (120, 280)], "none")
    s += R(210, 160, 92, 44, "#fde2e4")
    s += shine("M170,240 L160,380") + sparkle(120, 120, 18) + sparkle(440, 300, 14)
    s += NS("".join(C(x, y, 5, "#c77dff", 'opacity=".7"') for x, y in ((440, 170), (460, 150), (470, 190), (450, 210))))
    return s


def pyjamas():
    B = "#a2d2ff"
    s = shadow(256, 450, 200)
    top = (P("M70,120 L120,96 Q150,116 180,96 L230,120 L250,200 L214,210 L206,180 L206,330 L94,330 L94,180 L86,210 L50,200 Z", B)
           + P("M150,110 L150,330", extra='stroke-width="5"') + "".join(dot(160, y, 5) for y in (150, 200, 250, 300)))
    pants = P("M290,160 L450,160 L466,440 L392,440 L370,240 L348,440 L274,440 Z", B) + R(286, 150, 168, 26, "#80b9ef", 4)
    pattern = NS("".join(PL(star_pts(x, y, 11, 5), YELLOW) for x, y in ((120, 160), (180, 230), (120, 290), (320, 220), (420, 300), (310, 380), (420, 400))))
    pattern += NS("".join(P(f"M{x},{y} A14,14 0 1 0 {x + 6},{y + 22} A11,11 0 1 1 {x},{y} Z", "#fff") for x, y in ((190, 140), (110, 220), (390, 230), (350, 330))))
    return s + top + pants + pattern


def raincoat():
    Y = "#ffd60a"
    s = shadow(256, 450, 150)
    s += NS("".join(P(f"M{x},{y} Q{x + 14},{y + 24} {x},{y + 30} Q{x - 14},{y + 24} {x},{y} Z", "#4ea8de") for x, y in ((60, 80), (440, 120), (70, 300), (450, 340), (400, 50))))
    s += P("M200,100 Q256,40 312,100 L380,150 L420,330 L380,340 L360,250 L360,440 L152,440 L152,250 L132,340 L92,330 L132,150 Z", Y)
    s += P("M196,104 Q256,30 316,104 Q316,170 256,170 Q196,170 196,104 Z", Y)
    s += P("M214,110 Q256,70 298,110 Q298,150 256,150 Q214,150 214,110 Z", "#3d405b")
    s += L(256, 170, 256, 440, 6) + "".join(C(276, y, 8, "#3d405b") for y in (220, 280, 340, 400))
    s += R(170, 330, 50, 40, "none", 6, 'stroke-width="6"')
    return s


def boot(x, color):
    return (P(f"M{x - 50},{90} L{x + 30},{90} L{x + 30},{330} Q{x + 110},{340} {x + 110},{400} L{x + 110},{430} L{x - 50},{430} Z", color)
            + R(x - 56, 80, 92, 34, color, 8) + R(x - 50, 410, 160, 26, OUT, 8))


def boots():
    return shadow(256, 444, 200) + boot(110, "#52b788") + boot(290, "#e63946") + P("M70,200 L130,200 M250,200 L310,200", extra=f'stroke="{WHITE}" stroke-width="6" opacity=".6"')


def sandal(x, flip):
    g = (P("M-60,-150 Q0,-190 60,-150 Q80,-40 50,60 Q40,170 0,180 Q-40,170 -50,60 Q-80,-40 -60,-150 Z", "#d4a373")
         + P("M-58,-60 Q0,-20 58,-60", extra=f'stroke="{DORANGE}" stroke-width="24"')
         + P("M-56,40 Q0,70 56,40", extra=f'stroke="{DORANGE}" stroke-width="20"'))
    return tr(x, 256, g if not flip else f'<g transform="scale(-1 1)">{g}</g>')


def sandals():
    return shadow(256, 450, 180) + rot(-8, 170, 256, sandal(170, False)) + rot(8, 342, 256, sandal(342, True))


def belt():
    s = shadow(256, 420, 200)
    s += P("M60,230 Q256,170 452,230 L452,290 Q256,230 60,290 Z", "#6f3b1f")
    s += P("M60,260 Q256,200 452,260", extra=f'stroke="#c08552" stroke-width="3" stroke-dasharray="10 8"')
    s += "".join(C(x, 252 - 40 * math.sin(math.pi * (x - 60) / 392) + 10, 6, OUT) for x in (330, 360, 390, 420))
    s += R(140, 196, 90, 100, "none", 14, f'stroke="{OUT}" stroke-width="26"') + R(140, 196, 90, 100, "none", 14, f'stroke="{GOLD}" stroke-width="12"')
    s += L(185, 210, 185, 284, 10, GOLD)
    return s


def tie():
    s = PL([(150, 60), (256, 110), (362, 60), (362, 120), (256, 140), (150, 120)], WHITE)
    body = PL([(232, 130), (280, 130), (320, 380), (256, 460), (192, 380)])
    s += patterned("tie", body, NAVY, "".join(rot(-35, 256, 300, R(100, y, 320, 18, RED)) for y in range(140, 500, 50)))
    s += PL([(226, 100), (286, 100), (276, 146), (236, 146)], "#14213d")
    return s


# ---------------------------------------------------------------- transport
def tiny_person(cx, cy, shirt=RED):
    return (limb(f"M{cx},{cy + 10} L{cx},{cy + 44}", shirt, 14) + limb(f"M{cx - 4},{cy + 44} L{cx - 14},{cy + 74} M{cx + 4},{cy + 44} L{cx + 14},{cy + 74}", NAVY, 8)
            + limb(f"M{cx},{cy + 16} L{cx - 24},{cy - 6} M{cx},{cy + 16} L{cx + 24},{cy - 6}", shirt, 8) + C(cx, cy, 13, SKIN))


def parachute():
    s = sky() + NS(E(80, 400, 60, 20, WHITE) + E(430, 440, 70, 22, WHITE))
    for x in (90, 170, 256, 342, 422):
        s += L(x, 200, 256, 340, 3)
    canopy = P("M70,210 Q90,60 256,56 Q422,60 442,210 Q400,190 358,210 Q316,190 256,210 Q196,190 154,210 Q112,190 70,210 Z")
    s += patterned("pc", canopy, RED, "".join(R(x, 40, 56, 200, c) for x, c in ((120, YELLOW), (228, WHITE), (336, YELLOW))))
    s += tiny_person(256, 350, BLUE)
    return s


def hot_air_balloon():
    s = sky() + NS(E(90, 120, 56, 20, WHITE) + E(420, 380, 60, 22, WHITE))
    shape = P("M256,40 Q400,40 400,190 Q400,280 300,340 L212,340 Q112,280 112,190 Q112,40 256,40 Z")
    s += patterned("hb", shape, RED, "".join(f'<path d="M{x},20 Q{x + (256 - x) * .1},200 {256 + (x - 256) * .25},360" fill="none" stroke="{c}" stroke-width="40"/>'
                                         for x, c in ((140, YELLOW), (256, YELLOW), (372, YELLOW))))
    s += L(214, 340, 220, 390, 5) + L(298, 340, 292, 390, 5)
    s += R(212, 384, 88, 60, "#a0522d", 8) + "".join(L(212, y, 300, y, 3) for y in (404, 424))
    return s


def sailboard():
    s = sky() + NS(C(410, 90, 40, YELLOW))
    s += water(350, "#4ea8de", "#2a7fc1")
    s += L(250, 360, 230, 70, 8)
    s += P("M236,80 Q360,180 330,350 L246,350 Z", "#ff006e")
    s += P("M236,80 Q300,140 304,220 L240,220 Z", YELLOW)
    s += P("M240,220 L304,220 Q300,290 330,350", extra='stroke-width="0"')
    s += L(246, 260, 320, 240, 8)
    s += P("M100,370 Q256,340 430,360 Q440,380 420,390 Q256,400 110,390 Q90,380 100,370 Z", WHITE)
    s += P("M140,382 L400,374", extra=f'stroke="#3a86ff" stroke-width="8"')
    return s


# ---------------------------------------------------------------- weather / nature
def earthquake():
    s = sky("#ffe8cc")
    s += P("M0,330 L240,330 L210,512 L0,512 Z", "#a98467") + P("M272,330 L512,330 L512,512 L250,512 Z", "#a98467")
    s += P("M240,330 L272,330 L256,370 L280,400 L250,440 L270,470 L250,512 L210,512 L232,470 L214,430 L240,400 L224,370 Z", OUT)
    s += rot(-12, 120, 330, R(70, 210, 120, 120, CREAM) + PL([(56, 220), (130, 160), (204, 220)], RED) + R(110, 270, 34, 60, BROWN))
    s += rot(10, 390, 330, R(330, 190, 110, 140, "#dee2e6") + "".join(R(346 + c * 34, 206 + r * 36, 22, 24, LBLUE, 2, 'stroke-width="4"') for c in range(3) for r in range(3)))
    s += P("M40,120 Q60,100 40,80 M70,130 Q100,100 70,70 M440,120 Q460,100 440,80 M470,130 Q500,100 470,70", extra='stroke-width="6"')
    s += P("M300,350 L330,380 M180,380 L150,410", extra='stroke-width="5"')
    return s


def tornado():
    s = sky("#c9d6df") + ground("#95d5b2", 420)
    for i in range(9):
        y = 70 + i * 40
        rx = 170 - i * 17
        x = 256 + 20 * math.sin(i * 0.8)
        s += E(x, y, rx, 22, "#8d99ae")
    s += P("M240,420 Q256,400 272,420", extra='stroke-width="6"')
    s += rot(30, 120, 220, R(110, 210, 30, 18, BROWN, 3)) + rot(-20, 400, 300, R(390, 290, 26, 14, BROWN, 3)) + PL([(380, 160), (400, 150), (396, 172)], GREEN)
    s += P("M60,300 Q90,290 110,300 M420,240 Q450,230 470,240", extra='stroke-width="5"')
    return s


def lightning():
    s = NS(R(0, 0, 512, 512, "#343a5e", 48))
    s += PL([(260, 200), (190, 330), (250, 330), (210, 470), (340, 290), (276, 290), (320, 200)], "#ffe066", 'stroke-width="8"')
    s += cloud_shape(256, 150, 1.25, "#6c757d")
    s += NS(PL([(150, 260), (130, 300), (150, 300)], "#ffe066") + PL([(380, 250), (360, 290), (380, 290)], "#ffe066"))
    return s


def storm():
    s = NS(R(0, 0, 512, 512, "#adb5bd", 48))
    s += "".join(L(x, y, x - 30, y + 60, 6, "#4ea8de") for x, y in ((120, 260), (180, 300), (240, 260), (300, 300), (360, 260), (420, 300), (150, 380), (270, 390), (390, 380)))
    s += P("M40,420 Q120,390 180,420 Q220,440 210,470", extra=f'stroke="{WHITE}" stroke-width="10"')
    s += P("M300,460 Q380,430 460,450", extra=f'stroke="{WHITE}" stroke-width="10"')
    s += cloud_shape(220, 150, 1.1, "#495057") + cloud_shape(360, 120, 0.8, "#6c757d")
    s += PL([(300, 220), (270, 290), (300, 290), (280, 350), (340, 270), (310, 270), (330, 220)], "#ffe066", 'stroke-width="6"')
    return s


def fog():
    s = sky("#e9ecef")
    s += P("M-10,380 Q140,280 300,340 Q420,380 522,320 L522,522 L-10,522 Z", "#95d5b2")
    s += pine(110, 340, 170, "#52b788") + pine(390, 320, 190, "#52b788") + pine(250, 380, 140, "#40916c")
    s += NS("".join(R(-20 + (i % 2) * 60, 140 + i * 70, 500, 46, WHITE, 23, 'opacity=".75"') for i in range(5)))
    return s


# ---------------------------------------------------------------- animals
def kangaroo():
    K = "#c8814b"
    s = shadow(240, 444, 170)
    s += limb("M160,380 Q80,400 50,440", K, 30)
    s += limb("M236,260 Q270,210 292,180", K, 56)
    s += E(220, 330, 90, 110, K)
    s += E(250, 350, 50, 70, "#e8b888", 'stroke="none"')
    s += P("M226,350 Q256,390 290,350", extra='stroke-width="6"') + C(258, 344, 18, K) + dot(264, 340, 4)
    s += E(200, 420, 70, 26, K) + E(300, 440, 50, 12, K)
    s += limb("M270,260 L310,300", K, 16)
    s += rot(30, 300, 170, E(300, 170, 56, 40, K))
    s += rot(-10, 270, 110, E(270, 110, 16, 42, K)) + rot(10, 298, 108, E(298, 108, 16, 42, K))
    s += dot(312, 160, 8) + E(348, 196, 10, 8, OUT)
    return s


def koala():
    G = "#9aa5b1"
    s = R(330, 0, 90, 512, "#a0522d", 0) + R(330, 0, 90, 512, "none")
    s += E(240, 350, 100, 100, G)
    s += E(240, 370, 54, 64, "#e9ecef", 'stroke="none"')
    s += limb("M300,320 L360,300", G, 30) + limb("M300,400 L360,410", G, 30)
    s += C(130, 140, 56, G) + C(350, 140, 56, G) + C(130, 140, 34, "#e9ecef", 'stroke="none"') + C(350, 140, 34, "#e9ecef", 'stroke="none"')
    s += C(240, 200, 100, G)
    s += E(240, 220, 30, 40, "#3d405b")
    s += eyes(240, 180, 54, 11)
    s += P("M400,100 Q440,60 470,80 Q440,110 400,100 Z", GREEN) + P("M410,200 Q460,180 480,210 Q440,230 410,200 Z", GREEN)
    return s


def parrot():
    s = limb("M60,420 L452,420", DBROWN, 18)
    s += PL([(220, 340), (200, 480), (240, 470), (250, 350)], "#3a86ff") + PL([(250, 340), (270, 480), (290, 460), (276, 340)], YELLOW)
    s += E(256, 260, 90, 130, RED)
    s += P("M200,220 Q170,320 230,380 Q280,330 250,230 Z", "#2a9d8f")
    s += P("M210,300 Q200,350 236,380", extra=f'stroke="#3a86ff" stroke-width="16"')
    s += C(270, 150, 66, RED)
    s += E(296, 140, 26, 30, WHITE, 'stroke="none"') + dot(300, 140, 9)
    s += P("M320,150 Q380,150 372,214 Q360,200 334,196 Z", "#e9ecef") + P("M334,196 Q350,200 360,214 Q340,214 330,206 Z", OUT)
    s += "".join(E(x, 424, 12, 8, "#6c757d") for x in (226, 250, 280))
    return s


def dolphin():
    s = sky() + water(380, "#4ea8de", "#2a7fc1")
    s += P("M90,380 Q130,160 330,120 Q400,110 440,150 Q420,160 400,156 Q350,170 300,200 Q200,270 170,380 Z", "#6c9bc6")
    s += P("M120,370 Q170,260 260,220 Q220,280 200,380 Z", "#cfe2f3", 'stroke="none"')
    s += PL([(250, 150), (230, 90), (300, 136)], "#6c9bc6")
    s += P("M240,240 L200,280 L260,262 Z", "#6c9bc6")
    s += dot(380, 148, 7) + P("M400,156 Q420,166 440,150", extra='stroke-width="5"')
    s += NS("".join(C(x, y, r, WHITE, 'opacity=".9"') for x, y, r in ((70, 360, 10), (190, 360, 12), (60, 330, 6), (210, 330, 7))))
    return s


def octopus():
    O = "#c77dff"
    s = water(440, "#90e0ef", "#4ea8de") if False else ""
    for i in range(8):
        x0 = 150 + i * 30
        side = -1 if i < 4 else 1
        s += limb(f"M{x0},300 Q{x0 + side * 30},380 {x0 + side * (40 + (i % 4) * 14)},420 Q{x0 + side * (70 + (i % 4) * 14)},450 {x0 + side * (60 + (i % 4) * 14)},470", O, 26)
    s += P("M140,300 Q130,80 256,76 Q382,80 372,300 Q256,330 140,300 Z", O)
    s += C(216, 220, 26, WHITE) + C(296, 220, 26, WHITE) + dot(220, 224, 12) + dot(292, 224, 12)
    s += smile(256, 270, 24, 16) + cheeks(256, 262, 70, 14)
    s += NS(C(200, 130, 12, "#e0aaff") + C(320, 150, 9, "#e0aaff") + C(260, 110, 7, "#e0aaff"))
    return s


def crab():
    Cr = "#e63946"
    s = shadow(256, 430, 170)
    for side in (1, -1):
        for i in range(3):
            y = 320 + i * 26
            s += P(f"M{256 + side * 100},{y} L{256 + side * 170},{y + 20} L{256 + side * 190},{y + 70}", extra='stroke-width="12"')
        s += limb(f"M{256 + side * 90},{270} L{256 + side * 150},{200}", Cr, 20)
        s += tr(256 + side * 160, 170, f'<g transform="scale({side} 1)">' + P("M-30,20 Q-50,-40 0,-60 Q40,-60 40,-20 L10,-10 Q20,-40 0,-40 Q-20,-30 -10,20 Z", Cr) + "</g>")
    s += E(256, 320, 120, 76, Cr)
    s += L(226, 260, 220, 200, 8) + L(286, 260, 292, 200, 8)
    s += C(220, 196, 18, WHITE) + C(292, 196, 18, WHITE) + dot(222, 198, 8) + dot(290, 198, 8)
    s += smile(256, 316, 30, 18) + NS(C(200, 300, 8, "#ff8fa3") + C(312, 300, 8, "#ff8fa3"))
    return s


def jellyfish():
    s = ""
    for i, x in enumerate(range(170, 350, 30)):
        s += P(f"M{x},250 Q{x + 20},300 {x},350 Q{x - 20},400 {x + 6},460", extra=f'stroke="#ff8fab" stroke-width="10"')
    s += limb("M220,250 Q200,330 230,380", "#ffc8dd", 20) + limb("M292,250 Q312,330 282,380", "#ffc8dd", 20)
    s += P("M120,260 Q120,80 256,80 Q392,80 392,260 Q370,240 346,262 Q322,240 300,262 Q278,240 256,262 Q234,240 212,262 Q190,240 166,262 Q142,240 120,260 Z", "#ffafcc")
    s += eyes(256, 190, 36, 10) + smile(256, 212, 18, 12)
    s += shine("M160,180 Q170,130 210,110")
    s += NS("".join(C(x, y, r, WHITE, 'opacity=".7"') for x, y, r in ((420, 120, 10), (440, 80, 6), (90, 340, 8))))
    return s


def squirrel():
    Sq = "#d2691e"
    s = shadow(256, 444, 140)
    s += P("M300,420 Q460,420 440,250 Q430,120 340,110 Q280,110 290,170 Q380,160 380,260 Q380,360 300,370 Z", "#e07a2a")
    s += E(250, 340, 70, 96, Sq)
    s += E(240, 360, 40, 64, "#f6c28b", 'stroke="none"')
    s += E(210, 432, 32, 14, Sq) + E(286, 432, 32, 14, Sq)
    s += E(236, 292, 26, 22, "#8b5a2b") + P("M214,282 Q236,262 258,282 Z", "#5e3a1a")
    s += limb("M210,300 L222,300 M262,300 L250,300", Sq, 14)
    s += C(230, 200, 60, Sq)
    s += PL([(194, 162), (190, 110), (222, 146)], Sq) + PL([(256, 150), (270, 104), (276, 156)], Sq)
    s += dot(214, 196, 8) + dot(254, 196, 8) + E(232, 222, 8, 6, OUT)
    s += cheeks(234, 216, 34, 9)
    return s


def canine(fur, chest, ear_inner, bg_extra=""):
    s = bg_extra + shadow(256, 444, 130)
    s += limb("M320,410 Q420,420 420,330", fur, 32)
    s += E(256, 360, 84, 84, fur)
    s += P("M256,290 Q210,330 222,420 L290,420 Q302,330 256,290 Z", chest, 'stroke="none"')
    s += E(220, 434, 26, 14, fur) + E(292, 434, 26, 14, fur)
    s += PL([(186, 170), (184, 80), (240, 140)], fur) + PL([(326, 170), (328, 80), (272, 140)], fur)
    s += NS(PL([(196, 154), (196, 104), (228, 140)], ear_inner) + PL([(316, 154), (316, 104), (284, 140)], ear_inner))
    s += P("M170,180 Q170,120 256,120 Q342,120 342,180 Q340,240 256,280 Q172,240 170,180 Z", fur)
    s += NS(P("M206,226 Q256,296 306,226 Q290,256 256,258 Q222,256 206,226 Z", chest))
    s += E(256, 252, 14, 10, OUT)
    s += eyes(256, 196, 34, 9)
    return s


def fox():
    s = canine("#e8702a", WHITE, OUT)
    s += C(418, 326, 16, WHITE)
    return s


def wolf():
    bg = NS(R(0, 0, 512, 512, NIGHT, 48) + C(400, 100, 50, "#fde68a") + R(0, 420, 512, 92, "#2d3a5e"))
    return canine("#8d99ae", "#dee2e6", "#495057", bg)


def bear():
    Br = "#8b5a2b"
    s = shadow(256, 444, 150)
    s += E(256, 350, 116, 100, Br)
    s += E(256, 370, 64, 64, "#c08552", 'stroke="none"')
    s += E(196, 430, 40, 20, Br) + E(316, 430, 40, 20, Br)
    s += limb("M170,320 Q160,380 200,400", Br, 34) + limb("M342,320 Q352,380 312,400", Br, 34)
    s += C(176, 120, 34, Br) + C(336, 120, 34, Br) + C(176, 120, 16, "#c08552", 'stroke="none"') + C(336, 120, 16, "#c08552", 'stroke="none"')
    s += C(256, 190, 90, Br)
    s += E(256, 230, 42, 32, "#c08552")
    s += E(256, 216, 16, 11, OUT) + P("M256,226 L256,240 M240,246 Q256,254 272,246", extra='stroke-width="5"')
    s += eyes(256, 180, 36, 9)
    return s


def deer():
    D = "#b5764a"
    s = shadow(240, 436, 160)
    s += P("M118,230 L104,250", extra='stroke-width="0"')
    for x in (140, 172, 290, 320):
        s += R(x, 290, 20, 130, D, 8) + R(x - 2, 412, 24, 16, OUT, 4)
    s += E(232, 270, 120, 56, D)
    s += NS("".join(C(x, y, 7, CREAM) for x, y in ((180, 250), (210, 240), (240, 256), (270, 244), (200, 270), (300, 250))))
    s += E(112, 250, 14, 18, WHITE)
    s += PL([(310, 250), (330, 150), (376, 160), (356, 270)], D)
    s += rot(30, 384, 172, E(384, 172, 48, 26, D))
    s += P("M352,140 L340,90 L310,70 M340,90 L352,60 M346,110 L320,104", extra=f'stroke="{DBROWN}" stroke-width="10"')
    s += P("M372,136 L390,86 L420,66 M390,86 L382,56 M386,104 L410,100", extra=f'stroke="{DBROWN}" stroke-width="10"')
    s += rot(-30, 336, 150, E(336, 150, 22, 10, D))
    s += dot(378, 162, 7) + dot(420, 196, 6)
    return s


# ---------------------------------------------------------------- tools
def screwdriver():
    s = shadow(256, 440, 150)
    g = (R(80, 226, 150, 60, RED, 26) + "".join(L(x, 232, x, 280, 5, DRED) for x in (110, 140, 170, 200))
         + R(226, 238, 36, 36, OUT, 6) + R(260, 246, 160, 20, GREY, 4) + PL([(420, 244), (446, 252), (446, 260), (420, 268)], GREY))
    s += rot(-30, 256, 256, g)
    s += R(380, 330, 30, 24, GREY, 4) + PL([(386, 354), (404, 354), (395, 400)], GREY)
    return s


def drill():
    s = shadow(256, 450, 150)
    s += P("M90,160 Q90,120 130,120 L340,120 Q370,120 370,160 L370,230 Q370,250 340,250 L280,250 L250,380 L170,380 L190,250 L130,250 Q90,250 90,200 Z", "#ffb703")
    s += R(150, 370, 130, 70, OUT, 12)
    s += R(370, 150, 50, 70, DGREY, 8) + R(420, 172, 70, 26, GREY, 4)
    s += P("M430,180 L490,178 M430,190 L490,192", extra='stroke-width="3"')
    s += R(210, 262, 20, 40, OUT, 6)
    s += R(120, 150, 150, 40, "#fb8500", 10, 'stroke="none"')
    return s


def saw():
    s = shadow(256, 420, 190)
    teeth = " ".join(f"L{x},{356} L{x + 10},{340}" for x in range(150, 450, 20))
    s += P(f"M140,240 L450,290 L450,340 {teeth} L140,340 Z", "#ced4da")
    s += shine("M170,260 L420,298")
    s += P("M40,200 Q40,170 80,170 L150,180 Q170,190 170,220 L170,360 Q170,380 150,380 L80,380 Q40,380 40,340 Z", "#c08552")
    s += R(76, 230, 56, 100, "#f1e0c5", 20)
    s += C(154, 240, 7, GREY) + C(154, 320, 7, GREY)
    return s


def wrench():
    s = shadow(256, 440, 150)
    g = (R(130, 236, 260, 40, GREY, 20)
         + P("M380,200 Q440,190 460,230 L420,240 L420,272 L460,282 Q440,322 380,312 Q350,256 380,200 Z", GREY)
         + C(110, 256, 50, GREY) + C(110, 256, 22, CREAM)
         + R(300, 246, 50, 20, DGREY, 6))
    s += rot(-35, 256, 256, g)
    return s


# ---------------------------------------------------------------- home
def vacuum_cleaner():
    s = shadow(256, 450, 190)
    s += limb("M150,320 Q110,200 240,170 L340,140", "#495057", 16)
    s += L(340, 140, 410, 400, 14) + L(340, 140, 410, 400, 6, GREY)
    s += R(360, 396, 110, 30, OUT, 10)
    s += E(170, 350, 110, 80, RED)
    s += R(90, 330, 140, 30, DRED, 10, 'stroke="none"') + E(170, 350, 110, 80, "none")
    s += C(110, 420, 18, OUT) + C(230, 420, 18, OUT)
    s += C(220, 320, 14, WHITE)
    return s


def washing_machine():
    s = shadow(256, 450, 160)
    s += R(110, 70, 292, 370, WHITE, 18)
    s += L(110, 140, 402, 140, 6)
    s += R(140, 92, 100, 30, LBLUE, 6, 'stroke-width="5"') + C(310, 106, 16, GREY) + C(360, 106, 16, GREY)
    s += C(256, 290, 112, "#adb5bd") + C(256, 290, 86, "#90e0ef")
    s += NS(P("M180,300 Q220,260 256,300 T332,300 L332,360 L180,360 Z", "#4ea8de") + C(230, 320, 16, RED) + C(290, 330, 14, YELLOW))
    s += C(256, 290, 86, "none") + shine("M200,240 Q220,220 250,214")
    return s


def iron():
    s = shadow(256, 420, 180)
    s += NS("".join(C(x, y, r, "#e9ecef") for x, y, r in ((380, 140, 20), (410, 110, 26), (440, 80, 18))))
    s += P("M80,380 L430,380 Q440,250 330,240 L190,240 Q110,250 80,380 Z", "#3a86ff")
    s += R(76, 370, 360, 26, GREY, 8)
    s += limb("M200,240 L200,170 L360,170 L380,240", "#1d3557", 22)
    s += C(270, 300, 18, WHITE) + NS(C(270, 300, 7, RED))
    s += P("M436,330 Q470,330 480,380", extra='stroke-width="6"')
    return s


def hairdryer():
    s = shadow(240, 450, 140)
    s += P("M150,130 Q80,130 80,200 Q80,270 150,270 L340,250 L340,150 Z", "#f4a6c1")
    s += R(340, 160, 50, 80, "#e5739f", 8)
    s += C(150, 200, 50, "#e5739f") + C(150, 200, 28, OUT) + NS(C(150, 200, 12, GREY))
    s += P("M190,260 L250,260 L240,420 Q230,440 210,440 L196,440 Q180,440 180,420 Z", "#f4a6c1")
    s += R(200, 300, 24, 40, WHITE, 6)
    s += P("M410,170 Q440,160 470,170 M410,200 Q450,200 490,200 M410,230 Q440,240 470,230", extra=f'stroke="{GREY}" stroke-width="7"')
    s += limb("M210,440 Q220,480 280,470", OUT, 2)
    return s


DRAW_B1 = {
    "skyscraper": skyscraper, "tunnel": tunnel, "harbour": harbour, "factory": factory, "museum": museum,
    "library": library, "stadium": stadium, "hospital": hospital, "pharmacy": pharmacy, "bakery": bakery,
    "supermarket": supermarket, "restaurant": restaurant, "post-office": post_office,
    "police-station": police_station, "fire-station": fire_station,
    "laboratory": laboratory, "microscope": microscope, "telescope": telescope, "satellite": satellite,
    "robot": robot, "solar-panel": solar_panel, "wind-turbine": wind_turbine, "recycling-bin": recycling_bin,
    "wheelchair": wheelchair, "crutches": crutches, "bandage": bandage, "thermometer": thermometer,
    "stethoscope": stethoscope_, "syringe": syringe, "pills": pills,
    "jewellery": jewellery, "necklace": necklace, "ring": ring_, "bracelet": bracelet, "perfume": perfume,
    "pyjamas": pyjamas, "raincoat": raincoat, "boots": boots, "sandals": sandals, "belt": belt, "tie": tie,
    "parachute": parachute, "hot-air-balloon": hot_air_balloon, "sailboard": sailboard,
    "earthquake": earthquake, "tornado": tornado, "lightning": lightning, "storm": storm, "fog": fog,
    "kangaroo": kangaroo, "koala": koala, "parrot": parrot, "dolphin": dolphin, "octopus": octopus,
    "crab": crab, "jellyfish": jellyfish, "squirrel": squirrel, "fox": fox, "wolf": wolf, "bear": bear, "deer": deer,
    "screwdriver": screwdriver, "drill": drill, "saw": saw, "wrench": wrench,
    "vacuum-cleaner": vacuum_cleaner, "washing-machine": washing_machine, "iron": iron, "hairdryer": hairdryer,
}

art.DRAW.update(DRAW_B1)
art.CATEGORY_BG.update({"science": "#e7f0ff", "health": "#e6fcf5", "tools": "#fff4e6"})
art.BG_OVERRIDE.update({"octopus": "#bde0fe", "jellyfish": "#bde0fe", "koala": "#e9f5db"})
