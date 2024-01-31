import requests
import sys


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


try:
    # ask for input
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif is_float((sys.argv[1])) == True:
        q = float(sys.argv[1])
    else:
        sys.exit("command-line argument is not a number")

    price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    o = price.json()

    for result in o["bpi"]:
        bpi = o["bpi"]
        for s in bpi["USD"]:
            t = bpi["USD"]

    btc = (t["rate_float"]) * q

    print(f"${btc:,.4f}")

except requests.RequestException:
    pass
