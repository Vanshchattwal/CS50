import random


def main():
    score = 0
    p = get_level()

    for i in range(10):
        pr = generate_integer(p)

        wrong = 0
        while True:
            try:
                print(pr, end="")
                answer = int(input())
                if answer == z:
                    score = score + 1
                    break
                else:
                    wrong = wrong + 1
                    if wrong == 3:
                        print(f"{pr}{z}")
                        break
                    else:
                        print("EEE")
            except ValueError:
                wrong = wrong + 1
                if wrong == 3:
                    print(f"{pr}{z}")
                    break
                else:
                    print("EEE")

    print("Score:", score)


def get_level():
    valid_levels = {1, 2, 3}
    # ask for lever until it is from 1,2 or 3
    while True:
        try:
            level = int(input("Level: "))
            if level in valid_levels:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(p):
    global z
    if p == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif p == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    z = x + y

    return f"{x} + {y} = "


if __name__ == "__main__":
    main()
