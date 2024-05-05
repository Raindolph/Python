import sys

if __name__ == "__main__":
    first_name = input("Enter your first name: ")
    if first_name.isalpha():
        print(first_name)
    else:
        print("Invalid!")
        sys.exit(0)
    last_name = input("Enter your last name: ")
    if last_name.isalpha():
        print(last_name)
    else:
        print("Invalid!")
        sys.exit(0)
    year = input("Enter Birth year: ")
    if year.isalpha():
        print("Unacceptable!")
        sys.exit(0)
    if int(year) > 2023:
        print("You cant be from the future...")
        sys.exit(0)
    month = int(input("Enter your month(Numeric representation): "))
    if month > 12:
        print("Error!")
        sys.exit(0)
    days = input("Enter your day of birth: ")
    if days > "31":
        print("Error!")
        sys.exit(0)
    print(year, month, days)

    e_mail = input("Enter your email address: ")
    if "@" in e_mail and e_mail.endswith(".com"):
        print("")
    else:
        print("Invalid!")
        sys.exit(0)
    password = input("Enter password ")
    if len(password) < 8:
        print("Invalid")
    if password.isalpha() or password.isnumeric():
        print("weak password")
    elif password.isalnum():
        print("Normal password")
    else:
        print("strong password")
