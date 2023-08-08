import csv
import sys
from tabulate import tabulate

def main():
    if is_valid():
        get_table(sys.argv[1])


def is_valid():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    else:
        return True

def get_table(document):
    menus = []
    try:
        with open(document) as file:
            reader = csv.DictReader(file)
            for _ in reader:
                menus.append(_)
        # set headers to be the keys, possible as it is a dictionary.
        print(tabulate(menus, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

