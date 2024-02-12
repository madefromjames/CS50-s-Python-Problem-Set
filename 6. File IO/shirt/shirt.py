import sys
from os.path import splitext
from PIL import ImageOps
from PIL import Image

def main():
    cmdline()
    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]} does not exist")

    # open png shirt
    shirt = Image.open('shirt.png')
    # get the size of the shirt
    size = shirt.size
    # fit both images together
    fit = ImageOps.fit(image, size)
    # paste shirt in image
    fit.paste(shirt, shirt)
    # saving the file
    fit.save(sys.argv[2])

def cmdline():
    argv1 = splitext(sys.argv[1])
    argv2 = splitext(sys.argv[2])
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if argv1[1].lower() != argv2[1].lower():
        sys.exit("Input and output have different extensions")
    if extension(argv1[1]) == False:
        sys.exit("Invalid input")
    if extension(argv2[1]) == False:
        sys.exit("Invalid output")

def extension(file):
    if file in [".jpg", ".jpeg", "png"]:
        return True
    return False


if __name__ == "__main__":
    main()