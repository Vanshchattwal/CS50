def main():
    time = input("What time is it ?")
    x = convert(time)
    
    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
       print("dinner time")


def convert(time):

    hours, minutes = time.split(":")
    nminute = float(float(minutes)/60)

    op = float(hours) + nminute
    return op

if __name__ == "__main__":
    main()