import re


def main():
    get_input = input("Input: ").strip()
    w = shorten(get_input)
    print("Output:", end="")
    print(w)


def shorten(get_input):
    if get_input.isalpha() == True:
        i = re.sub("[aeiou]", "", get_input)
        return i
    else:
        exit(1)


if __name__ == "__main__":
    main()
