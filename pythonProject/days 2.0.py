# do the same with elif:
if __name__ == '__main__':
    data = int(input("Enter a number from 1 - 7: "))
    if data == 1:
        print("Sunday")
    elif data == 2:
        print("Monday")
    elif data == 3:
        print("Tuesday")
    elif data == 4:
        print("Wednesday")
    elif data == 5:
        print("Thursday")
    elif data == 6:
        print("Friday")
    elif data == 7:
        print("Saturday")
    else:
        print("Invalid!")
