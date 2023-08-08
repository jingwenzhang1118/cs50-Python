import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # don't forget "\" before the period, otherwise period represents any char.
    # It needs to return four elements, otherwise matches do not exist.
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        # re.search(r"^([0-9]+).(([0-9]+).){2}([0-9]+)$", ip), the match also captures period ".".
        for match in matches.groups():
            # or re.search(r"^0[0-9]+", match), this is not needed to check
            if int(match) > 255 or int(match) < 0:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
