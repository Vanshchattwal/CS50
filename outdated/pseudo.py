months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
    # prompt for input
        date = input("Date : ").title().replace(",", "").replace("/", " ")
        x = date.split(" ")
        #date = input("Date : ").replace(",", "")

        # check if it first is int or char
        if x[0] in months:
            #     if char seperate from space and remove comma
            x[1] = int(x[1])
        #     after that check if month is from months list, day is under 32 if not reprompt
            if x[1] < 32 :
        #     if yes print then break
                x[0] = 1 + (months.index(x))
                p = "{year}-{month:02}-{day:02}"
                print(p.format(year=x[2], month=x[0], day=x[1]))

            # else:
            #     return False


        else:
            #     if int seperate from /
            #     after that check if month upto 12, day is under 32 if not reprompt
            x[0] = int(x[0])
            x[1] = int(x[1])
            if x[0] < 13 and x[1] < 32 :
                #     if yes print then break
                p = "{year}-{month:02}-{day:02}"
                print(p.format(year=x[2], month=x[0], day=x[1]))
                break

            # else:
            #     return False

    except:
        pass
