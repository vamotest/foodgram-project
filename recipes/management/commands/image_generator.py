from pathlib import Path
from random import randint

from PIL import Image, ImageDraw


def random_gradient():
    img = Image.new('RGB', (500, 500), '#FFFFFF')
    draw = ImageDraw.Draw(img)

    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    dr = (randint(0, 255) - r) / 500.
    dg = (randint(0, 255) - g) / 500.
    db = (randint(0, 255) - b) / 500.

    for i in range(500):
        r, g, b = r + dr, g + dg, b + db
        draw.line((i, 0, i, 500), fill=(int(r), int(g), int(b)))

    return img


def main():
    folder = 'upload'
    path = Path(folder)
    path.mkdir(parents=True, exist_ok=True)

    for name in range(20):
        image = random_gradient()
        image.save(f'{folder}/{name + 1}.png', 'PNG')


if __name__ == '__main__':
    main()
