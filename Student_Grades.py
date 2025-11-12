students = []  # List to store (name, grade) tuples

n = int(input("Enter number of students: "))

# Take student name and grade
for i in range(n):
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: ")) 
    students.append((name, grade))  # store as tuple

# Display all student details
print("\n--- Student Grades ---")
for s in students: 
    print("Name:", s[0], "| Grade:", s[1])

# Calculate and display class average : 
total = 0
for s in students:
    total += s[1] 
average = total / len(students)
print("\nClass Average:", round(average, 2)) 