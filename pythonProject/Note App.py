import sys
note_title = []
if __name__ == "__main__":
    while True:
        print("**** Pella note ****")
        print("1. Add Note "
              "\n2. Remove Note"
              "\n3. Update Note"
              "\n4. View All Note"
              "\n5. Exit App")
        choice = input("Select Mode from 1 - 5: ")
        if choice == "1":
            title = input("Enter Title: ")
            note_title.append(title)
            print("Note Saved successfully!")
        if choice == "2":
            remover = input("Enter Remove Title: ")
            if remover in note_title:
                note_title.remove(remover)
                print("Note title removed!")
            else:
                print("Note Title not found!")
        if choice == "3":
            previous = input("Enter previous title: ")
            if previous in note_title:
                new = input("Enter new title: ")
                note_title[note_title.index(previous)] = new
                print("Update Successful!")
            else:
                print("The list is empty!")
        if choice == "4":
            print(note_title)
        if choice == "5":
            sys.exit(0)

