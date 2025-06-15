# ascii generator
import argparse
from PIL import Image


def generate_new_image(img, scale):
    image = Image.open(img)
    width = image.size[0]
    height = image.size[1]

    w = width * scale
    h = height * scale

    if scale < 1:
        raise ValueError("too small scale(scale >=1)")

    new_img = []
    new_line = []

    r = 0
    for pixel in image.getdata():
        if r % w == 0:
            for _ in range(scale):
                for pixel in new_line:
                    new_img.append(pixel)
            new_line = []
        for _ in range(scale):
            new_line.append(pixel)
            r += 1

    newim = Image.new(image.mode, (w, h))
    newim.putdata(new_img)
    return newim


def main():
    desc = "convert images to ascii art."
    parser = argparse.ArgumentParser(description=desc)

    # add arguments to parser
    parser.add_argument("--img", dest="img", help="source image", required=True)
    parser.add_argument(
        "--x",
        dest="cols",
        help="your terminal width",
        type=int,
        default=120,
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
    scale = args.cols
    out = args.out

    new_image = generate_new_image(img, scale)

    if out == "terminal":
        new_image.show()
    else:
        new_image.save(out)


if __name__ == "__main__":
    main()
