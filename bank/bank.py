grt = input("Greeting: ").lower().strip()


if grt[0:5]=="hello":
    print("$0")
elif grt[0] == "h":
    print("$20")
else:
    print("$100")