expression =(input("Expression: "))

x, y, z = expression.split(" ")

f = float(x)
s = float(z)

if y == "+":
    print(f+s)
elif y == "-":
    print(f-s)
elif y == "*":
    print(f*s)
elif y == "/":
    print(f/s)