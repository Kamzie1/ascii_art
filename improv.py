# ascii generator
import argparse
from PIL import Image


def generate_new_image(img, r, g, b):
    image = Image.open(img)

    new_img = []

    for pixel in image.getdata():
        bufor = pixel
        pixel2 = [pixel[i] for i in range(len(pixel))]
        pixel2[0] += r
        pixel2[1] += g
        pixel2[2] += b

        if pixel2[0] > 255:
            pixel2[0] = 255
        if pixel2[1] > 255:
            pixel2[1] = 255
        if pixel2[2] > 255:
            pixel2[2] = 255
        if pixel2[0] < 0:
            pixel2[0] = 0
        if pixel2[1] < 0:
            pixel2[1] = 0
        if pixel2[2] < 0:
            pixel2[2] = 0

        pixel = tuple(pixel2)

        new_img.append(pixel)

    newim = Image.new(image.mode, image.size)
    newim.putdata(new_img)
    return newim


def get_value(color):
    match color:
        case "red":
            return 0
        case "green":
            return 1
        case "blue":
            return 2
        case _:
            raise ValueError("wrong color")


def main():
    desc = "swap colors art."
    parser = argparse.ArgumentParser(description=desc)

    # add arguments to parser
    parser.add_argument("--img", dest="img", help="source image", required=True)
    parser.add_argument("--r", dest="r", help="source image", type=int, default=0)
    parser.add_argument("--g", dest="g", help="source image", type=int, default=0)
    parser.add_argument("--b", dest="b", help="source image", type=int, default=0)

    parser.add_argument(
        "--out",
        dest="out",
        help="your output or terminal if not mentioned",
        default="terminal",
        required=False,
    )

    args = parser.parse_args()

    img = args.img
    r = args.r
    g = args.g
    b = args.b
    out = args.out

    new_image = generate_new_image(img, r, g, b)

    if out == "terminal":
        new_image.show()
    else:
        new_image.save(out)


if __name__ == "__main__":
    main()
