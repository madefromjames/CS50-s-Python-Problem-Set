import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        link = re.search(r"(https?:\/\/)?(www\.)?youtube\.com\/embed\/(\w+)", s, re.I)
        if link:
            url = "https://youtu.be/" + link.group(3)
            return url


if __name__ == "__main__":
    main()