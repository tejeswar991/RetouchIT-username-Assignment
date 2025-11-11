'''
a = int(input("Enter First Number :"))
b = int(input("Enter second number : "))

print("Addition : ", a+b)
print("Subtraction : ", a-b)
print("multiplication :",a*b)
print("Division :",a/b)
print("Floor Division :",a//b)
print("Modulus :",a%b)
print("Exponent : ", a**b) '''

# Comparison Operators :
'''
a = 10
b = 20

print(a == b)
print( a!= b)
print(a<b)
print(a > b)
print(a <= b)
print( a >= b) '''

# Logical Operator
'''
age = int(input("Enter Your Age : "))
if age >= 18:
    print("Your are Eligible for Voting..")
elif age >= 13 and age < 18:
    print("Your are Teenager...")
else:
    print("Your are Child...")'''

# Calculator Using Operators :
a = float(input("Enter First Number :"))
b = float(input("Enter Second Number :"))

operator = input("Enter Operator (+,-,*,/,//,%,**) : ")
if operator == '+':
    print("Addition : ", a+b)
elif operator == '-':
    print("Subtraction : ", a-b)
elif operator == '*':
    print("Multiplication : ", a*b)
elif operator == '/':
    print("Division : ", a/b)
elif operator == '//':
    print("Floor Division : ", a//b)
elif operator == '%':
    print("Modulus : ", a%b)
elif operator == '**':
    print("Exponent : ", a**b)