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


def day_validator(_day):
    if days > "31":
        print("Error!")
        sys.exit(0)
    else:
        return days


def email_validator(email):
    if "@" in e_mail and e_mail.endswith(".com"):
        return email
    else:
        print("Invalid")
        sys.exit(0)


def contact_validator(_contact):
    if contact.isnumeric():
        return contact
    else:
        print("Invalid!")


def question():
    questions = [
        "What is the temperature of the moon at night? (A. 1000 celsius B. -130 celsius C. -208 celsius) ",
        "How much is a dozen? (A. 6 B. 10 C. 12) ",
        "What is the smallest particle? (A. Molecules B. Dust C.Atom) ",
        "Who painted mona Lisa? (A. Pablo picasso B. Leonardo Da Vinci C. Albert Einstein) ",
        "Who is the God Of War? (A. Aries B. Kratos C. Poseidon) ",
        "Who invented a car? (A. Lazio biro B.The Wright brothers C. Carl Benz)",
        "A being from space is called? (A. Space beings B. Alien C.Astronauts) ",
        "What is the collective word for sheep (A. Congress B. Army C. Flock) ",
        "Which planet is the farthest from the sun (A. Jupiter B. Neptune C. Saturn) ",
        "What is the coldest place on earth (A. Antarctica B.Siberia C. Africa) ",
        "What is hardest part of the tooth ? (A. Pulp cavity B. Enamel  C. Gum) ",
        "How many continents are there? (A. 7 B. 6 C. 5) ",
        "A person from poland is called? (A. Pol B. Pollandian C.Polish)",
        "Where can the Eiffel tower be found ? (A. Germany B. France C. Berlin ) ",
        "Who was the first person to go to space (A.Neil Armstrong B. Tony Stark C. Peter Parker )",
        "Which of these are natural disasters ? (A. Mountains B. Tsunami C. Scorching )",
        "Who invented electricity ? (A. Benjamin Franklin B. Edward Newgate C. John Bell )",
        "Between the sun and lightning which is hotter (A. Sun B.lightning C. None)",
        "Which galaxy is our solar system located? (A. Andromeda B. B. Nebula C. Milky Way )",
        "Why is light faster in air than water (A. Density B.Volume C.Adhesion force )"


    ]

    options = [

        ["A. 1000 celsius B. -130 celsius C. -208 celsius"],
        ["A. 6 B. 10 C. 12"],
        ["A. Molecules B. Dust C.Atom"],
        ["A. Pablo picasso B. Leonardo Da Vinci C. Albert Einstein"],
        ["A. Aries B. Kratos C. Poseidon"],
        ["A. Lazio biro B.The Wright brothers C. Carl Benz"],
        ["A. Space beings B. Alien C.Astronauts"],
        ["A. Congress B. Army C. Flock"],
        ["A. Jupiter B. Neptune C. Saturn"],
        ["A. Antarctica B.Siberia C. Africa"],
        ["A. Pulp cavity B. Enamel  C. Gum "],
        ["A. 7 B. 6 C. 5"],
        ["A. Pol B. Pollandian C.Polish"],
        ["A. Germany B. France C. Berlin "],
        ["A.Neil Armstrong B. Tony Stark C. Peter Parker "],
        ["A. Mountains B. Tsunami C. Scorching"],
        ["A. Benjamin Franklin B. Edward Newgate C. John Bell"],
        ["A. Sun B.lightning C. None"],
        ["A. Andromeda B. B. Nebula C. Milky Way"],
        ["A. Density B.Volume C.Adhesion force"]


     ]

    correct_answers = ["b", "c", "c", "b", "a", "c", "b", "c", "b", "a", "b", "b", "c", "a", "b",
                       "a", "b", "a", "c", "a"]

    score = 0
    for i in range(len(questions)):
        print(f"\nQuestion {i + 1}: {questions[i]}")
        for option in options[i]:
            print(option)

        while True:
            user_answer = input("choose your answer ('a', 'b', 'c') ").lower()
            if user_answer in ['a', 'b', 'c']:
                break
            else:
                print("Error!")

        if user_answer == correct_answers[i]:
            print("Correct Answer!")
            score += 5
        else:
            print("Incorrect!")
    print(f"{first} you had {score} out of 100")
    if score >= 50:
        print("You passed")
    else:
        print("You failed!")


if __name__ == "__main__":
    first = input("Enter your Firstname: ")
    print(first_name_validator(first))
    last = input("Enter your lastname: ")
    print(last_name_validator(last))
    month = int(input("Enter your birth month: "))
    print(month_validator(month))
    year = input("Enter your birth year: ")
    print(year_validator(year))
    days = input("Enter your birth day: ")
    print(day_validator(days))
    e_mail = input("Enter your E-mail Address: ")
    print(email_validator(e_mail))
    contact = input("Provide your contact: ")
    print(contact_validator(contact))
    print(question())
