def main():
    #text = input("Your text: ")
    #convert(text)
    convert(input("Your text: "))

def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    print(text)

main()