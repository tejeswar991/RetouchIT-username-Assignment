students = {}
classes = set()

while True:
    print("\n1. Add Student")
    print("2. Show All Students")
    print("3. Show Unique Classes")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        class_name = input("Enter Class: ")

        students[roll] = name
        classes.add(class_name)

        print("Student Added!")

    elif choice == "2":
        print("\n--- Student List ---")
        for roll, name in students.items():
            print(roll, ":", name)

    elif choice == "3":
        print("\nUnique Classes:", classes)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")