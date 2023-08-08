month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()
        if date[0].isdigit():
            mon, day, year = date.split('/')
            if 0 <= int(mon) <= 12 and 0 <= int(day) <= 31 and int(year) > 0:
                print(f"{year}-{int(mon):02}-{int(day):02}")
                break
        elif date[0].isalpha():
            mon, day, year = date.split()
            day = int(day[:-1])
            if mon in month and 0 <= day <= 31 and int(year) > 0:
                print(f"{year}-{(month.index(mon) + 1):02}-{day:02}")
                break
    except ValueError:
        pass


