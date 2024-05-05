import sys


def first_name_validator(firstname):
    if firstname.isalpha():
        return firstname
    else:
        print("invalid!")
        sys.exit(0)


def last_name_validator(lastname):
    if lastname.isalpha():
        return lastname
    else:
        print("Invalid!")
        sys.exit(0)


def password_validator(_password):
    if len(password) < 8:
        print("Invalid!")

    if password.isalpha() or password.isalnum():
        print("weak password")
    elif password.isalnum():
        print("Normal password")
    else:
        print("Strong password")


def month_validator(_month):
    if _month > 12:
        print("Error!")
        sys.exit(0)
    else:
        return _month


def year_validator(years):
    if years.isalpha():
        print("Unacceptable!")
        sys.exit(0)
    if int(years) > 2023:
        print("You cant be from the future")
    else:
        return years
    sys.exit(0)


def email_validator(email):
    if "@" in e_mail and e_mail.endswith(".com"):
        return e_mail
    else:
        print("Invalid")
        sys.exit(0)


def day_validator(_day):
    if days > "31":
        print("Error!")
        sys.exit(0)
    else:
        return days


if __name__ == "__main__":
    first_name = input("Enter your name: ")
    last_name = input("Enter last name: ")
    year = input("Enter your birth year: ")
    month = int(input("Enter your birth month: "))
    days = input("Enter your birth day: ")
    e_mail = input("Enter your e-mail Address: ")
    password = input("Enter password: ")

    print(first_name_validator(first_name))
    print(last_name_validator(last_name))
    print(year_validator(year))
    print(month_validator(month))
    print(day_validator(days))
    print(year, month, days)
    print(email_validator(e_mail))



