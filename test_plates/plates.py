def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # start with atlesat two letters
    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    # if s[len(s) - 1].isalpha() == True:
    #     return False
    n = int(len(s) / 2)
    if s[n - 1].isalpha() == False:
        return False

    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i = i + 1

    if s.isalnum() == False:
        return False

    return True

    # if plate[0:2] != "0":
    # # max 6 len & minimum 2 letter
    #     if len(plate) <= 6:
    #         # last char must be number
    #         if 9 >= plate[len(plate)] >= 0:
    #              # num must not start with 0 (if there is any letter before 0 means invalid)
    #              j = 0
    #              for i in plate:
    #                 if 9 >= i >= 0:
    #                      if plate[j-1]
    #                 j = j + 1


# No periods, spaces, or punctuation marks are allowed
if __name__ == "__main__":
    main()
