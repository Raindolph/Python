import sys

if __name__ == "__main__":
    print("   Diary  ")
    notes = input("Provide your notes (100 characters): ")
    if len(notes) >= 100:
        print("Character limit reached!")
    else:
        sys.exit(0)
