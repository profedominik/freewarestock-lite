"""A2 illustrations. Same style and helpers as art.py; registers into art.DRAW."""
import math

import art
from art import (OUT, SW, SKIN, SKIN2, HAIR, BLONDE, RED, DRED, BLUE, NAVY, LBLUE, SKY, GREEN, DGREEN,
                 LGREEN, YELLOW, ORANGE, DORANGE, PINK, PURPLE, BROWN, DBROWN, TAN, GREY, DGREY, WHITE,
                 CREAM, NIGHT, C, E, R, P, PL, L, NS, dot, limb, ring, merged, rot, tr, shadow, shine,
                 scallop, star_pts, eyes, smile, cheeks, person, wheel, cloud_shape, plane)

SAND = "#f4c27a"
GOLD = "#f2b134"


def nf(shape):
    """drop explicit white fills so a wrapping <g fill> applies"""
    return shape.replace(f'fill="{WHITE}"', "")


def clip(cid, shape, content):
    return f'<clipPath id="{cid}">{shape}</clipPath><g clip-path="url(#{cid})" stroke="none">{content}</g>'


def patterned(cid, body, fill, content):
    """silhouette filled with `fill`, overlaid with `content` clipped to it, then outlined"""
    body = nf(body)
    return f'<g fill="{fill}">{body}</g>' + clip(cid, body, content) + f'<g fill="none">{body}</g>'


def stripes_v(x0, x1, step, color, w, y0=0, y1=512, wave=20):
    return "".join(f'<path d="M{x},{y0} Q{x + wave},{(y0 + y1) / 2} {x - wave / 2},{y1}" fill="none" stroke="{color}" stroke-width="{w}"/>'
                   for x in range(x0, x1, step))


def water(y=380, color=LBLUE, wave=BLUE):
    s = R(0, y, 512, 512 - y, color, 0, 'stroke="none"')
    s += P(f"M0,{y + 12} " + " ".join(f"Q{x + 32},{y - 4} {x + 64},{y + 12}" for x in range(0, 512, 64)),
           extra=f'stroke="{wave}" stroke-width="6"')
    return s


def sky(color=SKY):
    return NS(R(0, 0, 512, 512, color, 48))


# ---------------------------------------------------------------- animals
def giraffe():
    G, S = "#f6c453", "#b8742b"
    s = shadow(220, 438, 150)
    s += limb("M100,320 Q84,360 92,390", G, 8)
    for x in (122, 154, 236, 266):
        s += R(x, 340, 22, 90, G, 8) + R(x - 2, 420, 26, 16, OUT, 4)
    s += E(196, 326, 104, 54, G)
    s += PL([(232, 300), (292, 318), (370, 142), (328, 116)], G)
    s += L(344, 94, 338, 66, 7) + C(338, 62, 8, S) + L(366, 92, 368, 64, 7) + C(368, 60, 8, S)
    s += rot(-30, 326, 104, E(326, 104, 18, 9, G))
    s += rot(25, 372, 128, E(372, 128, 54, 30, G))
    s += NS("".join(E(x, y, 13, 10, S) for x, y in
                    [(150, 316), (200, 302), (246, 330), (170, 346), (118, 330), (210, 340)]))
    s += NS("".join(C(x, y, 10, S) for x, y in [(284, 270), (306, 222), (330, 172), (296, 300)]))
    s += dot(372, 116, 7) + dot(414, 146, 4)
    return s


def zebra():
    s = shadow(250, 430, 160)
    s += limb("M126,246 Q86,300 104,380", OUT, 14)
    body = (E(244, 268, 124, 62) + PL([(318, 250), (342, 144), (394, 148), (372, 280)])
            + rot(40, 402, 168, E(402, 168, 58, 30)) + "".join(R(x, 296, 26, 112, rx=8) for x in (156, 192, 296, 330)))
    s += f'<g fill="{WHITE}">{nf(body)}</g>'
    s += clip("zb", body, stripes_v(110, 440, 32, OUT, 13, 100, 420, 24))
    s += f'<g fill="none">{nf(body)}</g>'
    for x in (156, 192, 296, 330):
        s += R(x - 2, 404, 30, 20, OUT, 5)
    s += PL([(354, 128), (362, 94), (380, 128)], WHITE)
    s += limb("M338,140 Q322,196 314,248", OUT, 16)
    s += E(440, 200, 18, 14, "#555")
    s += C(380, 150, 9, WHITE) + dot(380, 150, 6)
    return s


def monkey():
    M, F = "#8d5a3b", "#f1c6a0"
    s = shadow(256, 444, 130)
    s += limb("M320,400 Q420,410 410,320 Q404,270 370,280", M, 16)
    s += E(256, 350, 86, 90, M)
    s += E(256, 370, 50, 60, F, 'stroke="none"')
    s += limb("M196,300 Q170,360 200,400", M, 26) + limb("M316,300 Q342,360 312,400", M, 26)
    s += E(212, 432, 32, 16, M) + E(300, 432, 32, 16, M)
    s += C(166, 196, 34, M) + C(346, 196, 34, M) + C(166, 196, 18, F, 'stroke="none"') + C(346, 196, 18, F, 'stroke="none"')
    s += C(256, 190, 86, M)
    s += P("M256,170 Q220,130 196,160 Q176,200 200,240 Q220,272 256,272 Q292,272 312,240 Q336,200 316,160 Q292,130 256,170 Z", F)
    s += eyes(256, 186, 28, 10)
    s += dot(248, 220, 4) + dot(264, 220, 4) + smile(256, 238, 26, 18)
    return s


def penguin():
    s = NS(R(0, 400, 512, 112, WHITE))
    s += shadow(256, 440, 120)
    s += E(206, 436, 34, 14, ORANGE) + E(306, 436, 34, 14, ORANGE)
    s += rot(20, 158, 300, E(158, 300, 26, 80, "#2b2d42")) + rot(-20, 354, 300, E(354, 300, 26, 80, "#2b2d42"))
    s += E(256, 286, 108, 150, "#3d405b")
    s += P("M256,170 Q200,170 196,230 Q172,330 200,400 Q256,440 312,400 Q340,330 316,230 Q312,170 256,170 Z", WHITE)
    s += C(226, 214, 12, WHITE) + dot(228, 214, 8) + C(286, 214, 12, WHITE) + dot(284, 214, 8)
    s += PL([(236, 240), (276, 240), (256, 270)], ORANGE)
    s += cheeks(256, 262, 52, 12)
    return s


def snake():
    d = "M80,420 C200,440 340,430 344,360 C348,290 170,310 170,240 C170,170 290,150 336,180"
    s = shadow(240, 440, 170)
    s += limb(d, GREEN, 46)
    s += f'<path d="{d}" fill="none" stroke="{YELLOW}" stroke-width="22" stroke-dasharray="2 40" stroke-linecap="round"/>'
    s += P("M392,190 L426,196 L440,186 M426,196 L438,210", extra=f'stroke="{RED}" stroke-width="5"')
    s += rot(15, 360, 184, E(360, 184, 46, 32, GREEN))
    s += C(356, 166, 10, WHITE) + dot(358, 166, 5)
    return s


def turtle():
    s = shadow(256, 410, 190)
    s += E(160, 380, 34, 22, LGREEN) + E(350, 380, 34, 22, LGREEN) + PL([(96, 350), (66, 364), (100, 370)], LGREEN)
    s += C(428, 300, 44, LGREEN) + dot(440, 290, 7) + smile(436, 312, 14, 8, 5)
    s += P("M100,350 Q110,170 256,170 Q402,170 412,350 Z", GREEN)
    s += R(92, 340, 328, 30, "#b7e4c7", 14)
    s += PL([(220, 220), (292, 220), (318, 270), (292, 320), (220, 320), (194, 270)], "#40916c")
    s += P("M220,220 L190,180 M292,220 L322,180 M318,270 L396,280 M194,270 L116,280 M220,320 L200,344 M292,320 L312,344",
           extra='stroke-width="6"')
    return s


def whale():
    s = water(400)
    s += P("M186,130 Q170,90 150,96 M186,130 Q200,80 226,90 M186,130 L186,84", extra=f'stroke="#4ea8de" stroke-width="10"')
    s += P("M396,280 Q440,250 472,200 Q486,240 464,262 Q492,282 480,316 Q440,300 396,300 Z", "#3a6ea5")
    s += P("M70,290 Q76,160 240,156 Q390,156 410,280 Q414,360 330,372 L160,372 Q72,364 70,290 Z", "#4a7fc1")
    s += P("M90,320 Q180,350 380,330 Q350,372 300,372 L160,372 Q110,366 90,320 Z", "#bcd7f0")
    s += P("M110,320 L130,360 M150,330 L162,368 M190,336 L198,372", extra='stroke-width="4" opacity=".4"')
    s += dot(150, 270, 9) + P("M96,300 Q130,312 170,304", extra='stroke-width="6"')
    return s


def shark():
    Gr = "#8d99ae"
    s = water(440, "#a9d6f5", "#5aa9e6")
    s += PL([(240, 214), (296, 120), (322, 212)], Gr)
    s += P("M56,280 Q160,200 300,206 Q400,212 438,250 L488,184 L470,266 L490,352 L430,296 Q350,338 200,332 Q100,322 56,280 Z", Gr)
    s += P("M70,290 Q160,330 300,330 Q380,326 420,300 Q350,338 200,334 Q110,326 70,290 Z", WHITE, 'stroke="none"')
    s += PL([(220, 320), (244, 396), (286, 324)], Gr)
    s += dot(130, 258, 9)
    s += P("M180,250 Q186,270 180,290 M200,248 Q206,268 200,288 M220,246 Q226,266 220,286", extra='stroke-width="5"')
    s += P("M76,292 Q110,306 146,298", extra='stroke-width="6"')
    s += PL([(96, 298), (104, 312), (112, 300)], WHITE, 'stroke-width="3"') + PL([(118, 302), (126, 314), (134, 302)], WHITE, 'stroke-width="3"')
    return s


def owl():
    O = "#a47148"
    s = limb("M60,420 L452,420", DBROWN, 20)
    s += PL([(166, 150), (180, 80), (220, 130)], O) + PL([(346, 150), (332, 80), (292, 130)], O)
    s += E(256, 280, 120, 150, O)
    s += E(256, 320, 76, 96, CREAM, 'stroke="none"')
    for y in (280, 320, 360):
        for x in (226, 256, 286):
            s += P(f"M{x - 10},{y} Q{x},{y + 12} {x + 10},{y}", extra=f'stroke="{TAN}" stroke-width="5"')
    s += rot(12, 150, 300, E(150, 300, 32, 86, "#7f5539")) + rot(-12, 362, 300, E(362, 300, 32, 86, "#7f5539"))
    s += C(206, 200, 46, ORANGE) + C(306, 200, 46, ORANGE)
    s += C(206, 200, 32, WHITE) + C(306, 200, 32, WHITE) + dot(210, 202, 16) + dot(302, 202, 16)
    s += PL([(242, 236), (270, 236), (256, 262)], YELLOW)
    s += "".join(E(x, 424, 12, 8, ORANGE) for x in (210, 232, 280, 302))
    return s


def bee():
    s = P("M60,420 Q120,360 160,400 Q200,440 230,380", extra=f'stroke="{DGREY}" stroke-width="5" stroke-dasharray="12 14"')
    s += rot(-20, 220, 170, E(220, 170, 56, 80, "#dff3ff")) + rot(20, 300, 170, E(300, 170, 56, 80, "#dff3ff"))
    body = E(270, 290, 130, 92)
    s += f'<g fill="{YELLOW}">{nf(body)}</g>'
    s += clip("bb", body, "".join(R(x, 180, 34, 220, OUT) for x in (210, 274, 338)))
    s += f'<g fill="none">{nf(body)}</g>'
    s += PL([(398, 280), (440, 292), (398, 304)], OUT)
    s += C(150, 270, 66, OUT)
    s += C(130, 256, 15, WHITE, 'stroke="none"') + C(172, 256, 15, WHITE, 'stroke="none"')
    s += dot(132, 258, 7) + dot(170, 258, 7)
    s += P("M130,296 Q150,312 172,296", extra=f'stroke="{WHITE}" stroke-width="6"')
    s += P("M130,210 Q110,150 90,140 M166,208 Q176,150 200,136", extra='stroke-width="7"') + C(90, 140, 10, OUT) + C(200, 136, 10, OUT)
    return s


def spider():
    s = L(256, 0, 256, 200, 4, DGREY)
    s += P("M0,80 L120,0 M0,40 L60,0 M0,120 L170,0", extra=f'stroke="{GREY}" stroke-width="3"')
    s += P("M20,70 Q60,60 70,26 M34,100 Q100,90 118,40", extra=f'stroke="{GREY}" stroke-width="3"')
    for side in (1, -1):
        for i, (dy, ang) in enumerate(((-20, -40), (0, -10), (20, 20), (40, 50))):
            kx = 256 + side * 120
            ky = 260 + dy - 40
            fx = 256 + side * 190
            fy = 300 + dy + ang
            s += P(f"M{256 + side * 40},{280 + dy} L{kx},{ky} L{fx},{fy}", extra='stroke-width="12"')
    s += E(256, 310, 76, 70, "#3d405b")
    s += C(256, 226, 46, "#3d405b")
    s += C(238, 220, 14, WHITE) + C(274, 220, 14, WHITE) + dot(240, 222, 7) + dot(272, 222, 7)
    s += smile(256, 246, 14, 8, 5)
    s += NS(E(256, 320, 26, 34, PURPLE, 'opacity=".7"'))
    return s


def camel():
    s = NS(R(0, 400, 512, 112, SAND)) + NS(C(420, 100, 40, YELLOW))
    s += shadow(240, 436, 160)
    s += limb("M110,300 Q96,340 104,370", TAN, 8)
    for x in (136, 168, 284, 316):
        s += R(x, 316, 22, 110, TAN, 8) + R(x - 2, 418, 26, 14, DBROWN, 4)
    s += P("M106,320 Q100,250 150,240 Q180,150 224,226 Q256,150 296,226 Q346,236 356,300 Q356,336 326,336 L136,336 Q106,336 106,320 Z", TAN)
    s += limb("M340,290 Q396,260 392,186", TAN, 40)
    s += rot(10, 420, 172, E(420, 172, 46, 26, TAN))
    s += rot(-20, 392, 150, E(392, 150, 10, 16, TAN))
    s += dot(412, 160, 6) + P("M448,182 Q456,186 460,180", extra='stroke-width="5"')
    return s


# ---------------------------------------------------------------- places
def bridge():
    s = sky()
    s += water(360, "#7ec8e3", BLUE)
    s += NS(R(0, 350, 70, 162, GREEN) + R(442, 350, 70, 162, GREEN))
    s += P("M40,220 L472,220 L472,430 L404,430 Q404,300 256,300 Q108,300 108,430 L40,430 Z", "#c9a27e")
    s += P("M40,220 L472,220 L472,246 L40,246 Z", "#a98467")
    for x in range(56, 472, 40):
        s += R(x, 180, 12, 40, "#a98467", 3)
    s += L(40, 184, 472, 184, 8)
    s += P("M70,280 L130,280 M180,260 L240,260 M300,260 L360,260 M410,280 L460,280", extra='stroke-width="4" opacity=".4"')
    return s


def castle():
    St, Dk = "#c0c7d1", "#9aa5b1"
    s = sky() + NS(R(0, 420, 512, 92, GREEN))
    for x in (90, 344):
        s += PL([(x - 10, 160), (x + 39, 70), (x + 88, 160)], RED)
        s += L(x + 39, 70, x + 39, 40, 5) + PL([(x + 39, 40), (x + 70, 50), (x + 39, 60)], YELLOW, 'stroke-width="5"')
    s += R(156, 240, 200, 190, St)
    for x in range(156, 356, 40):
        s += R(x, 220, 24, 24, St)
    s += R(80, 160, 98, 270, St) + R(334, 160, 98, 270, St)
    s += P("M216,430 L216,350 Q256,300 296,350 L296,430 Z", DBROWN)
    s += L(256, 330, 256, 430, 5)
    for x, y in ((112, 210), (112, 300), (366, 210), (366, 300), (230, 270), (282, 270)):
        s += P(f"M{x},{y + 40} L{x},{y + 12} Q{x + 12},{y} {x + 24},{y + 12} L{x + 24},{y + 40} Z", NAVY)
    s += NS("".join(R(x, y, 22, 10, Dk) for x, y in ((190, 380), (320, 260), (100, 380), (380, 360))))
    return s


def pine(x, y, h, c):
    w = h * 0.45
    return (R(x - 10, y - 10, 20, 34, BROWN, 3)
            + PL([(x - w, y), (x, y - h * 0.6), (x + w, y)], c)
            + PL([(x - w * 0.8, y - h * 0.35), (x, y - h * 0.9), (x + w * 0.8, y - h * 0.35)], c)
            + PL([(x - w * 0.55, y - h * 0.7), (x, y - h * 1.15), (x + w * 0.55, y - h * 0.7)], c))


def forest():
    s = sky("#dff3e4") + NS(R(0, 400, 512, 112, "#74c69d"))
    s += pine(110, 360, 200, "#40916c") + pine(400, 350, 210, "#40916c")
    s += pine(256, 400, 280, DGREEN)
    s += pine(170, 440, 160, GREEN) + pine(350, 450, 170, GREEN)
    return s


def desert():
    s = sky("#ffe8c2") + NS(C(400, 110, 48, YELLOW))
    s += P("M-10,360 Q120,300 260,350 Q380,390 520,330 L520,520 L-10,520 Z", SAND)
    s += P("M-10,430 Q160,390 300,430 Q420,460 520,420 L520,520 L-10,520 Z", "#e9a95c")
    cact = (R(220, 170, 64, 250, rx=32) + R(150, 290, 100, 38, rx=19) + R(150, 220, 38, 100, rx=19)
            + R(262, 260, 100, 38, rx=19) + R(324, 190, 38, 100, rx=19))
    s += merged(cact, "#52b788")
    s += P("M252,200 L252,400 M169,240 L169,300 M343,210 L343,270", extra=f'stroke="{DGREEN}" stroke-width="5"')
    return s


def island():
    s = sky()
    s += water(330, "#4ea8de", "#2a7fc1")
    s += P("M100,350 Q256,240 412,350 Z", SAND)
    s += limb("M256,320 Q240,240 280,150", "#a0522d", 22)
    for d in ("M280,150 Q220,110 160,150 Q220,130 280,160", "M280,150 Q340,100 400,140 Q340,130 280,160",
              "M280,150 Q240,170 210,230 Q250,180 284,160", "M280,150 Q330,170 360,230 Q320,180 278,160",
              "M280,150 Q280,90 250,70 Q290,100 286,152"):
        s += P(d + " Z", GREEN)
    s += C(270, 166, 12, DBROWN) + C(292, 166, 12, DBROWN)
    s += NS(E(100, 110, 50, 18, WHITE) + E(400, 70, 40, 14, WHITE))
    return s


def volcano():
    s = sky("#ffe0d1")
    s += cloud_shape(256, 90, 0.75, "#adb5bd")
    s += PL([(30, 440), (196, 170), (316, 170), (482, 440)], "#7f5539")
    s += P("M196,170 L316,170 L300,200 Q280,250 270,210 Q256,280 240,215 Q226,250 212,200 Z", DORANGE)
    s += NS(P("M226,180 L286,180 L278,190 L234,190 Z", YELLOW))
    s += NS(R(0, 430, 512, 82, "#6c584c"))
    return s


def lighthouse():
    s = sky("#d0e7ff")
    s += NS(PL([(256, 110), (40, 40), (40, 180)], "#fff3b0", 'opacity=".9"') + PL([(256, 110), (472, 40), (472, 180)], "#fff3b0", 'opacity=".9"'))
    s += water(390)
    s += P("M140,420 Q160,370 210,370 L310,370 Q370,370 380,420 Z", DGREY)
    tower = PL([(208, 380), (226, 150), (286, 150), (304, 380)])
    s += f'<g fill="{WHITE}">{nf(tower)}</g>'
    s += clip("lh", tower, "".join(R(200, y, 120, 40, RED) for y in (150, 230, 310)))
    s += f'<g fill="none">{nf(tower)}</g>'
    s += R(212, 130, 88, 22, OUT, 4)
    s += R(226, 84, 60, 48, YELLOW, 4) + L(256, 84, 256, 132, 5)
    s += PL([(216, 86), (256, 50), (296, 86)], RED)
    s += P("M246,380 L246,340 Q256,326 266,340 L266,380 Z", DBROWN)
    return s


def farm():
    s = sky() + NS(R(0, 380, 512, 132, "#95d5b2"))
    s += R(370, 160, 70, 240, "#adb5bd", 4) + P("M370,160 Q405,110 440,160 Z", "#6c757d")
    s += R(100, 220, 250, 190, RED)
    s += PL([(80, 230), (225, 120), (370, 230)], DRED)
    s += R(176, 290, 98, 120, WHITE) + L(176, 290, 274, 410, 8) + L(274, 290, 176, 410, 8)
    s += R(200, 180, 50, 40, WHITE) + L(225, 180, 225, 220, 6)
    for x in range(20, 512, 40):
        s += R(x, 400, 10, 50, "#e9c46a", 3, 'stroke-width="5"')
    s += L(10, 414, 502, 414, 6) + L(10, 436, 502, 436, 6)
    return s


def tent():
    s = NS(R(0, 0, 512, 512, NIGHT, 48))
    s += NS("".join(PL(star_pts(x, y, r, r * .45), "#fff4b8") for x, y, r in ((90, 90, 14), (400, 70, 10), (440, 170, 12), (180, 60, 8))))
    s += NS(C(330, 110, 30, "#fde68a"))
    s += NS(R(0, 400, 512, 112, "#2d6a4f"))
    s += PL([(256, 140), (60, 420), (452, 420)], ORANGE)
    s += PL([(256, 140), (196, 420), (316, 420)], DORANGE)
    s += PL([(256, 220), (216, 420), (296, 420)], "#3a2a1a")
    s += L(256, 140, 256, 110, 8) + L(60, 420, 30, 440, 5) + L(452, 420, 482, 440, 5)
    return s


def beach():
    s = sky() + NS(C(90, 90, 40, YELLOW))
    s += water(240, "#4ea8de", "#2a7fc1")
    s += P("M0,330 Q140,290 300,320 Q420,340 512,300 L512,512 L0,512 Z", SAND)
    s += L(330, 210, 360, 430, 8)
    s += P("M200,240 Q320,120 460,190 Z", RED)
    s += P("M260,206 Q320,140 360,160 L330,210 Z", WHITE, 'stroke="none"') + P("M396,170 Q440,180 460,190 L360,230 Z", WHITE, 'stroke="none"')
    s += P("M200,240 Q320,120 460,190 Z", "none")
    s += C(150, 400, 40, YELLOW) + P("M110,400 Q150,380 190,400 M150,360 L150,440", extra=f'stroke="{RED}" stroke-width="10"')
    s += C(150, 400, 40, "none")
    s += P("M410,440 Q430,410 450,440 Z", PINK, 'stroke-width="5"')
    return s


# ---------------------------------------------------------------- transport
def airport():
    s = sky() + NS(R(0, 380, 512, 132, "#95d5b2"))
    s += P("M0,410 L512,410 L512,470 L0,470 Z", DGREY)
    s += P("M20,440 L492,440", extra=f'stroke="{WHITE}" stroke-width="6" stroke-dasharray="30 24"')
    s += R(390, 190, 46, 220, "#e9ecef")
    s += PL([(366, 140), (460, 140), (450, 196), (376, 196)], "#adb5bd")
    s += R(380, 152, 66, 30, LBLUE, 3) + L(413, 152, 413, 182, 4)
    s += R(400, 120, 26, 20, RED, 3) + L(413, 120, 413, 96, 5)
    s += tr(-40, 60, plane(), 0.68)
    return s


def ambulance():
    s = shadow(256, 396, 200)
    s += R(60, 150, 280, 220, WHITE, 18)
    s += P("M340,200 L400,200 Q420,200 432,222 L456,280 L456,370 L340,370 Z", WHITE)
    s += PL([(356, 216), (398, 216), (430, 280), (356, 280)], LBLUE)
    s += R(60, 300, 396, 24, RED, 0)
    s += NS("".join(rot(a, 190, 230, R(176, 186, 28, 88, "#1f6feb", 6)) for a in (0, 60, 120)))
    s += R(170, 130, 30, 22, "#1f6feb", 6) + R(212, 130, 30, 22, RED, 6)
    s += C(448, 300, 8, YELLOW)
    s += wheel(140, 372, 40) + wheel(380, 372, 40)
    return s


def tractor():
    s = shadow(256, 432, 200)
    s += R(340, 120, 18, 90, OUT, 4)
    s += P("M90,330 L90,250 L190,250 L200,150 L330,150 L340,250 L430,262 L440,330 Z", "#2a9d8f")
    s += PL([(214, 166), (316, 166), (322, 246), (210, 246)], LBLUE)
    s += R(380, 280, 40, 18, YELLOW, 4, 'stroke-width="5"')
    s += C(170, 340, 92, OUT) + C(170, 340, 44, YELLOW)
    s += C(392, 370, 56, OUT) + C(392, 370, 26, YELLOW)
    return s


def submarine():
    s = sky("#9fd3f5")
    s += NS(R(0, 440, 512, 72, "#e9c46a"))
    s += P("M90,440 Q100,400 110,440 M400,440 Q420,390 430,440 M420,440 Q440,410 450,440", extra=f'stroke="{GREEN}" stroke-width="8"')
    s += R(250, 100, 14, 70, DGREY) + R(250, 96, 50, 14, DGREY)
    s += R(206, 150, 120, 70, YELLOW, 20)
    s += P("M80,280 L50,240 L50,320 Z", ORANGE) + E(66, 280, 10, 40, DGREY)
    s += E(260, 280, 180, 84, YELLOW)
    for x in (180, 260, 340):
        s += C(x, 276, 24, DGREY) + C(x, 276, 15, LBLUE, 'stroke="none"')
    s += NS("".join(C(x, y, r, WHITE, 'opacity=".8"') for x, y, r in ((40, 200, 10), (30, 160, 7), (46, 124, 5), (470, 160, 8))))
    return s


def taxi():
    s = shadow(262, 382, 180)
    s += R(230, 160, 60, 26, YELLOW, 6)
    s += P("M84,340 L84,290 Q86,262 116,258 L170,252 L212,198 Q222,186 242,186 L328,186 "
           "Q348,186 360,200 L398,252 L414,254 Q442,260 442,290 L442,340 Z", YELLOW)
    s += PL([(188, 250), (224, 204), (282, 204), (282, 250)], LBLUE)
    s += PL([(298, 204), (346, 204), (380, 250), (298, 250)], LBLUE)
    s += NS("".join(R(96 + i * 24, 290 + (i % 2) * 12, 12, 12, OUT) for i in range(14)))
    s += C(428, 280, 10, WHITE) + wheel(160, 340) + wheel(368, 340)
    return s


def rocket():
    s = NS(R(0, 0, 512, 512, NIGHT, 48))
    s += NS("".join(C(x, y, r, "#fff4b8") for x, y, r in ((80, 90, 4), (420, 70, 5), (440, 300, 4), (70, 330, 5), (380, 200, 3), (120, 200, 3))))
    s += P("M226,380 Q256,480 286,380 Z", ORANGE) + P("M240,380 Q256,440 272,380 Z", YELLOW)
    s += P("M196,300 L150,380 L210,370 Z", RED) + P("M316,300 L362,380 L302,370 Z", RED)
    s += P("M256,60 Q330,140 316,300 L306,380 L206,380 L196,300 Q182,140 256,60 Z", WHITE)
    s += P("M256,60 Q296,100 308,140 L204,140 Q216,100 256,60 Z", RED)
    s += C(256, 220, 32, LBLUE, 'stroke-width="10"')
    s += L(256, 300, 256, 380, 6)
    return s


def ship():
    s = sky() + water(370)
    for x in (200, 290):
        s += R(x, 120, 50, 90, RED) + R(x, 120, 50, 20, OUT)
    s += R(130, 200, 270, 90, WHITE, 6)
    s += NS("".join(R(150 + i * 42, 228, 26, 20, LBLUE) for i in range(6)))
    s += R(130, 200, 270, 90, "none", 6)
    s += P("M50,290 L470,290 L420,400 L100,400 Z", NAVY)
    s += R(70, 290, 390, 18, RED, 0, 'stroke="none"') + L(50, 290, 470, 290, 8)
    s += "".join(C(140 + i * 50, 340, 9, WHITE, 'stroke-width="5"') for i in range(6))
    s += NS(C(250, 90, 20, "#dee2e6") + C(280, 66, 26, "#dee2e6"))
    return s


def anchor():
    s = shadow(256, 450, 140)
    s += ring(256, 100, 32, NAVY, 18)
    s += limb("M256,134 L256,420", NAVY, 26)
    s += limb("M190,180 L322,180", NAVY, 24)
    s += limb("M120,300 Q130,420 256,420 Q382,420 392,300", NAVY, 24)
    s += PL([(96, 320), (120, 270), (148, 314)], NAVY) + PL([(364, 314), (392, 270), (416, 320)], NAVY)
    s += P("M256,100 Q190,140 210,210 Q220,260 180,300", extra=f'stroke="{TAN}" stroke-width="10"')
    return s


# ---------------------------------------------------------------- jobs
def man_hair(hy=120, hr=54):
    return P(f"M{256 - hr},{hy} Q{256 - hr},{hy - hr - 8} 256,{hy - hr - 2} "
             f"Q{256 + hr},{hy - hr - 8} {256 + hr},{hy} L{256 + hr - 6},{hy - 20} "
             f"Q256,{hy - 34} {256 - hr + 6},{hy - 20} Z", HAIR)


def woman_hair(hy=124, hr=54, color=HAIR):
    back = P(f"M{256 - hr - 14},{hy + 10} Q{256 - hr - 20},{hy - hr - 20} 256,{hy - hr - 12} "
             f"Q{256 + hr + 20},{hy - hr - 20} {256 + hr + 14},{hy + 10} L{256 + hr + 12},{hy + 60} "
             f"Q256,{hy + 70} {256 - hr - 12},{hy + 60} Z", color)
    front = P(f"M{256 - hr},{hy + 6} Q{256 - hr + 4},{hy - hr - 6} 256,{hy - hr - 2} "
              f"Q{256 + hr - 4},{hy - hr - 6} {256 + hr},{hy + 6} Q{256 + 24},{hy - 40} {256 - 10},{hy - 30} "
              f"Q{256 - 30},{hy - 20} {256 - hr},{hy + 6} Z", color)
    return back, front


def adult(shirt, bottoms, kind="pants", hair=None, back="", extra="", shoe=OUT, skin=SKIN, hy=120):
    return person(hy, 54, 188, 320, 440, shirt, bottoms, kind, hair_back=back,
                  hair_front=man_hair(hy) if hair is None else hair, extra=extra, skin=skin, shoe=shoe)


def stethoscope(y=190):
    return (P(f"M230,{y} Q222,{y + 70} 256,{y + 80} Q290,{y + 70} 282,{y}", extra=f'stroke="{DGREY}" stroke-width="6"')
            + P(f"M256,{y + 80} L256,{y + 100}", extra=f'stroke="{DGREY}" stroke-width="6"') + C(256, y + 108, 10, GREY, 'stroke-width="5"'))


def doctor():
    ex = (PL([(232, 188), (256, 240), (246, 250), (220, 196)], "#e9ecef") + PL([(280, 188), (256, 240), (266, 250), (292, 196)], "#e9ecef")
          + R(274, 254, 24, 22, "none", 3, 'stroke-width="5"') + stethoscope())
    return adult(WHITE, "#5fa8d3", "pants", extra=ex, shoe=DGREY)


def teacher():
    board = (R(14, 100, 230, 170, BROWN, 8) + R(28, 114, 202, 142, DGREEN, 3)
             + C(76, 170, 24, "none", f'stroke="{WHITE}" stroke-width="5"')
             + PL([(120, 200), (150, 146), (180, 200)], "none", f'stroke="{WHITE}" stroke-width="5"')
             + P("M50,230 Q90,214 130,232 T210,228", extra=f'stroke="{WHITE}" stroke-width="5"')
             + R(192, 144, 26, 26, "none", 0, f'stroke="{YELLOW}" stroke-width="5"')
             + L(40, 290, 60, 430, 8, BROWN) + L(220, 290, 200, 430, 8, BROWN))
    back, front = woman_hair()
    pers = person(124, 54, 192, 320, 440, "#2a9d8f", "#264653", "pants", hair_back=back, hair_front=front,
                  extra=R(214, 112, 34, 22, "none", 8, 'stroke-width="5"') + R(264, 112, 34, 22, "none", 8, 'stroke-width="5"') + L(248, 120, 264, 120, 5),
                  shoe=DBROWN)
    return board + tr(90, 0, pers)


def police_officer():
    cap = (P("M196,80 Q192,38 256,36 Q320,38 316,80 Z", NAVY) + R(198, 70, 116, 16, OUT, 4)
           + P("M206,86 Q256,108 306,86 L300,80 L212,80 Z", OUT)
           + PL(star_pts(256, 56, 14, 6), YELLOW, 'stroke-width="4"'))
    badge = PL(star_pts(286, 236, 16, 8, 6), YELLOW, 'stroke-width="5"') + R(212, 300, 88, 12, OUT, 2)
    return adult("#1d3557", "#14213d", "pants", hair="", extra=cap + badge, shoe=OUT)


def firefighter():
    Ct = "#d9a441"
    stripes = (R(206, 278, 100, 14, YELLOW, 0, 'stroke-width="5"')
               + R(212, 396, 34, 12, YELLOW, 0, 'stroke-width="4"') + R(266, 396, 34, 12, YELLOW, 0, 'stroke-width="4"'))
    helmet = (E(256, 94, 86, 16, RED) + P("M198,92 Q196,36 256,34 Q316,36 314,92 Z", RED)
              + P("M256,38 L256,90", extra=f'stroke="{DRED}" stroke-width="8"') + P("M240,52 L272,52 L268,78 L244,78 Z", YELLOW, 'stroke-width="5"'))
    return adult(Ct, Ct, "pants", hair="", extra=stripes + helmet, shoe=OUT)


def chef():
    hat = (merged(C(222, 46, 30) + C(256, 30, 36) + C(290, 46, 30) + R(214, 44, 84, 40), WHITE)
           + R(210, 70, 92, 20, WHITE, 4))
    jacket = (PL([(234, 188), (256, 214), (278, 188)], RED) + dot(240, 240, 6) + dot(272, 240, 6) + dot(240, 270, 6) + dot(272, 270, 6))
    return adult(WHITE, "#495057", "pants", hair="", extra=jacket + hat, shoe=OUT)


def farmer():
    overall = (R(220, 236, 72, 84, BLUE, 6) + L(224, 240, 214, 192, 8, BLUE) + L(288, 240, 298, 192, 8, BLUE)
               + dot(228, 248, 5, YELLOW) + dot(284, 248, 5, YELLOW) + R(240, 262, 32, 24, "none", 3, 'stroke-width="5"'))
    plaid = P("M210,210 L302,210 M210,250 L222,250 M290,250 L302,250", extra=f'stroke="{DRED}" stroke-width="6"')
    hat = (E(256, 80, 96, 18, BLONDE) + P("M204,80 Q204,30 256,30 Q308,30 308,80 Z", BLONDE)
           + P("M206,66 Q256,76 306,66 L307,78 Q256,88 205,78 Z", RED))
    return adult(RED, BLUE, "pants", hair="", extra=plaid + overall + hat, shoe=DBROWN)


def nurse():
    back, front = woman_hair(color="#3b2a20")
    cap = P("M222,76 L290,76 L282,50 L230,50 Z", WHITE) + R(250, 54, 12, 18, "#1f6feb", 2, 'stroke="none"') + R(247, 57, 18, 12, "#1f6feb", 2, 'stroke="none"')
    ex = cap + PL([(236, 192), (256, 216), (276, 192)], "#90e0ef") + R(270, 250, 22, 18, "none", 3, 'stroke-width="5"')
    return person(124, 54, 192, 320, 440, "#48cae4", "#48cae4", "pants", hair_back=back, hair_front=front, extra=ex, shoe=WHITE)


# ---------------------------------------------------------------- things
def camera():
    s = shadow(256, 410, 180)
    s += P("M190,160 L210,124 L300,124 L320,160 Z", DGREY)
    s += R(80, 156, 352, 230, "#3d405b", 26)
    s += R(80, 200, 352, 130, "#6c757d", 0, 'stroke="none"') + R(80, 156, 352, 230, "none", 26)
    s += C(256, 270, 90, "#adb5bd") + C(256, 270, 64, OUT) + C(256, 270, 40, "#3a6ea5")
    s += NS(C(240, 252, 12, WHITE, 'opacity=".8"'))
    s += R(110, 130, 50, 26, RED, 6) + R(360, 180, 46, 26, YELLOW, 6)
    return s


def wallet():
    s = shadow(256, 410, 170)
    s += rot(-8, 256, 180, R(150, 120, 220, 110, "#95d5b2", 6) + C(260, 175, 24, "#74c69d"))
    s += R(90, 170, 332, 220, BROWN, 26)
    s += R(250, 230, 172, 90, DBROWN, 20)
    s += C(380, 275, 14, YELLOW)
    s += R(108, 188, 296, 184, "none", 18, f'stroke="{TAN}" stroke-width="4" stroke-dasharray="10 8"')
    return s


def passport():
    s = shadow(256, 440, 140)
    s += R(146, 76, 230, 340, "#a5a5a5", 16)
    s += R(132, 70, 230, 344, "#1d3557", 16)
    s += C(247, 220, 60, "none", f'stroke="{GOLD}" stroke-width="7"')
    s += E(247, 220, 26, 60, "none", f'stroke="{GOLD}" stroke-width="6"')
    s += P("M187,220 L307,220 M196,190 L298,190 M196,250 L298,250", extra=f'stroke="{GOLD}" stroke-width="6"')
    s += R(197, 320, 100, 12, GOLD, 4, 'stroke="none"') + R(217, 120, 60, 10, GOLD, 4, 'stroke="none"')
    return s


def ticket():
    s = shadow(256, 410, 180)
    d = "M70,150 L442,150 L442,220 A36,36 0 0 0 442,292 L442,362 L70,362 L70,292 A36,36 0 0 0 70,220 Z"
    s += rot(-8, 256, 256, P(d, ORANGE)
             + L(330, 166, 330, 346, 5, DORANGE) + f'<line x1="330" y1="166" x2="330" y2="346" stroke="{CREAM}" stroke-width="6" stroke-dasharray="10 12"/>'
             + PL(star_pts(190, 256, 54, 24), YELLOW)
             + "".join(R(360 + i * 9, 200, 4 + (i % 3) * 2, 110, OUT, 0, 'stroke="none"') for i in range(7)))
    return s


def map_():
    s = shadow(256, 430, 190)
    panels = [(60, 110, 160, 130, 160, 400, 60, 380), (160, 130, 256, 110, 256, 380, 160, 400),
              (256, 110, 352, 130, 352, 400, 256, 380), (352, 130, 452, 110, 452, 380, 352, 400)]
    for i, p in enumerate(panels):
        pts = [(p[0], p[1]), (p[2], p[3]), (p[4], p[5]), (p[6], p[7])]
        s += PL(pts, "#fdf0c4" if i % 2 == 0 else "#f1dfa4")
    s += NS(P("M90,200 Q140,160 200,190 Q240,220 220,280 Q180,320 120,300 Q70,260 90,200 Z", "#95d5b2", 'opacity=".9"')
            + P("M300,170 Q380,150 420,200 Q430,260 370,280 Q310,270 300,170 Z", "#95d5b2", 'opacity=".9"'))
    s += P("M60,340 Q160,330 256,300 Q340,280 452,300", extra=f'stroke="#4ea8de" stroke-width="10"')
    s += P("M130,250 Q200,180 280,240 Q330,280 380,220", extra=f'stroke="{RED}" stroke-width="6" stroke-dasharray="4 14"')
    s += P("M366,206 L394,234 M394,206 L366,234", extra=f'stroke="{RED}" stroke-width="9"')
    return s


def compass():
    s = shadow(256, 440, 150)
    s += C(256, 256, 170, GOLD) + C(256, 256, 140, WHITE)
    for i in range(16):
        a = math.radians(i * 22.5)
        r1 = 112 if i % 4 else 96
        s += L(256 + r1 * math.sin(a), 256 - r1 * math.cos(a), 256 + 128 * math.sin(a), 256 - 128 * math.cos(a), 7 if i % 4 == 0 else 4)
    s += PL([(256, 136), (284, 256), (228, 256)], RED) + PL([(256, 376), (284, 256), (228, 256)], "#3a6ea5")
    s += C(256, 256, 14, GOLD)
    s += C(256, 74, 18, GOLD)
    return s


def backpack():
    s = shadow(256, 440, 140)
    s += limb("M210,120 Q210,70 256,70 Q302,70 302,120", "#2b6cb0", 14)
    s += R(140, 110, 232, 320, "#3a86ff", 60)
    s += P("M140,190 Q256,150 372,190", extra='stroke-width="6"')
    s += R(176, 270, 160, 120, "#2b6cb0", 24)
    s += L(196, 300, 316, 300, 5, YELLOW) + R(240, 290, 32, 18, YELLOW, 4, 'stroke-width="4"')
    s += R(100, 220, 40, 120, "#2b6cb0", 18) + R(372, 220, 40, 120, "#2b6cb0", 18)
    return s


def suitcase():
    s = shadow(256, 446, 160)
    s += P("M226,140 L226,70 L286,70 L286,140", extra='stroke-width="14"')
    s += P("M226,140 L226,70 L286,70 L286,140", extra=f'stroke="{GREY}" stroke-width="6"')
    s += R(130, 136, 252, 290, "#e76f51", 26)
    for x in (190, 256, 322):
        s += L(x, 150, x, 412, 6, "#c4553a")
    s += C(180, 440, 14, OUT) + C(332, 440, 14, OUT)
    s += rot(-12, 300, 200, R(276, 180, 70, 44, YELLOW, 8, 'stroke-width="5"')) + C(190, 340, 24, LBLUE, 'stroke-width="5"')
    return s


def hammer():
    s = shadow(256, 440, 140)
    h = (R(240, 170, 34, 260, TAN, 12) + R(240, 360, 34, 70, "#7b4b2a", 12)
         + P("M150,110 L330,110 L330,180 L150,180 Q130,145 150,110 Z", GREY)
         + P("M330,120 Q390,120 410,80 Q400,140 330,170 Z", GREY))
    s += rot(-30, 256, 270, h)
    return s


def ladder():
    s = shadow(256, 450, 140)
    s += R(150, 60, 24, 390, TAN, 6) + R(338, 60, 24, 390, TAN, 6)
    for y in range(100, 440, 60):
        s += R(170, y, 172, 20, "#c08552", 4)
    return s


def bucket():
    s = shadow(256, 440, 140)
    s += P("M136,200 Q136,40 256,40 Q376,40 376,200", extra='stroke-width="10"')
    s += P("M120,190 L392,190 L360,430 L152,430 Z", "#3a86ff")
    s += E(256, 190, 136, 28, "#90cdf4")
    s += P("M132,250 L380,250", extra=f'stroke="#2b6cb0" stroke-width="10"')
    s += C(120, 196, 10, GREY) + C(392, 196, 10, GREY)
    return s


def brush():
    s = P("M60,440 Q160,380 240,420 Q300,450 360,400", extra=f'stroke="{BLUE}" stroke-width="30" opacity=".8"')
    b = (R(236, 60, 40, 200, "#c1121f", 16) + R(232, 250, 48, 50, GREY, 4)
         + P("M232,300 L280,300 L284,360 Q256,420 228,360 Z", TAN) + P("M230,350 Q256,420 282,350 Q256,370 230,350 Z", BLUE))
    s += rot(30, 256, 256, b)
    return s


def mirror():
    s = shadow(256, 450, 120)
    s += R(246, 380, 20, 60, BROWN) + E(256, 444, 70, 12, BROWN)
    s += E(256, 220, 140, 180, "#d4a373")
    s += E(256, 220, 112, 152, "#d8eefe")
    s += shine("M190,140 L160,190") + shine("M220,150 L170,240") + shine("M330,280 L300,330")
    return s


def pillow():
    s = shadow(256, 400, 190)
    s += P("M90,140 Q256,170 422,140 Q400,256 422,372 Q256,342 90,372 Q112,256 90,140 Z", "#a8dadc")
    s += NS("".join(C(x, y, 9, WHITE) for x in (160, 220, 280, 340) for y in (210, 270, 330) if (x + y) % 120 == 10 or True))
    s += P("M140,180 Q256,200 372,180", extra=f'stroke="{WHITE}" stroke-width="5" opacity=".7"')
    return s


def blanket():
    s = shadow(256, 420, 190)
    shape = P("M70,170 L442,170 L442,390 L70,390 Z")
    s += f'<g fill="#e76f51">{nf(shape)}</g>'
    s += clip("bk", shape, "".join(R(x, 160, 30, 240, "#f4a261") for x in range(90, 450, 80))
              + "".join(R(60, y, 400, 26, "#f4a261", 0, 'opacity=".7"') for y in range(190, 400, 70)))
    s += f'<g fill="none">{nf(shape)}</g>'
    s += P("M70,240 Q256,270 442,240 L442,170 L70,170 Z", "#e76f51", 'opacity="0"')
    s += P("M90,390 L90,420 M120,390 L120,420 M150,390 L150,420 M180,390 L180,420 M210,390 L210,420 M240,390 L240,420 M270,390 L270,420 M300,390 L300,420 M330,390 L330,420 M360,390 L360,420 M390,390 L390,420 M420,390 L420,420",
           extra='stroke-width="5"')
    return s


def towel():
    s = L(80, 120, 432, 120, 14) + C(80, 120, 14, GREY) + C(432, 120, 14, GREY)
    s += R(150, 100, 212, 340, "#90e0ef", 10)
    s += R(150, 100, 212, 60, "#48cae4", 10)
    s += NS(R(152, 360, 208, 18, WHITE) + R(152, 390, 208, 10, WHITE))
    s += P("M150,440 L150,460 M180,440 L180,460 M210,440 L210,460 M240,440 L240,460 M270,440 L270,460 M300,440 L300,460 M330,440 L330,460 M360,440 L360,460",
           extra='stroke-width="5"')
    return s


def soap():
    s = shadow(256, 400, 170)
    s += R(120, 240, 272, 140, "#f4a6c1", 50)
    s += P("M140,270 Q256,230 372,270", extra=f'stroke="{WHITE}" stroke-width="10" opacity=".6"')
    s += "".join(C(x, y, r, "#e7f5ff", 'stroke-width="5" opacity=".95"') for x, y, r in ((170, 200, 30), (236, 160, 40), (320, 190, 28), (370, 130, 20), (180, 120, 18)))
    s += NS("".join(C(x - r * .35, y - r * .35, r * .25, WHITE) for x, y, r in ((170, 200, 30), (236, 160, 40), (320, 190, 28))))
    return s


def oven():
    s = shadow(256, 450, 170)
    s += R(100, 90, 312, 350, "#dee2e6", 16)
    s += R(100, 90, 312, 60, "#adb5bd", 16)
    s += "".join(C(x, 120, 12, OUT) for x in (150, 200, 312, 362))
    s += R(130, 180, 252, 200, "#495057", 12) + R(156, 210, 200, 140, "#ffb703", 8)
    s += R(160, 168, 192, 14, GREY, 6)
    s += NS(E(256, 300, 70, 30, DORANGE))
    s += R(130, 400, 252, 24, "#adb5bd", 6)
    return s


def kettle():
    s = shadow(256, 430, 150)
    s += P("M200,80 Q190,60 205,40 M250,70 Q240,50 255,30", extra=f'stroke="{GREY}" stroke-width="7"')
    s += P("M360,280 L440,180 L452,196 L384,310 Z", RED)
    s += limb("M180,180 Q256,90 332,180", OUT, 14)
    s += P("M140,410 Q120,260 200,190 L312,190 Q392,260 372,410 Z", RED)
    s += E(256, 190, 56, 14, DRED) + C(256, 172, 12, OUT)
    s += R(130, 400, 252, 22, DGREY, 8)
    s += shine("M176,320 Q176,260 210,226")
    return s


def teapot():
    s = shadow(256, 420, 160)
    s += P("M140,300 Q90,280 80,200 Q100,260 140,250 Z", "#4ea8de")
    s += ring(382, 290, 46, "#4ea8de", 20)
    s += E(256, 300, 130, 110, "#4ea8de")
    s += P("M180,200 Q256,160 332,200 Z", "#3a86ff") + C(256, 168, 16, YELLOW)
    s += NS("".join(C(x, y, 10, WHITE) + C(x, y, 4, YELLOW) for x, y in ((210, 290), (300, 270), (256, 340), (190, 350), (322, 340))))
    return s


def fridge():
    s = shadow(256, 450, 130)
    s += R(150, 50, 212, 396, "#e9ecef", 22)
    s += L(150, 190, 362, 190, 8)
    s += R(320, 90, 14, 70, DGREY, 6) + R(320, 220, 14, 120, DGREY, 6)
    s += C(200, 250, 16, RED) + PL(star_pts(240, 290, 16, 7), YELLOW, 'stroke-width="5"') + R(186, 300, 30, 36, LBLUE, 3, 'stroke-width="5"')
    s += R(170, 434, 20, 14, OUT, 3) + R(322, 434, 20, 14, OUT, 3)
    return s


def microwave():
    s = shadow(256, 406, 190)
    s += R(70, 130, 372, 250, "#dee2e6", 18)
    s += R(96, 156, 240, 196, "#495057", 10) + R(116, 176, 200, 156, "#ffd166", 6)
    s += NS(E(216, 300, 70, 14, "#e9c46a") + C(216, 280, 30, ORANGE))
    s += R(352, 156, 70, 196, "#ced4da", 8)
    s += R(362, 170, 50, 26, "#2b2d42", 4) + NS(R(368, 178, 30, 10, "#52b788", 2))
    s += "".join(R(364 + c * 18, 212 + r * 22, 12, 14, WHITE, 3, 'stroke-width="3"') for c in range(3) for r in (0, 1, 2, 3))
    s += R(96, 380, 30, 14, OUT, 3) + R(386, 380, 30, 14, OUT, 3)
    return s


# ---------------------------------------------------------------- food
def sandwich():
    s = shadow(256, 420, 180)
    s += PL([(80, 380), (430, 380), (256, 210)], "#f6d7a7")
    s += P("M90,360 Q150,330 200,360 Q256,330 310,360 Q370,330 420,360 L430,380 L80,380 Z", GREEN)
    s += P("M100,340 L410,340 L420,358 L90,358 Z", RED)
    s += P("M110,320 L400,320 L410,338 L100,338 Z", YELLOW)
    s += PL([(90, 320), (420, 320), (256, 120)], "#f6d7a7")
    s += PL([(90, 320), (420, 320), (256, 120)], "none", f'stroke="#c08552" stroke-width="14"')
    s += PL([(90, 320), (420, 320), (256, 120)], "none")
    return s


def bowl(fill, inner):
    return P("M80,250 L432,250 Q432,420 256,420 Q80,420 80,250 Z", fill) + E(256, 250, 176, 30, inner)


def soup():
    s = shadow(256, 432, 170)
    s += P("M190,200 Q170,170 190,140 M250,190 Q230,160 250,130 M310,200 Q290,170 310,140", extra=f'stroke="{GREY}" stroke-width="7"')
    s += limb("M330,250 L430,140", GREY, 18)
    s += bowl("#e63946", "#f4a261")
    s += NS(C(200, 252, 10, "#52b788") + C(280, 246, 10, YELLOW) + C(240, 260, 8, "#52b788"))
    s += P("M100,320 Q256,350 412,320", extra=f'stroke="{WHITE}" stroke-width="8"')
    return s


def salad():
    s = shadow(256, 432, 170)
    s += merged(C(150, 200, 44) + C(210, 160, 50) + C(290, 156, 50) + C(356, 196, 44) + C(250, 200, 56), "#74c69d")
    s += C(196, 196, 24, RED) + C(316, 186, 24, RED) + C(256, 160, 20, "#b7e4c7") + C(150, 222, 16, YELLOW) + C(360, 222, 16, YELLOW)
    s += NS(C(196, 196, 11, "#ff8fa3") + C(316, 186, 11, "#ff8fa3"))
    s += bowl(WHITE, "#d8f3dc")
    s += P("M90,300 Q256,340 422,300", extra=f'stroke="{LBLUE}" stroke-width="10"')
    return s


def rice():
    s = shadow(256, 432, 170)
    s += limb("M330,90 L190,250", "#c08552", 10) + limb("M370,100 L226,250", "#c08552", 10)
    s += P("M100,252 Q130,150 256,140 Q382,150 412,252 Z", WHITE)
    s += NS("".join(E(x, y, 7, 4, "#e9ecef") for x, y in ((180, 210), (220, 180), (260, 200), (300, 180), (330, 220), (240, 236), (160, 236), (290, 230), (350, 240))))
    s += bowl("#3a86ff", "#ffffff")
    s += P("M90,310 Q256,350 422,310", extra=f'stroke="{WHITE}" stroke-width="8"')
    return s


def noodles():
    s = shadow(256, 432, 170)
    s += limb("M300,70 L230,250", "#c08552", 10) + limb("M340,80 L260,250", "#c08552", 10)
    s += "".join(P(f"M{x},250 Q{x + 10},200 {x},150 Q{x - 10},120 {x + 6},96", extra=f'stroke="{YELLOW}" stroke-width="10"') for x in (238, 252, 266))
    s += bowl("#e63946", "#f6d365")
    s += P("M120,250 Q150,236 180,250 T240,250 T300,250 T360,250 T400,250", extra=f'stroke="#e9b949" stroke-width="7"')
    s += NS(C(330, 248, 14, "#ffafcc") + C(180, 246, 10, GREEN))
    s += P("M90,310 Q256,350 422,310", extra=f'stroke="{WHITE}" stroke-width="8"')
    return s


def chocolate():
    s = shadow(256, 430, 170)
    s += R(150, 300, 230, 130, "#c1121f", 8)
    s += rot(-10, 256, 220, R(120, 90, 250, 250, "#6f3b1f", 10)
             + "".join(R(140 + c * 76, 110 + r * 76, 60, 60, "#7f4a2a", 6, 'stroke-width="5"') for c in range(3) for r in range(3)))
    s += R(150, 300, 230, 130, "#c1121f", 8) + P("M150,300 L380,300 L370,330 L160,330 Z", "#e5e5e5")
    return s


def honey():
    s = shadow(256, 444, 150)
    s += R(150, 110, 212, 50, "#c08552", 10)
    s += P("M140,160 L372,160 Q402,170 402,230 L402,400 Q402,436 366,436 L146,436 Q110,436 110,400 L110,230 Q110,170 140,160 Z", "#f2b134")
    s += P("M150,160 L362,160 L362,190 Q330,214 310,190 Q290,240 270,190 Q240,210 220,190 Q190,226 170,190 L150,190 Z", "#f2b134")
    s += R(160, 260, 192, 110, CREAM, 10)
    s += PL([(256, 280), (286, 297), (286, 333), (256, 350), (226, 333), (226, 297)], YELLOW, 'stroke-width="6"')
    s += shine("M136,260 L136,380")
    return s


def lemon():
    s = shadow(256, 420, 160)
    s += P("M90,260 Q100,150 240,140 Q380,130 420,250 Q400,370 260,380 Q120,390 90,260 Z", "#ffd60a")
    s += E(84, 262, 14, 10, "#ffd60a") + E(424, 250, 14, 10, "#ffd60a")
    s += P("M240,140 Q280,90 330,100 Q300,150 240,140 Z", GREEN)
    s += NS("".join(C(x, y, 4, "#f2b134") for x, y in ((180, 220), (250, 200), (320, 230), (200, 300), (290, 300), (350, 280))))
    s += shine("M140,240 Q150,200 190,180")
    return s


def potato():
    s = shadow(256, 410, 170)
    s += P("M100,260 Q90,170 200,160 Q260,140 330,170 Q420,190 410,280 Q400,370 290,370 Q230,380 170,360 Q100,340 100,260 Z", "#c99a5b")
    s += NS("".join(E(x, y, 9, 5, "#8b5e34") for x, y in ((170, 230), (260, 200), (330, 250), (220, 310), (320, 330), (140, 300))))
    return s


def onion():
    s = shadow(256, 430, 140)
    s += P("M226,410 L220,440 M246,412 L246,446 M266,412 L272,440 M286,408 L296,436", extra='stroke-width="5"')
    s += limb("M256,140 Q250,90 270,60", GREEN, 14) + limb("M262,140 Q280,100 300,90", "#74c69d", 10)
    s += P("M256,140 Q370,220 370,320 Q360,420 256,420 Q152,420 142,320 Q142,220 256,140 Z", "#b5838d")
    s += P("M256,150 Q300,240 300,320 Q296,400 256,416 M256,150 Q212,240 212,320 Q216,400 256,416", extra=f'stroke="#6d4c5a" stroke-width="5"')
    s += shine("M180,280 Q182,240 210,214")
    return s


def mushroom():
    s = shadow(256, 436, 140)
    s += P("M206,260 L306,260 Q320,360 330,420 Q256,440 182,420 Q192,360 206,260 Z", CREAM)
    s += P("M80,280 Q80,110 256,100 Q432,110 432,280 Q256,300 80,280 Z", RED)
    s += C(180, 180, 22, WHITE) + C(272, 150, 28, WHITE) + C(360, 210, 20, WHITE) + C(230, 240, 14, WHITE) + C(330, 260, 10, WHITE)
    return s


def watermelon():
    s = shadow(256, 410, 190)
    s += P("M60,200 A196,196 0 0 0 452,200 Z", "#40916c")
    s += P("M84,200 A172,172 0 0 0 428,200 Z", "#d8f3dc", 'stroke="none"')
    s += P("M100,200 A156,156 0 0 0 412,200 Z", "#ef476f")
    s += NS("".join(E(x, y, 6, 10, OUT) for x, y in ((170, 240), (220, 280), (290, 280), (340, 240), (256, 330), (200, 230), (310, 230))))
    s += L(60, 200, 452, 200, 8)
    return s


def pineapple():
    s = shadow(256, 444, 130)
    for a, c in ((-40, GREEN), (40, GREEN), (-15, DGREEN), (15, DGREEN), (0, GREEN)):
        s += rot(a, 256, 170, P("M240,170 Q236,90 256,40 Q276,90 272,170 Z", c))
    body = E(256, 300, 110, 140)
    s += f'<g fill="#f6bd60">{nf(body)}</g>'
    s += clip("pa", body, "".join(f'<line x1="{x}" y1="140" x2="{x + 260}" y2="460" stroke="#c98a2b" stroke-width="6"/>' for x in range(-120, 380, 44))
              + "".join(f'<line x1="{x}" y1="140" x2="{x - 260}" y2="460" stroke="#c98a2b" stroke-width="6"/>' for x in range(140, 640, 44)))
    s += f'<g fill="none">{nf(body)}</g>'
    return s


# ---------------------------------------------------------------- music
def piano():
    s = shadow(256, 444, 190)
    s += R(70, 90, 372, 250, "#3d2b1f", 16)
    s += R(150, 120, 212, 60, "#5a3e2b", 6)
    s += R(60, 330, 392, 30, "#3d2b1f", 6)
    s += R(70, 252, 372, 80, WHITE, 0)
    for i in range(1, 14):
        x = 70 + i * 372 / 14
        s += L(x, 252, x, 332, 4)
    for i in (1, 2, 4, 5, 6, 8, 9, 11, 12, 13):
        x = 70 + i * 372 / 14
        if x < 440:
            s += R(x - 9, 252, 18, 48, OUT, 2, 'stroke="none"')
    s += R(90, 360, 28, 80, "#3d2b1f", 4) + R(394, 360, 28, 80, "#3d2b1f", 4)
    return s


def violin():
    body = (merged(E(256, 220, 70, 74) + E(256, 360, 90, 90) + R(206, 220, 100, 130), "#b5651d"))
    v = (R(244, 30, 24, 210, OUT, 6) + C(256, 34, 20, "#7b3f12") + body
         + P("M220,300 Q210,320 222,340 M292,300 Q302,320 290,340", extra='stroke-width="6"')
         + R(226, 380, 60, 12, OUT, 3) + "".join(L(248 + i * 6, 40, 248 + i * 6, 400, 2, "#eee") for i in range(4)))
    s = shadow(256, 470, 110) + rot(20, 256, 256, v)
    s += L(80, 120, 420, 400, 8, "#7b3f12") + L(90, 132, 420, 410, 3, "#f8f9fa")
    return s


def drum():
    s = shadow(256, 430, 170)
    s += limb("M150,100 L240,200", "#e9c46a", 12) + C(144, 92, 14, "#e9c46a")
    s += limb("M370,90 L290,200", "#e9c46a", 12) + C(376, 84, 14, "#e9c46a")
    s += P("M100,220 L100,370 Q256,430 412,370 L412,220 Z", RED)
    s += P("M100,240 L170,380 L256,250 L340,384 L412,240", extra=f'stroke="{YELLOW}" stroke-width="6"')
    s += P("M100,360 Q256,420 412,360", extra='stroke-width="14"')
    s += E(256, 220, 156, 40, "#f8f9fa")
    s += E(256, 220, 156, 40, "none", 'stroke-width="14"')
    return s


def microphone():
    s = shadow(256, 450, 110)
    m = (P("M224,250 L288,250 L272,430 Q256,444 240,430 Z", OUT)
         + R(216, 230, 80, 30, DGREY, 8) + C(256, 160, 80, "#adb5bd")
         + "".join(L(256 + dx, 84, 256 + dx, 236, 3, DGREY) for dx in (-50, -25, 0, 25, 50))
         + "".join(L(180, 160 + dy, 332, 160 + dy, 3, DGREY) for dy in (-50, -25, 0, 25, 50))
         + C(256, 160, 80, "none") + R(248, 300, 16, 40, RED, 4, 'stroke="none"'))
    s += rot(20, 256, 260, m)
    s += P("M400,120 Q420,140 400,160 M424,100 Q456,140 424,180", extra='stroke-width="6"')
    return s


def headphones():
    s = shadow(256, 430, 170)
    s += limb("M120,300 L120,220 Q120,90 256,90 Q392,90 392,220 L392,300", "#3d405b", 26)
    s += R(80, 260, 80, 140, "#e63946", 30) + R(352, 260, 80, 140, "#e63946", 30)
    s += R(140, 280, 34, 100, "#3d405b", 14) + R(338, 280, 34, 100, "#3d405b", 14)
    s += P("M420,120 L420,180 L448,170 L448,110 Z", "none", 'stroke-width="0"')
    return s


# ---------------------------------------------------------------- objects
def lightbulb():
    s = ""
    for a in range(-80, 81, 40):
        s += rot(a, 256, 200, L(256, 40, 256, 70, 10, ORANGE))
    s += P("M256,90 Q360,90 360,200 Q360,260 310,300 L310,340 L202,340 L202,300 Q152,260 152,200 Q152,90 256,90 Z", YELLOW)
    s += P("M230,300 L230,240 L256,270 L282,240 L282,300", extra=f'stroke="{ORANGE}" stroke-width="6"')
    s += R(206, 336, 100, 80, GREY, 10)
    s += L(206, 362, 306, 362, 5) + L(206, 388, 306, 388, 5)
    s += P("M234,416 L278,416 L268,444 L244,444 Z", OUT)
    s += shine("M190,190 Q192,140 230,120")
    return s


def battery():
    s = shadow(256, 400, 190)
    s += R(420, 210, 30, 92, GREY, 8)
    s += R(60, 170, 366, 172, "#3d405b", 26)
    s += R(80, 190, 230, 132, "#52b788", 14, 'stroke="none"')
    s += PL([(220, 190), (170, 262), (210, 262), (180, 324), (260, 240), (220, 240), (250, 190)], YELLOW, 'stroke-width="6"')
    return s


def magnet():
    s = P("M100,90 Q60,70 50,40 M90,130 Q40,130 20,100 M412,90 Q452,70 462,40 M422,130 Q472,130 492,100", extra=f'stroke="{GREY}" stroke-width="5" stroke-dasharray="8 10"')
    s += limb("M150,110 L150,280 Q150,400 256,400 Q362,400 362,280 L362,110", RED, 80)
    s += R(102, 80, 96, 70, "#dee2e6", 6) + R(314, 80, 96, 70, "#dee2e6", 6)
    return s


def globe():
    s = shadow(256, 450, 120)
    s += E(256, 440, 90, 16, "#7b4b2a") + R(246, 380, 20, 60, "#7b4b2a")
    s += P("M120,120 A170,170 0 0 0 360,380", extra='stroke-width="14"')
    s += C(240, 230, 140, "#4ea8de")
    s += NS(P("M170,140 Q230,120 250,160 Q240,210 200,220 Q170,250 150,230 Q130,180 170,140 Z", "#74c69d")
            + P("M270,240 Q330,220 350,270 Q340,330 290,340 Q260,300 270,240 Z", "#74c69d")
            + P("M200,280 Q230,300 220,330 Q190,320 200,280 Z", "#74c69d"))
    s += C(240, 230, 140, "none")
    s += shine("M150,180 Q170,130 210,110")
    return s


def calendar():
    s = shadow(256, 440, 170)
    s += R(96, 100, 320, 330, WHITE, 18)
    s += P("M96,170 L96,118 Q96,100 114,100 L398,100 Q416,100 416,118 L416,170 Z", RED)
    s += R(150, 70, 20, 60, DGREY, 8) + R(342, 70, 20, 60, DGREY, 8)
    for r in range(4):
        for c in range(5):
            x, y = 120 + c * 56, 196 + r * 56
            s += R(x, y, 40, 40, "#f1f3f5", 6, 'stroke="none"')
    s += C(296, 272, 30, "none", f'stroke="{RED}" stroke-width="7"')
    s += R(276, 252, 40, 40, "#ffccd5", 6, 'stroke="none"')
    return s


def envelope():
    s = shadow(256, 420, 180)
    s += R(70, 140, 372, 250, CREAM, 14)
    s += P("M76,380 L220,260 M436,380 L292,260", extra=f'stroke="#d9c49a" stroke-width="6"')
    s += P("M70,152 L256,290 L442,152", "#f6e7c1")
    s += P("M256,268 C210,236 232,206 256,226 C280,206 302,236 256,268 Z", RED)
    return s


def newspaper():
    s = shadow(256, 440, 170)
    s += R(120, 90, 290, 340, "#e9ecef", 6)
    s += R(96, 70, 290, 350, WHITE, 6)
    s += R(120, 96, 242, 30, OUT, 4, 'stroke="none"')
    s += R(120, 146, 120, 100, LBLUE, 4, 'stroke-width="4"') + NS(PL([(120, 246), (160, 196), (190, 220), (210, 200), (240, 246)], GREEN))
    s += "".join(R(256, y, 106, 8, GREY, 3, 'stroke="none"') for y in range(150, 250, 20))
    s += "".join(R(120, y, 242, 8, GREY, 3, 'stroke="none"') for y in range(270, 400, 20))
    return s


def candle():
    s = shadow(256, 440, 140)
    s += E(256, 420, 120, 26, GOLD)
    s += R(206, 200, 100, 220, "#f8edeb", 10)
    s += P("M206,214 L306,214 L306,240 Q290,270 280,240 Q266,226 250,250 Q236,276 226,240 Q216,226 206,240 Z", WHITE)
    s += L(256, 200, 256, 170, 6)
    s += P("M256,90 Q290,140 276,166 Q256,184 236,166 Q222,140 256,90 Z", ORANGE) + P("M256,130 Q270,150 264,164 Q256,172 248,164 Q242,150 256,130 Z", YELLOW)
    s += NS(C(256, 140, 60, "#ffd166", 'opacity=".25"'))
    return s


def trophy():
    s = shadow(256, 450, 130)
    s += ring(150, 170, 46, GOLD, 18) + ring(362, 170, 46, GOLD, 18)
    s += P("M150,90 L362,90 L362,170 Q362,290 256,300 Q150,290 150,170 Z", GOLD)
    s += R(236, 296, 40, 70, GOLD) + R(176, 360, 160, 30, "#7b4b2a", 6) + R(160, 390, 192, 46, "#5a3a20", 6)
    s += PL(star_pts(256, 180, 46, 20), YELLOW, 'stroke-width="6"')
    s += shine("M180,120 L180,200")
    return s


DRAW_A2 = {
    "giraffe": giraffe, "zebra": zebra, "monkey": monkey, "penguin": penguin, "snake": snake, "turtle": turtle,
    "whale": whale, "shark": shark, "owl": owl, "bee": bee, "spider": spider, "camel": camel,
    "bridge": bridge, "castle": castle, "forest": forest, "desert": desert, "island": island, "volcano": volcano,
    "lighthouse": lighthouse, "farm": farm, "tent": tent, "beach": beach,
    "airport": airport, "ambulance": ambulance, "tractor": tractor, "submarine": submarine, "taxi": taxi,
    "rocket": rocket, "ship": ship, "anchor": anchor,
    "doctor": doctor, "teacher": teacher, "police-officer": police_officer, "firefighter": firefighter,
    "chef": chef, "farmer": farmer, "nurse": nurse,
    "camera": camera, "wallet": wallet, "passport": passport, "ticket": ticket, "map": map_, "compass": compass,
    "backpack": backpack, "suitcase": suitcase, "hammer": hammer, "ladder": ladder, "bucket": bucket, "brush": brush,
    "mirror": mirror, "pillow": pillow, "blanket": blanket, "towel": towel, "soap": soap,
    "oven": oven, "kettle": kettle, "teapot": teapot, "fridge": fridge, "microwave": microwave,
    "sandwich": sandwich, "soup": soup, "salad": salad, "rice": rice, "noodles": noodles, "chocolate": chocolate,
    "honey": honey, "lemon": lemon, "potato": potato, "onion": onion, "mushroom": mushroom,
    "watermelon": watermelon, "pineapple": pineapple,
    "piano": piano, "violin": violin, "drum": drum, "microphone": microphone, "headphones": headphones,
    "lightbulb": lightbulb, "battery": battery, "magnet": magnet, "globe": globe, "calendar": calendar,
    "envelope": envelope, "newspaper": newspaper, "candle": candle, "trophy": trophy,
}

art.DRAW.update(DRAW_A2)
art.CATEGORY_BG.update({"places": "#e3f2fd", "jobs": "#fff0f3", "music": "#f3e8ff"})
art.BG_OVERRIDE.update({"penguin": "#e0f2fe", "whale": SKY, "shark": "#cfe8ff", "submarine": "#9fd3f5",
                        "camel": "#ffe8c2", "bee": "#fff8e1"})
