while True:
    fuel = input("Fraction :")
    try:
        x, y = fuel.split("/")
        x = int(x)
        y = int(y)
        if x <= y:
            break
    except (ValueError, ZeroDivisionError):
        pass
z = round(100 / y * x)
if z <= 1:
    print("E")
elif z >= 99:
    print("F")
else:
    print(z, "%", sep="")
