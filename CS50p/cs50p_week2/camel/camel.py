camelInput = input("camelCase: ")

snake_case = ""
for c in camelInput:
    if c.islower():
        snake_case = snake_case + c
    else:
        snake_case = snake_case + "_" + c.lower()

print(snake_case)
