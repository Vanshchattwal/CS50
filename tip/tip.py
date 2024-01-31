def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    p = d.replace("$", " ")
    return float(p)


def percent_to_float(p):
    f = float(p.replace("%"," "))
    return (f/100)


main()