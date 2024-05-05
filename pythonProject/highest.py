
if __name__ == '__main__':
    print(" ENTER A NUMBER TO DETERMINE THE HIGHEST ")
    print(" _______________________________________ ")
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))
    fourth_number = int(input("Enter the fourth number: "))
    if first_number > second_number and first_number > third_number and first_number > fourth_number:
        print(first_number, "Is the highest number ")
    if second_number > first_number and second_number > third_number and second_number > fourth_number:
        print(second_number, "is the highest number ")
    if third_number > first_number and third_number > second_number and third_number > fourth_number:
        print(third_number, "is the highest number ")
    if fourth_number > first_number and fourth_number > second_number and fourth_number > third_number:
        print(fourth_number, "is the highest number ")


