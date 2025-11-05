age = int(input("Enter Your Age : "))
if age >= 18:
    print("Your are Eligible for Voting..")
elif age >= 13 and age < 18:
    print("Your are teenager...")
else:
    print("Your are Child...")