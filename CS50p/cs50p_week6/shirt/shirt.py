from PIL import ImageOps, Image
import os
import sys


def main():
    if argv_check():
        try:
            shirt = Image.open("shirt.png")
            before_image = Image.open(sys.argv[1])
            # ImageOps.fit accepts an image object, not a file, so the image needs to be opened first.
            after_image = ImageOps.fit(before_image, shirt.size)
            # if a mask is given, this method updates only the regions indicated by the mask.
            after_image.paste(shirt, mask=shirt)
            after_image.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("Input does not exist")


def argv_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        # return the extension of the file, it splits the path into two parts: the name and the extension
        input_ext = os.path.splitext(sys.argv[1])[1]
        output_ext = os.path.splitext(sys.argv[2])[1]
        if input_ext not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid input")
        elif output_ext not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid output")
        elif input_ext != output_ext:
            sys.exit("Input and output have different extensions")
        else:
            return True


if __name__ == "__main__":
    main()
