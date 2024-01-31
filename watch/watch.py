import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    elements = re.search(
        r".+src=\"https?://(?:www\.)?youtube\.com/embed/([^\"]+)[\"]", s, re.IGNORECASE
    )

    try:
        format = f"https://youtu.be/{elements[1]}"
        return format
    except:
        pass


if __name__ == "__main__":
    main()
