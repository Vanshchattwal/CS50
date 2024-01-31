import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

valid_cla = ["--font", "-f"]
# text = list((input("Input: ")).split())
# generate random
try:
    if len(sys.argv) == 1:
        # print(sys.argv[0])
        # select random font from list
        style = random.choice(figlet.getFonts())
        # print(i)
        # print(figlet.getFonts()[i])
        figlet.setFont(font=style)
        text = input("Input: ")
        print(figlet.renderText(text))
    # generate using iput
    elif len(sys.argv) == 3:
        if sys.argv[1] in valid_cla:
            if sys.argv[2] in figlet.getFonts():
                figlet.setFont(font=sys.argv[2])
                text = input("Input: ")
                print(figlet.renderText(text))
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

except:
    sys.exit("Invalid usage")
    # f = Figlet(font='slant')
    # print f.renderText('text to render')
