import random
import sys


def main():
    digit = get_level()
    numq = 10
    score = 0
    while numq > 0:
        x = generate_integer(digit)
        y = generate_integer(digit)
        for i in range(0, 3):
            try:
                answer = input(f"{x} + {y} = ")
                if int(answer) == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        numq -= 1
        print(f"{x} + {y} = {x + y}")
    print(score)


def get_level():
    while True:
        try:
            digit = int(input("Level: "))
            if digit in range(1, 4):
                return digit
        except ValueError:
            pass


def generate_integer(level):
    try:
        if level == 1:
            return random.randrange(0, 10)
        elif level in [2, 3]:
            return random.randrange(10 ** (level - 1), 10**level)
        else:
            raise ValueError
    except ValueError:
        sys.exit()


if __name__ == "__main__":
    main()
