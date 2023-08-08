import sys

def main():
    if is_valid():
        print(get_numlines(sys.argv[1]))


def is_valid():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")
    else:
        return True


def get_numlines(document):
    numlines = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.strip() != "" and line.strip().startswith("#") == False:
                    numlines += 1
            return numlines
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()