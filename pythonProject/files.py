if __name__ == "__main__":
    file = open("Writer.py", "w")
    text = "if __name__ == '__main__':\n\trandom = input('Enter any random sentence: ')\n\tprint(random)"
    file.write(text)
    file.close()
