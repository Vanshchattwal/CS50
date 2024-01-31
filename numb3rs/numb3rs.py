import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    # from 1 to 255 sep with .
    digits = re.match(r"(\d*)\.(\d*)\.(\d*)\.(\d*)", ip)

    for i in range(1, 5):
        # print(digits[i])
        try:
            if 255 < int(digits[i]) or int(digits[i]) < 0:
                return False
        except:
            return False

    # print(int(digits[2]))
    # print(digits)
    return True


if __name__ == "__main__":
    main()
