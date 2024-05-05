import sys
import random
if __name__ == "__main__":
    i = 0
    correct_guess = random.randint(1, 20)
    while i < 5:
        i += 1
        secret_number = int(input("Guess a number from 1 - 20: "))

        if random == secret_number:
            print("You're guessed right!")
            sys.exit(0)
        else:
            print("You failed to guess the number!")
