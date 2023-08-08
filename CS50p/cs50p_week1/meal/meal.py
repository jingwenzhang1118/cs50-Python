'''
def main():
    answer = input("What time is it? ").split(":")
    answer[0] = int(answer[0])
    answer[1] = int(answer[1])
    convert(answer)



def convert(time):
    if time[0] == 7 or (time[0] == 8 and time[1] == 0):
        print("breakfast time")
    elif time[0] == 12 or (time[0] == 13 and time[1] == 0):
        print("lunch time")
    elif time[0] == 18 or (time[0] == 19 and time[1] == 0):
        print("dinner time")
'''

def main():
    answer = input("What time is it? ")
    time_converted = convert(answer)
    if 7 <= time_converted <= 8:
        print("breakfast time")
    elif 12 <= time_converted <= 13:
        print("lunch time")
    elif 18 <= time_converted <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    time_converted = float(hours) + float(minutes) / 60
    return time_converted



if __name__ == "__main__":
    main()


