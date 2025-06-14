# ascii generator
import argparse
from PIL import Image

# 10 levels of gray
gscale2 = "@%#*+=-:. "


def average(hist):
    suma = 0
    division = 0
    for i, amount in enumerate(hist):
        suma += i * amount
        division += amount

    if division == 0:
        return 0
    return suma / division


def generate_new_image(img, cols):

    global gscale2

    image = Image.open(img).convert("L")
    width = image.size[0]
    height = image.size[1]

    if width < cols:
        raise ValueError("to small picture")

    sub = 1.7

    scale = int(width / cols)
    rows = int(height / scale / sub)
    ascii = []

    for y in range(rows):
        y1 = y * scale * sub
        y2 = y * scale * sub + scale

        output = ""
        for x in range(cols):
            x1 = x * scale
            x2 = x * scale + scale

            crop = image.crop((x1, y1, x2, y2))
            gr_scale = gscale2[int((average(crop.histogram()) * 9) / 255)]
            output += gr_scale
        ascii.append(output)
    return ascii


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
        "--out",
        dest="out",
        help="your output file name or terminal if not mentioned",
        default="terminal",
        required=False,
    )

    args = parser.parse_args()

    img = args.img
    cols = args.cols
    output = args.out

    try:
        new_image = generate_new_image(img, cols)
    except Exception as e:
        print(e)

    if output == "terminal":
        for line in new_image:
            print(line)
    else:
        with open(f"{output}.txt", "w") as text_file:
            text_file.writelines("\n".join(new_image))


if __name__ == "__main__":
    main()
