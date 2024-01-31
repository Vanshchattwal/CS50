import sys


def main():
    try:
        while True:
            number = input("Number: ")
            if number.isnumeric() != True:
                continue
            else:
                if len_valid(number) and card_name(number) != False:
                    n = validity(number)
                    if n % 10 == 0:
                        print(card_name(number))
                    else:
                        print("INVALID")
                else:
                    print("INVALID")
                break
    except:
        print("INVALID")


def len_valid(number):
    # no must be 13, 15, 16
    card_len = [13, 15, 16]
    if len(number) in card_len:
        return True
    else:
        return False


def card_name(number):
    inamex = ["4", "7"]
    inmst = ["1", "2", "3", "4", "5"]
    # [15 digits]American Express numbers start with 34 or 37
    if number[0] == "3" and number[1] in inamex:
        return "AMEX"
    # [13 and 16 digits]Visa numbers start with 4
    elif number[0] == "4":
        return "VISA"
    # [16 digits]MasterCard numbers start with 51, 52, 53, 54, or 55
    elif number[0] == "5" and number[1] in inmst:
        return "MASTERCARD"
    else:
        return False


def validity(number):
    # multiply every other digit by 2 starting with 2nd last digit

    # how can i reverse it ? txt = "Hello World"[::-1]
    rnumber = number[::-1]
    adddigi = 0
    addelse = 0
    for i in range(len(rnumber)):
        if i % 2 != 0:
            digi = int(rnumber[i]) * 2
            if digi > 9:
                a, b = str(digi)[0], str(digi)[1]
                digi = int(int(a) + int(b))
                adddigi = digi + adddigi
            else:
                adddigi = digi + adddigi
        else:
            digiplus = int(rnumber[i])
            addelse = addelse + digiplus
    r = adddigi + addelse
    return r


if __name__ == "__main__":
    main()


# add sum of remaining digits + sum of product of digits * 2

#  last digit is 0
