import random
import sys

# ask for difficulty , difficulty from 1 to 100 if its not +ve int re prompt
while True:
    try:
        Level = int(input("Level: "))

        # set x as random number between 1 to select difficulty
        x = random.randint(1, Level)

        while True:
            try:
                # ask for use guess if its less than x print too small if large to big if right correct and sys.exit if its not +ve int re prompt
                guess = int(input("Guess: "))
                if guess > x:
                    print("Too large!")
                elif guess < x:
                    print("Too small!")
                else:
                    print("Just right!")
                    sys.exit()
            except ValueError:
                True

    except ValueError:
        True
