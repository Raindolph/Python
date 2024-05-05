
if __name__ == "__main__":
    string1 = input("Enter a random phrase: ")
    string2 = input("Enter a phrase to be appended: ")
    num = int(input("Enter the number of characters to append: "))
    string1 += string2[0:num]
    print(string1)
