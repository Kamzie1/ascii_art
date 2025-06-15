# ascii generator
import argparse
from PIL import Image


def generate_new_image(img, color1, color2):
    image = Image.open(img).convert("RGB")

    new_img = []
    tolerance = 100**2

    for pixel in image.getdata():
        d = (
            (pixel[0] - color1[0]) ** 2
            + (pixel[1] - color1[1]) ** 2
            + (pixel[2] - color1[2]) ** 2
        )
        if d <= tolerance:
            pixel = color2
            print(pixel)
        new_img.append(pixel)

    newim = Image.new(image.mode, image.size)
    newim.putdata(new_img)
    return newim


def parse_color(color_str):
    # Remove parentheses and spaces, then split by comma
    color_str = color_str.strip().replace("(", "").replace(")", "").replace(" ", "")
    parts = color_str.split(",")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError(
            f"Color must have 3 components, got {color_str}"
        )
    return tuple(int(p) for p in parts)


def main():
    desc = "convert images to ascii art."
    parser = argparse.ArgumentParser(description=desc)

    # add arguments to parser
    parser.add_argument("--img", dest="img", help="source image", required=True)
    parser.add_argument(
        "--color1",
        dest="color1",
        help="color to change",
        required=True,
        type=parse_color,
    )
    parser.add_argument(
        "--color2", dest="color2", help="new color", required=True, type=parse_color
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
    color1 = args.color1
    color2 = args.color2
    out = args.out

    new_image = generate_new_image(img, color1, color2)

    if out == "terminal":
        new_image.show()
    else:
        new_image.save(out)


if __name__ == "__main__":
    main()
