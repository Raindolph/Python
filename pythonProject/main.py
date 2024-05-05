
if __name__ == '__main__':
    number = int(input("Guess the magic number from 1 - 10: "))
    magic_number = 7
    int(magic_number)
    if number == magic_number:
        print("Whoa! You're good at guessing")
    elif number != magic_number:
        print("You failed! ")
    else:
        print(" invalid ")
