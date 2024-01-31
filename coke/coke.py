left = 50
paid = 0
cost = 50

while True:
    print("Amount Due:", left)
    insert = int(input("Insert Coin:"))
    if insert == 25 or insert == 10 or insert == 5:
        paid = insert + paid
        left = cost - paid
    else:
        continue

    if left <= 0:
        print("Change Owed:", (left - left*2))
        break
    else:
        continue

