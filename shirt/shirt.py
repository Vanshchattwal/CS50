import sys
from os.path import splitext
from PIL import Image, ImageOps

# take input if input is less or more than 3 sys.exit
# if imput is 3 check if arg1 and arg2 is from png, jpg and jepg if not sys.exit
# if both are from () then check if input and output extention are same if not sys.exit
# if same then go to image main function ***BOOM***


def main():
    if len(sys.argv) == 3:
        input_file = splitext(sys.argv[1])
        output_file = splitext(sys.argv[2])

        supported = [".jpg", ".png", ".jpeg"]

        if input_file[1].lower() not in supported:
            sys.exit("Invalid input")

        if output_file[1].lower() not in supported:
            sys.exit("Invalid output")

        if input_file[1].lower() != output_file[1].lower():
            sys.exit("Input and output have different extensions")

        edit(sys.argv[1], sys.argv[2])

    else:
        if len(sys.argv) > 3:
            print("Too much command-line arguments")
        elif len(sys.argv) < 3:
            print("Too few command-line arguments")


def edit(raw, new):
    with Image.open("shirt.png") as shirt:
        with Image.open(raw) as base_image:
            base_image = ImageOps.fit(base_image, shirt.size)
            base_image.paste(shirt, shirt)
            base_image.save(new)


if __name__ == "__main__":
    main()
