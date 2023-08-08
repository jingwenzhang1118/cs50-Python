amount = 0
while True:
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        amount += coin
    if amount < 50:
        print("Amount Due:", 50 - amount)
    else:
        break
print("Change Owed:", amount - 50)
