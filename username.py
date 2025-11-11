# Username Generator and Text Analyzer

# Step 1: Input user details
word = input("Enter your first name: ")
special = input("Enter your last name: ")
digit = input("Enter your favorite word: ")

# Step 2: Use slicing and indexing
part1 = word[:3]  
part2 = special[-3:]
symbol = "@"  

# Step 3: Combine using f-string (string formatting)
username = f"{part1.lower()}{symbol}{part2.upper()}_{word[::-1]}"  
print(f"\nGenerated Username: {username}")

# Step 4: String method demonstrations
print("\n--- String Method Demonstrations ---")
print(f"Uppercase version: {username.upper()}")
print(f"Lowercase version: {username.lower()}")
print(f"Replace '@' with '#': {username.replace('@', '#')}")
print(f"Reversed Username: {username[::-1]}")