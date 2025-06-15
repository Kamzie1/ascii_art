# ascii generator
import argparse
from PIL import Image

colors = ["red", "green", "blue"]


def generate_new_image(img, color1: int, color2: int):
    image = Image.open(img)

    new_img = []

    for pixel in image.getdata():
        bufor = pixel
        pixel2 = [-1 for _ in range(len(pixel))]
        pixel2[len(pixel) - 1] = pixel[len(pixel) - 1]
        pixel2[color1] = bufor[color2]
        pixel2[color2] = bufor[color1]

        for i in range(3):
            if pixel2[i] == -1:
                pixel2[i] = bufor[i]

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
    parser.add_argument(
        "--color1",
        dest="color1",
        help="color to change",
        required=True,
    )
    parser.add_argument("--color2", dest="color2", help="new color", required=True)
    parser.add_argument(
        "--out",
        dest="out",
        help="your output or terminal if not mentioned",
        default="terminal",
        required=False,
    )

    args = parser.parse_args()

    img = args.img
    color1 = args.color1
    color2 = args.color2
    out = args.out

    if not color1 in colors:
        raise ValueError("wrong color1")
    if not color2 in colors:
        raise ValueError("wrong color2")

    color1 = get_value(color1)
    color2 = get_value(color2)
    new_image = generate_new_image(img, color1, color2)

    if out == "terminal":
        new_image.show()
    else:
        new_image.save(out)


if __name__ == "__main__":
    main()
