from datetime import date, datetime
import inflect, re, sys


def main():
    birth = check_birth(input("Date of birth: "))
    print(minutes(birth))


def check_birth(input):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", input) != None:
            return input
    else:
        sys.exit("Invalid date")


def minutes(s):
    try:
        # as the time of the day is set to midnight, so it is sufficient to only focus on dates without time info.
        birth_date = datetime.strptime(s, "%Y-%m-%d").date()
        minutes_dif = (date.today() - birth_date).days * 24 * 60
        # minutes_dif = ((date.today() - birth_date).total_seconds())/60
        p = inflect.engine()
        return f"{p.number_to_words(minutes_dif, andword='').capitalize()} minutes"
    except Exception:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()


