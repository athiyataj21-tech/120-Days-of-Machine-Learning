"""
Day 4 - Python Loops
Practice Programs
"""

# ==========================================
# Program 1: Print Numbers from 1 to 10
# ==========================================

for i in range(1, 11):
    print(i)

print("-" * 40)

# ==========================================
# Program 2: Print Numbers from 10 to 1
# ==========================================

for i in range(10, 0, -1):
    print(i)

print("-" * 40)

# ==========================================
# Program 3: Print Even Numbers
# ==========================================

for i in range(2, 21, 2):
    print(i)

print("-" * 40)

# ==========================================
# Program 4: Print Odd Numbers
# ==========================================

for i in range(1, 20, 2):
    print(i)

print("-" * 40)

# ==========================================
# Program 5: Sum of First 10 Numbers
# ==========================================

total = 0

for i in range(1, 11):
    total += i

print("Sum =", total)

print("-" * 40)

# ==========================================
# Program 6: Multiplication Table
# ==========================================

num = 5

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("-" * 40)

# ==========================================
# Program 7: Factorial
# ==========================================

number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial =", factorial)

print("-" * 40)

# ==========================================
# Program 8: Fibonacci Series
# ==========================================

a = 0
b = 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

print("\n" + "-" * 40)

# ==========================================
# Program 9: Count Digits
# ==========================================

number = 98765
count = 0

while number > 0:
    number //= 10
    count += 1

print("Digits =", count)

print("-" * 40)

# ==========================================
# Program 10: Reverse a Number
# ==========================================

number = 12345
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Reverse =", reverse)

print("-" * 40)

# ==========================================
# Program 11: Reverse a String
# ==========================================

text = "Python"

for char in reversed(text):
    print(char, end="")

print("\n" + "-" * 40)

# ==========================================
# Program 12: Count Vowels
# ==========================================

text = "Machine Learning"

count = 0

for letter in text.lower():
    if letter in "aeiou":
        count += 1

print("Vowels =", count)

print("-" * 40)

# ==========================================
# Program 13: Check Prime Number
# ==========================================

number = 17

is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime Number")
else:
    print("Not Prime")

print("-" * 40)

# ==========================================
# Program 14: Print Square Pattern
# ==========================================

for i in range(5):
    print("* " * 5)

print("-" * 40)

# ==========================================
# Program 15: Right Triangle Pattern
# ==========================================

for i in range(1, 6):
    print("* " * i)

print("-" * 40)

# ==========================================
# Program 16: Inverted Triangle
# ==========================================

for i in range(5, 0, -1):
    print("* " * i)

print("-" * 40)

# ==========================================
# Program 17: Number Triangle
# ==========================================

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("-" * 40)

# ==========================================
# Program 18: Print Characters of a String
# ==========================================

word = "Python"

for letter in word:
    print(letter)

print("-" * 40)

# ==========================================
# Program 19: Iterate Through List
# ==========================================

languages = ["Python", "Java", "C++", "R"]

for language in languages:
    print(language)

print("-" * 40)

# ==========================================
# Program 20: Iterate Dictionary
# ==========================================

student = {
    "Name": "Athiya",
    "Age": 21,
    "Course": "Machine Learning"
}

for key, value in student.items():
    print(key, ":", value)

print("-" * 40)

# ==========================================
# Program 21: break Statement
# ==========================================

for i in range(10):

    if i == 5:
        break

    print(i)

print("-" * 40)

# ==========================================
# Program 22: continue Statement
# ==========================================

for i in range(10):

    if i % 2 == 0:
        continue

    print(i)

print("-" * 40)

# ==========================================
# Program 23: pass Statement
# ==========================================

for i in range(5):
    pass

print("Loop Finished")

print("-" * 40)

# ==========================================
# Program 24: Print Squares
# ==========================================

for i in range(1, 11):
    print(i ** 2)

print("-" * 40)

# ==========================================
# Program 25: Print Cubes
# ==========================================

for i in range(1, 11):
    print(i ** 3)

print("-" * 40)

# ==========================================
# Program 26: Sum of Even Numbers
# ==========================================

total = 0

for i in range(2, 21, 2):
    total += i

print("Sum =", total)

print("-" * 40)

# ==========================================
# Program 27: Sum of Odd Numbers
# ==========================================

total = 0

for i in range(1, 20, 2):
    total += i

print("Sum =", total)

print("-" * 40)

# ==========================================
# Program 28: Countdown Timer
# ==========================================

for i in range(10, 0, -1):
    print(i)

print("Time's Up!")

print("-" * 40)

# ==========================================
# Program 29: Nested Loop
# ==========================================

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

print("-" * 40)

# ==========================================
# Program 30: Find Largest Number
# ==========================================

numbers = [12, 45, 67, 23, 89, 10]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest Number =", largest)

print("-" * 40)

print("🎉 Day 4 Practice Completed!")