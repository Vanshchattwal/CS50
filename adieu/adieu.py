import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        final = p.join(names)
        print("")
        print(f"Adieu, adieu, to {final}")
        break
