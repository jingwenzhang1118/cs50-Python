answer = input("Expression: ").split()
x = int(answer[0])
z = int(answer[2])

if answer[1] == "+":
    print(f"{float(x + z):.1f}")
elif answer[1] == "/":
    print(f"{float(x / z):.1f}")
elif answer[1] == "*":
    print(f"{float(x * z):.1f}")
else:
    print(f"{float(x - z):.1f}")
