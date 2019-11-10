from PIL import Image, ImageDraw

img = Image.open('test2.jpg')

draw = ImageDraw.Draw(img)  # Інструмент для редагування фото.
width = img.size[0]  # Задаємо ширину.
height = img.size[1]  # Задаємо висоту.
pix = img.load()  # Вигружаємо значення пікселів.
w = int(width / 20)  # Число, на яке ділиться горизонтальна зона
h = int(height / 11)-8  # Число, на яке ділиться вертикальна зона - 8 пікселів(рядок для інформації фото)
count = red = green = blue = 0


def coloring(x, y):                             # фарбування необхідних зон
    for i in range((x - 1) * w, x * w):
        for j in range((y - 1) * h, y * h):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (a-20, b, c + 70))


for x in range(1, 21):
    for i in range((x - 1) * w, x * w):
        for y in range(1, 12):
            for j in range((y - 1) * h, y * h):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                if b > a and b > c and b < 160 and b > 60:
                    red += a
                    green += b
                    blue += c
                    count += 1
                else:
                    red += a - 25
                    blue += c + 25
                    green += b
                    count += 1

                if i == x * w - 1 and j == y * h - 1 and count != 0:
                    if red / count - blue / count > 35:
                        coloring(x, y)
                    count = red = green = blue = 0


del draw
img.show()


