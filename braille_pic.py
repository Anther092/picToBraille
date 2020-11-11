"""
ASCII art generator braille only.

To start, put this and the image (you need to rename it to input.jpg) in one folder.

The main problem of the algorithm:
Due to the fact that the 8 empty dots symbol and any other Braille symbol have different widths,
the picture may 'float'.

"""
from PIL import Image, ImageDraw

# Change scale of image.
scale = int(input('% of scale: ')) / 100
imgForScale = Image.open('input.jpg')
widthOldForScale, heightOldForScale = imgForScale.size
widthNewForScale, heightNewForScale = int(widthOldForScale * scale), int(heightOldForScale * scale)
scaleImg = imgForScale.resize((widthNewForScale, heightNewForScale), Image.ANTIALIAS)
scaleImg.save('inputScale.jpg')
# -------------

# Makes the image BW.
factor = int(input('factor: '))  # The more, the darker.
imgForBW = Image.open('inputScale.jpg')
draw = ImageDraw.Draw(imgForBW)
widthForBW, heightForBW = imgForBW.size
pix = imgForBW.load()
for i in range(widthForBW):
    for j in range(heightForBW):
        a = pix[i, j][0]
        b = pix[i, j][1]
        c = pix[i, j][2]
        S = a + b + c
        if S > (((255 + factor) * 3) // 2):
            a, b, c = 255, 255, 255
        else:
            a, b, c = 0, 0, 0
        draw.point((i, j), (a, b, c))
imgForBW.save("inputScaleBW.jpg")
# -------------

# The image should be divided by 2 horizontally, by 4 vertically. Otherwise, the extra pixels will be removed.
img = Image.open('inputScaleBW.jpg')
size = w, h = img.size
if (w % 2) == 0:
    pass
else:
    w -= 1
hCut = h % 4
if hCut == 0:
    pass
else:
    h -= hCut
# -------------

data = img.load()
yStart, yEnd = 0, 4
xStart, xEnd = 0, 2
valueOfPixNow = []
b = w // 2  # I don`t remember.
a = b - 1   # The same thing.
i = 0

while (yEnd <= h) and (xEnd <= w):
    # Getting data from a image.
    valueOfPixNow = []
    for y in range(yStart, yEnd):
        for x in range(xStart, xEnd):
            if not ((230 <= data[x, y][0] <= 255) and (230 <= data[x, y][1] <= 255) and (230 <= data[x, y][2] <= 255)):
                valueOfPixNow.append(1)
            else:
                valueOfPixNow.append(0)
    # -------------------
    # Convert data from image.
    normalBinaryReversed = [valueOfPixNow[0], valueOfPixNow[2], valueOfPixNow[4], valueOfPixNow[1], valueOfPixNow[3],
                            valueOfPixNow[5], valueOfPixNow[6], valueOfPixNow[7]]
    normalBinary = list(reversed(normalBinaryReversed))
    strBinary = ''.join(map(str, normalBinary))
    strHex = hex(int(strBinary, 2))
    twoLastNum = strHex[2:]
    if len(twoLastNum) == 1:
        twoLastNum = '0' + twoLastNum
    hexStrBraille = '28' + twoLastNum
    decimalBraille = int(hexStrBraille, 16)
    answer = chr(decimalBraille)
    # -------------------
    if i == a:
        a += b
        print(answer)
    else:
        print(answer, end='')
    i += 1

    if xEnd < w:
        xStart += 2
        xEnd += 2
    else:
        xStart = 0
        xEnd = 2
        yStart += 4
        yEnd += 4
