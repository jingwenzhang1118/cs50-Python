text = input("Input: ")

short_text = ""
for c in text:
    if c.lower() not in ["a", "e", "i", "o", "u"]:
        short_text = short_text + c
print("Output:", short_text)
