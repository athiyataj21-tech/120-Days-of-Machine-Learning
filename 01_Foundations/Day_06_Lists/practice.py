# Day 06 - Lists Practice

# Creating Lists
fruits = ["Apple", "Banana", "Orange"]

print(fruits)

# Accessing
print(fruits[0])
print(fruits[-1])

# Updating
fruits[1] = "Mango"
print(fruits)

# Append
fruits.append("Grapes")
print(fruits)

# Insert
fruits.insert(1, "Kiwi")
print(fruits)

# Extend
fruits.extend(["Pineapple", "Guava"])
print(fruits)

# Remove
fruits.remove("Apple")
print(fruits)

# Pop
removed = fruits.pop()
print("Removed:", removed)
print(fruits)

# Length
print(len(fruits))

# Sorting
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)

# Reverse
numbers.reverse()
print(numbers)

# Count
nums = [1, 2, 2, 3, 2]
print(nums.count(2))

# Index
print(nums.index(3))

# Nested List
matrix = [[1, 2], [3, 4]]
print(matrix[0][1])

# List Comprehension
squares = [x*x for x in range(10)]
print(squares)

# Even Numbers
even = [x for x in range(20) if x % 2 == 0]
print(even)

# Loop
for fruit in fruits:
    print(fruit)

# Membership
print("Mango" in fruits)

# Copy
copy_list = fruits.copy()
print(copy_list)

# Clear
temp = [1, 2, 3]
temp.clear()
print(temp)