# Day 3 Practice - Conditional Statements

# 1. Positive, Negative or Zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 2. Even or Odd
num = int(input("\nEnter another number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Largest of Two Numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)


# 4. Largest of Three Numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# 5. Voting Eligibility
age = int(input("\nEnter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")


# 6. Grade Calculator
marks = int(input("\nEnter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


# 7. Login Authentication
username = input("\nUsername: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")


# 8. Simple Calculator
a = float(input("\nEnter first number: "))
op = input("Enter operator (+,-,*,/): ")
b = float(input("Enter second number: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Division by zero not allowed")
else:
    print("Invalid Operator")


# 9. BMI Calculator
weight = float(input("\nEnter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


# 10. Age Category

age = int(input("\nEnter age: "))

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")