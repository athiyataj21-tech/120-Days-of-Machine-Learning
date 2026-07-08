# -----------------------------
# Day 08 - Dictionaries Practice
# -----------------------------

# Creating dictionaries
student = {
    "name": "Athiya",
    "age": 22,
    "course": "Machine Learning"
}

print(student)

# Accessing values
print(student["name"])
print(student.get("course"))

# Adding a key
student["city"] = "Bangalore"

print(student)

# Updating value
student["age"] = 23

print(student)

# Dictionary methods
print(student.keys())
print(student.values())
print(student.items())

# Looping

print("\nLooping through dictionary")

for key, value in student.items():
    print(key, ":", value)

# Membership

print("name" in student)
print("salary" in student)

# Removing

student.pop("city")

print(student)

# Copy

copy_student = student.copy()

print(copy_student)

# Nested Dictionary

students = {
    101: {"name": "Alice", "marks": 90},
    102: {"name": "Bob", "marks": 85},
}

print(students[101]["name"])

# Dictionary Comprehension

square = {x: x**2 for x in range(1, 11)}

print(square)

# Merge Dictionaries

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d1.update(d2)

print(d1)

# Count frequency of characters

text = "machinelearning"

freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print(freq)

# Student marks

marks = {
    "Math": 95,
    "Python": 98,
    "ML": 91,
}

total = sum(marks.values())

average = total / len(marks)

print("Total =", total)
print("Average =", average)

# Maximum marks

highest = max(marks, key=marks.get)

print("Highest Subject =", highest)