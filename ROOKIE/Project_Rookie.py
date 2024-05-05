if __name__ == '__main__':
    #  Hero's Inventory
    inventory = ()
    if not inventory:
        print("You're Empty handed")
        input("\nPress the enter key to continue. ")
        inventory = ("Sword",
                     "Armor",
                     "Shield",
                     "healing potion")
        print("\nThe inventory is:")
        print(inventory)
        print("\nYour items: ")
        for item in inventory:
            print(item)
        print("You have ", len(inventory), "Items in your inventory")
        print("\nPress the enter key to continue")
        if "healing potion" in inventory:
            print("You live to see another day")
            #  Display one item through index
            index = int(input("\nEnter the index number for an item in the inventory: "))
            print("At Index", index, "is", inventory[index])
            start = int(input("\nEnter the index number to begin a slice: "))
            finish = int(input("Enter the index number to end the slice: "))
            print("inventory[", start, ":", finish, "] is", end=" ")
            print(inventory[start:finish])
            print(input("\nPress on the enter key to continue "))
            # Concatenate tuples
            chest = ("gold", "gems")
            print("You find a chest and it contains:")
            print(chest)
            print("You add the contents of your chest to your inventory")
            inventory += chest
            print("Your inventory is now:")
            print(inventory)
            print("\n\n Press the enter key to exit")


