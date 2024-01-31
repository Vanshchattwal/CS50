import csv
import sys

# Each nucleotide of DNA contains one of four different bases
# genome vary similar in all

# match sequence from .txt file with names in .csv file then print name

def main():

    # pehle me .csv then txt file folder
    if len(sys.argv) > 3:
        sys.exit("Too much command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        if (sys.argv[1].endswith(".csv") == True and sys.argv[2].endswith(".txt") == True):
            data = "/workspaces/124705098/dna/databases/" + sys.argv[1]
            toreadfrm = "/workspaces/124705098/dna/sequences/" + sys.argv[2]
        else:
            sys.exit("Invalid Arguments")

    # Read database file into a variable
    rows = []
    with open(data) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    # print(rows)

    # Read DNA sequence file into a variable
    with open(toreadfrm) as trfile:
        toreadfrom = trfile.read()


    # Find longest match of each STR in DNA sequence
    res = longest_match(toreadfrom, rows)
    print(res)

    # TODO: Check database for matching profiles

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence) #text file
    sequence_length = len(sequence) #csv file

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
