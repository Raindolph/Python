"""
          Accept and display the names of 10 people
           if name is james,stop asking
"""

if __name__ == '__main__':
   for a in range(10):
        name = input("Enter your name ")
        if name == "james":
            break
        print(name)
        print("Loop ended")
