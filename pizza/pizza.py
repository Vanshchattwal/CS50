import sys
import csv
from tabulate import tabulate

if len(sys.argv) > 2:
    sys.exit("Too much command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    if sys.argv[1].endswith(".csv") == True:
        try:
            with open(sys.argv[1], newline="") as f:
                reader = csv.reader(f)
                data = list(reader)
                print(tabulate(data, headers="firstrow", tablefmt="grid"))
        except:
            sys.exit("File not found")
    else:
        sys.exit("Not a CSV file")