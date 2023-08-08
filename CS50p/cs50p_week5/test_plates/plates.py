import string

def main():
    if is_valid(input("Plate: ").strip().upper()):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    n = len(s)
    check = True
    if s[0:2].isalpha() and 2 <= n <= 6:
        for i in range(2, n):
            if s[i].isdigit():
                if s[i] == "0":
                    check = False
                elif s[i] != "0" and s[i:].isdigit() == False:
                    check = False
                # breaks after finding the first digit
                break
            elif s[i].isalpha() == False:
                check = False
    else:
        check = False
    return check


if __name__ == "__main__":
    main()