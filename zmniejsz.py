# ascii generator
import argparse
from PIL import Image

# 10 levels of gray
gscale1 = "$@%8&#*/|?-_+~<>;:,\"^`'. "
gscale2 = "@%#*+=-:. "


def average(hist):
    R = 0
    G = 0
    B = 0
    d = 0
    for t in hist.getdata():
        R += t[0]
        G += t[1]
        B += t[2]
        d += 1

    if d == 0:
        return 0
    return (int(R / d), int(G / d), int(B / d))


def generate_new_image(img, cols, x):
    image = Image.open(img)
    width = image.size[0]
    height = image.size[1]

    if width < cols and x < 1:
        raise ValueError("to small picture")

    if x != 0:
        scale = x
        cols = int(width / scale)
    else:
        scale = int(width / cols)
    rows = int(height / scale)
    new_img = []

    for y in range(rows):
        y1 = y * scale
        y2 = y * scale + scale

        for x in range(cols):
            x1 = x * scale
            x2 = x * scale + scale

            crop = image.crop((x1, y1, x2, y2))
            pixel = average(crop)
            new_img.append(pixel)

    newim = Image.new(image.mode, (cols, rows))
    newim.putdata(new_img)
    return newim


def main():
    desc = "convert images to ascii art."
    parser = argparse.ArgumentParser(description=desc)

    # add arguments to parser
    parser.add_argument("--img", dest="img", help="source image", required=True)
    parser.add_argument(
        "--cols",
        dest="cols",
        help="your terminal width",
        type=int,
        default=120,
        required=False,
    )
    parser.add_argument(
        "--x",
        dest="x",
        help="your scale",
        type=int,
        default=0,
        required=False,
    )
    parser.add_argument(
        "--out",
        dest="out",
        help="your output or terminal if not mentioned",
        default="terminal",
        required=False,
    )

    args = parser.parse_args()

    img = args.img
    cols = args.cols
    x = args.x

    out = args.out

    new_image = generate_new_image(img, cols, x)

    if out == "terminal":
        new_image.show()
    else:
        new_image.save(out)


if __name__ == "__main__":
    main()
