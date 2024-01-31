x = (input("What is the answer to the Great Question of Life, the Universe and Everything ?"))

y = x.title().strip()

if y == "42" or y == "Forty-Two" or y == "Forty Two":
    print("Yes")
else:
    print("NO")
