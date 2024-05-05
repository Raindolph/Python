if __name__ == "__main__":
    food = "rice", "beans", "agusi", "bitaleaf"
    soft_drinks = "fanta", "Puka", "Pepsi", "Tampico", "Don simon"

    # union or join
    free = food + soft_drinks
    print(free)

    # count the number of elements in a tuple
    lenfree = len(free)
    print(lenfree)

    # Removing An element from a tuple
    food_list = list(foods)
    food_list.remove("beans")
    print(food_list)

    # Adding an element to a tuple
    food_list.append("Soup")
    print(food_list)
