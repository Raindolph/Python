if __name__ == "__main__":
    drinks = {"fanta", "Puka", "Pepsi", "Tampico", "Don simon"}
    sub_drinks = {"Puka", "Pepsi", "don simon"}

    #  print the items available in the first but not the second
    minus = drinks - sub_drinks
    print(minus)

    minuses = drinks.symmetric_difference(sub_drinks)
    print(minuses)

    inter = drinks.intersection(sub_drinks)
    print(inter)

