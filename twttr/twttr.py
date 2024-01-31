import re

def main():
    get_input = input("Input: ").strip().lower()
    w = shorten(get_input)
    print("Output:", end="")
    print(w)


def shorten(get_input):

    i = re.sub("[aeiou]", "", get_input)
    return i


if __name__ == "__main__":
    main()


