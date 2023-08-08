import csv
import sys


def main():
    if is_valid():
        write_csv(get_dict(sys.argv[1]), sys.argv[2])


def is_valid():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 4:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a csv file")
    else:
        return True


def get_dict(document):
    try:
        students = []
        with open(document) as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                last, first = row["name"].split(", ")
                students.append({"first": first, "last": last, "house": row["house"]})
        return students
    except FileNotFoundError:
        sys.exit(f"Could not read {document}")


def write_csv(list, output):
    with open(output, "w") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list[0].keys())
        writer.writeheader()
        writer.writerows(list)


if __name__ == "__main__":
    main()
