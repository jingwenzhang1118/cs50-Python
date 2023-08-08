def main():
    print(shorten(input("Input: ")))


def shorten(word):
    short_text = ""
    for c in word:
        if c.lower() not in ["a", "e", "i", "o", "u"]:
            short_text = short_text + c
    return short_text


if __name__ == "__main__":
    main()