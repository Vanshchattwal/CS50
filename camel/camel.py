inpt = input("camelCase: ").strip()

print("snake_case: ", end="")

for i in inpt:
    if i == i.upper():
        print("_"+i.lower(), end="")
    else:
        print(i, end="")