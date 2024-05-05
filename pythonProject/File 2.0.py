if __name__ == "__main__":
    file = open("sample.txt", "r")
    text = "I am writing"
    output = file.read()
    print(len(output))
    output = file.read(12)
    print(output)
    file.close()
