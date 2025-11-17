library = {}    # create empty dictionary to store books

while True:
    print("\n1. Add Book")
    print("2. Remove Book")
    print("3. Search Book by Title")
    print("4. Update Book")
    print("5. Show All Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    # --- ADD  Books---
    if choice == "1":
        book_id = input("Enter Book ID: ")

        title = input("Enter Title: ")
        author = input("Enter Author: ")
        year = input("Enter Year: ")

        library[book_id] = {
            "title": title,
            "author": author,
            "year": year
        }

        print("Book Added!")

    # --- REMOVE ---
    elif choice == "2":
        book_id = input("Enter Book ID to remove: ")

        if book_id in library:
            library.pop(book_id)
            print("Book Removed!")
        else:
            print("Book not found!")

    # ---- SEARCH ----
    elif choice == "3":
        title = input("Enter Title to Search: ").lower()

        found = False
        for b_id in library:
            if library[b_id]["title"].lower() == title:
                print("\nBook ID:", b_id)
                print(library[b_id])
                found = True

        if not found:
            print("No book with that title!")

    # ---- UPDATE -----
    elif choice == "4":
        book_id = input("Enter Book ID to update: ")

        if book_id in library:
            new_title = input("Enter New Title: ")
            new_author = input("Enter New Author: ")
            new_year = input("Enter New Year: ")

            library[book_id]["title"] = new_title
            library[book_id]["author"] = new_author
            library[book_id]["year"] = new_year

            print("Book Updated!")
        else:
            print("Book ID not found!")

    # ---- SHOW ALL ----
    elif choice == "5":
        if not library:
            print("Library is Empty!")
        else:
            print("\n------ All Books ------")
            for b_id in library:
                print("Book ID:", b_id)
                print(library[b_id])
                print("-----------------------")

    # --- EXIT ----
    elif choice == "6":
        print("END Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")