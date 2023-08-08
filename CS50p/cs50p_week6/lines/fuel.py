def main():
    while True:
        try:
            frac = convert(input("Fraction: ").strip())
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(frac))


def convert(fraction):
    num, denom = fraction.split("/")
    if 0 <= int(num) <= int(denom):
        return round(int(num) / int(denom) * 100)
    elif int(denom) == 0:
        raise ZeroDivisionError
    else:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()