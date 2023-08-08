import random
import sys


while True:
    try:
        level = input("Level: ")
        n = random.randint(1, int(level))
        break
    except ValueError:
        pass


while True:
    try:
        guess = int(input("Guess: "))
        if guess < n:
            print("Too small!")
        elif guess > n:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()
    except ValueError:
        pass
