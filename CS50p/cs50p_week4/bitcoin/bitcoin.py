import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

while True:
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        break
    except requests.RequestException:
        pass
o = r.json()
price = float(o["bpi"]["USD"]["rate"].replace(",", "")) * n
print(f"${price:,.4f}")
