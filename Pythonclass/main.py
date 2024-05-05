
if __name__ == "__main__":
    sentence = input("Enter a meaningful sentence: ")
    number_of_characters = len(sentence)
    print(number_of_characters)
    new = sentence.replace("r","b").replace("s","k").replace("a","e")
    print(new)
