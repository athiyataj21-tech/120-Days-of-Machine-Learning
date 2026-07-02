"""
Day 2 Practice
Python Operators
"""

# Arithmetic Operators

a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

print("-" * 40)

# Assignment Operators

x = 10
x += 5
print("After += :", x)

x *= 2
print("After *= :", x)

print("-" * 40)

# Comparison Operators

print(a > b)
print(a == b)
print(a != b)

print("-" * 40)

# Logical Operators

age = 22

print(age > 18 and age < 30)
print(age > 25 or age < 30)
print(not age > 18)

print("-" * 40)

# Identity Operators

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)
print(list1 is list3)

print("-" * 40)

# Membership Operators

fruits = ["apple", "banana", "orange"]

print("apple" in fruits)
print("grapes" not in fruits)

print("-" * 40)

# Bitwise Operators

print(5 & 3)
print(5 | 3)
print(5 ^ 3)