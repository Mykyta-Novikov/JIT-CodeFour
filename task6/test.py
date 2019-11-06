import math

from PIL import Image, ImageDraw

img = Image.open('test2.jpg')

draw = ImageDraw.Draw(img)  # Создаем инструмент для рисования.
width = img.size[0]  # Определяем ширину.
height = img.size[1]  # Определяем высоту.
pix = img.load()  # Выгружаем значения пикселей.
w = int(width / 50)
h = int(height / 50)
count = red = green = blue = 0
cq = 0

def coloring(x, y):
    for i in range((x - 1) * w, x * w):
        for j in range((y - 1) * h, y * h):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (a-20, b , c+ 70))

for x in range(1, 51):
    for i in range((x - 1) * w, x * w):
        for y in range(1, 51):
            for j in range((y - 1) * h, y * h):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                red += a
                green += b
                blue += c
                count += 1
                if i == x * w - 1 and j == y * h - 1:
                    if 15 <= math.fabs(int(red / count) - 90) and 15 <= math.fabs( # 90 - red
                            int(green / count) - 100) and 15 <= math.fabs(int(blue / count)- 56): # 100 green 56 blue
                        coloring(x, y)
                    print(int(red / count), int(green / count), int(blue / count))
                    count = red = green = blue = 0

print()
del draw


img.show()


