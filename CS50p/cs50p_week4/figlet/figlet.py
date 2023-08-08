from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
if len(sys.argv) == 2 or len(sys.argv) > 3:
    sys.exit("Not the expected number of arguments.")
elif len(sys.argv) == 3 and (
    sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in figlet.getFonts()
):
    sys.exit("Wrong font.")

text = input("Input: ")

if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
else:
    f = sys.argv[2]

figlet.setFont(font=f)
print(figlet.renderText(text))
