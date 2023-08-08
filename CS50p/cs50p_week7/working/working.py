import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    if matches := re.search(
        r"^([1-9][0-2]?):?([0-5][0-9])? ((?:A|P)M) to ([1-9][0-2]?):?([0-5][0-9])? ((?:A|P)M)$",
        s,
    ):
        s_hr = int(matches.group(1))
        s_min = int(matches.group(2)) if matches.group(2) else 0
        s_am = 1 if matches.group(3) == "AM" else 0
        e_hr = int(matches.group(4))
        e_min = int(matches.group(5)) if matches.group(5) else 0
        e_am = 1 if matches.group(6) == "AM" else 0
        if s_hr in range(1, 12):
            s_hr = s_hr + 12 * (1 - s_am)
        elif s_hr == 12:
            s_hr = 0 if s_am == 1 else 12
        else:
            raise ValueError

        if e_hr in range(1, 12):
            e_hr = e_hr + 12 * (1 - e_am)
        elif e_hr == 12:
            e_hr = 0 if e_am == 1 else 12
        else:
            raise ValueError

        return f"{s_hr:02}:{s_min:02} to {e_hr:02}:{e_min:02}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
