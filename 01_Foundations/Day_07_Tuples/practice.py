print("===== Day 7 - Tuples =====")

# Creating Tuples
numbers = (10, 20, 30, 40, 50)
print(numbers)

# Mixed Tuple
data = ("Athiya", 22, 8.5, True)
print(data)

# Single Element Tuple
single = (100,)
print(single)

# Access Elements
print(numbers[0])
print(numbers[-1])

# Slicing
print(numbers[1:4])
print(numbers[::-1])

# Length
print(len(numbers))

# Membership
print(20 in numbers)
print(60 not in numbers)

# Loop
for num in numbers:
    print(num)

# Concatenation
a = (1,2)
b = (3,4)
print(a+b)

# Repetition
print(a*3)

# Packing
person = "Athiya",22,"Engineer"
print(person)

# Unpacking
name,age,profession = person

print(name)
print(age)
print(profession)

# Nested Tuple
students = (
    ("Athiya",22),
    ("Rahul",23)
)

print(students[0])
print(students[1][0])

# count()
nums = (1,2,2,3,2,4)

print(nums.count(2))

# index()
print(nums.index(3))

# Built-in Functions
values = (5,8,2,9,1)

print(min(values))
print(max(values))
print(sum(values))
print(sorted(values))

# Conversion
lst = list(values)
print(lst)

tp = tuple(lst)
print(tp)

# Tuple Immutability

try:
    values[0] = 100
except TypeError as e:
    print("Error:", e)

print("Day 7 Completed Successfully!")