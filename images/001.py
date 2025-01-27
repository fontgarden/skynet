import math
import argparse
import drawBot as db
import random
#import pytweening as pt
from fontTools.ttLib import TTFont
from datetime import datetime


# Width, Height, Margin, Unit, Frames
W, H, M, U, F = 1080*2, 1080*2, 120, 60, 50
MAIN_FONT_PATH = "fonts/SkynetGroteskVF.ttf"
MAIN_TEXT_OPSZ = 144
CURRENT_DATE = datetime.now()
FORMATTED_DATE = CURRENT_DATE.strftime("%d-%m-%Y")
GRID_VIEW = False


# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()


# FontTools docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(MAIN_FONT_PATH)


# Draws a grid
def grid():
    db.fill(None)
    db.stroke(0.5)
    db.strokeWidth(1)
    step_x = 0
    step_y = 0
    increment_x, increment_y = U*2, U*2
    db.rect(M, M, W - (M * 2), H - (M * 2))
    for x in range(33*1):
        db.polygon((M + step_x, M), (M + step_x, H - M))
        step_x += increment_x
    for y in range(33*1):
        db.polygon((M, M + step_y), (W - M, M + step_y))
        step_y += increment_y
    #db.stroke(0.9, 0.0, 0.0, 1.0)
    #db.fill(None)
    db.polygon((W / 2, 0), (W / 2, H))
    db.polygon((0, H / 2), (W, H / 2))


# Remap input range to VF axis range
# This is useful for animation
# (E.g. sinewave(-1,1) to wght(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)


# For looping animations
def sin_loop(x):
    # Scale the input to the range [0, 2π] and shift by -π/2
    scaled_input = 2 * math.pi * (x % 1) - (math.pi / 2)
    # Calculate the sine of the scaled input
    return (math.sin(scaled_input) + 1) / 2


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    db.newPage(W, H)
    db.fill(0.05)
    db.fill(0.01)
    db.rect(-2, -2, W + 2, H + 2)

    if GRID_VIEW:
        grid()
    else:
        pass


# Main Text
draw_background()
db.font(MAIN_FONT_PATH)
db.openTypeFeatures(dlig=False)
#db.openTypeFeatures(dlig=True)
#for axis, data in db.listFontVariations().items():
#   print((axis, data))


db.stroke(None)
db.tracking(None)
SIZE = 180
OPSZ = 144
db.fontVariations(wght=400)
db.fontVariations(opsz=OPSZ)
db.fontSize(SIZE)
#db.lineHeight(SIZE*1.02)
db.fill(0.9)


TOP_ROW = 32
# db.text("أشهد يا إلهي",             (M+(U*(31)),   M+(U*(TOP_ROW-2))), align="right")
# db.text("بأنّك خلقتني",              (M+(U*(31)),   M+(U*(TOP_ROW-6))), align="right")
# db.text("لعرفانك وعبادتك",          (M+(U*(31)),   M+(U*(TOP_ROW-10))), align="right")
# db.text("أشهد في هذا الحين",        (M+(U*(31)),   M+(U*(TOP_ROW-14))), align="right")
# db.text("بعجزي وقوتك وضعفي",        (M+(U*(31)),   M+(U*(TOP_ROW-18))), align="right")
# db.text("واقتدارك وفقري وغنآئك",    (M+(U*(31)),   M+(U*(TOP_ROW-22))), align="right")
# db.text("لا إله إلاّ أنت المهيمن القيّوم", (M+(U*(31)),M+(U*(TOP_ROW-26))), align="right")


db.fontSize(256+64)
db.text("skynet was",      (M+13, M+(U*(TOP_ROW-4.6))),  align="left")
db.text("closed source", (M, M+(U*(TOP_ROW-9))),  align="left")

db.fontSize(128+32+16-4)
# v = 4
# db.text("skynet was closed-source",   (M,       M+(U*(TOP_ROW-v*9))), align="left")
# db.text("skynet was closed-source",   (M,       M+(U*(TOP_ROW-v*8))), align="left")
# db.text("skynet was closed-source",   (M,       M+(U*(TOP_ROW-v*7))), align="left")
# db.text("skynet was closed-source",   (M,       M+(U*(TOP_ROW-v*6))), align="left")
# db.text("skynet was closed-source",   (M,       M+(U*(TOP_ROW-v*5))), align="left")
# db.text("skynet was closed-source",   (M,       M+(U*(TOP_ROW-v*4))), align="left")
# db.text("skynet was closed-source",   (M,       M+(U*(TOP_ROW-v*3))), align="left")
# db.text("skynet was closed-source",   (M,       M+(U*(TOP_ROW-v*2))), align="left")
# db.text("skynet was closed-source",   (M,       M+(U*(TOP_ROW-v*1))), align="left")


# Generate 32 random points within margins
num_points = 8
# Calculate vertical range for upper 3/4 (from top to 75% height)
new_y_max = M + (H - 2*M) * 0.75  # 75% from top of margin area
points = [(random.uniform(M, W-M), random.uniform(M, new_y_max)) for _ in range(num_points)]

# Draw connecting lines between all points
db.stroke(0.9)
db.strokeWidth(2)
for i in range(len(points)):
    for j in range(i+1, len(points)):
        db.line((points[i][0], points[i][1]), (points[j][0], points[j][1]))

# Draw circles at each point
db.fill(0.9)
db.stroke(None)
for x, y in points:
    db.oval(x-20, y-20, 40, 40)  # 20px diameter circles

db.stroke(None)
db.tracking(None)
db.fill(0.9)
db.fontSize(256+64)
db.text("skynet was",      (M+13, M+(U*(TOP_ROW-4.6))),  align="left")
db.text("closed source", (M, M+(U*(TOP_ROW-9))),  align="left")

db.saveImage(args.output)
print("DrawBot: Done\n")
