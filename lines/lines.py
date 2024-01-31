import sys

if len(sys.argv) == 2:
    d = 0
    if (sys.argv[1]).endswith(".py") == True:
        try:
            f = open(sys.argv[1])
            for lines in f.readlines():
                if lines.strip().startswith("#") or lines == "\n":
                    continue
                else:
                    d = d + 1
            print(d)
        except:
            sys.exit("File does mot exist")
    else:
        sys.exit("Not a python file")

else:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")
