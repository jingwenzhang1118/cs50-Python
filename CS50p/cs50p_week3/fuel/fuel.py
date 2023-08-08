def main():
    x = get_frac("Fraction: ")
    if x <= 1:
        print("E")
    elif 99 <= x <= 100:
        print("F")
    else:
        print(f"{x}%")


def get_frac(prompt):
    while True:
        try:
            num, denom = input(prompt).split('/')
            # Assume the input is correct and define the accepted range of data, otherwise continue the loop
            if 0 <= int(num) <= int(denom):
                return round(int(num) / int(denom) * 100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()

'''
while True:
    try:
        frac = input("Fraction: ")
        x, y = frac.split(sep="/")
        output = round(int(x) / int(y) * 100)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    except frac.find("/") == False:
        pass
    if int(x) > int(y):
        pass
    else:
        break






main()
'''