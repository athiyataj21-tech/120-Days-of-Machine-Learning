"""
===========================================
Day 09 - Python Sets
120 Days of Machine Learning
===========================================

Topics Covered:
1. Creating Sets
2. Empty Sets
3. Duplicate Removal
4. Adding Elements
5. Updating Sets
6. Removing Elements
7. Membership Operators
8. Set Operations
9. Subset & Superset
10. Disjoint Sets
11. Frozen Sets
12. Set Comprehension
13. Practical Examples
14. Practice Exercises
"""

print("=" * 50)
print("DAY 09 - PYTHON SETS")
print("=" * 50)


# =====================================
# 1. Creating Sets
# =====================================

print("\n1. Creating Sets")

fruits = {"Apple", "Banana", "Orange"}

print("Fruits:", fruits)


# =====================================
# 2. Empty Set
# =====================================

print("\n2. Empty Set")

empty_set = set()

print("Empty Set:", empty_set)
print(type(empty_set))


# =====================================
# 3. Duplicate Removal
# =====================================

print("\n3. Duplicate Removal")

numbers = {1, 2, 2, 3, 3, 4, 5, 5}

print(numbers)


# =====================================
# 4. Length of Set
# =====================================

print("\n4. Length")

print(len(numbers))


# =====================================
# 5. Membership Operator
# =====================================

print("\n5. Membership")

print(3 in numbers)

print(10 in numbers)

print(5 not in numbers)


# =====================================
# 6. Iterating Through Set
# =====================================

print("\n6. Iterating")

for fruit in fruits:
    print(fruit)


# =====================================
# 7. Adding Elements
# =====================================

print("\n7. add()")

fruits.add("Mango")

print(fruits)


# =====================================
# 8. Updating Set
# =====================================

print("\n8. update()")

fruits.update(["Kiwi", "Pineapple"])

print(fruits)


# =====================================
# 9. Removing Elements
# =====================================

print("\n9. remove()")

fruits.remove("Banana")

print(fruits)


# =====================================
# 10. discard()
# =====================================

print("\n10. discard()")

fruits.discard("Watermelon")

print(fruits)


# =====================================
# 11. pop()
# =====================================

print("\n11. pop()")

removed = fruits.pop()

print("Removed:", removed)

print(fruits)


# =====================================
# 12. clear()
# =====================================

print("\n12. clear()")

sample = {1, 2, 3}

sample.clear()

print(sample)


# =====================================
# 13. copy()
# =====================================

print("\n13. copy()")

A = {1, 2, 3}

B = A.copy()

print(B)


# =====================================
# 14. Union
# =====================================

print("\n14. Union")

A = {1, 2, 3}

B = {3, 4, 5}

print(A.union(B))

print(A | B)


# =====================================
# 15. Intersection
# =====================================

print("\n15. Intersection")

print(A.intersection(B))

print(A & B)


# =====================================
# 16. Difference
# =====================================

print("\n16. Difference")

print(A.difference(B))

print(A - B)


# =====================================
# 17. Symmetric Difference
# =====================================

print("\n17. Symmetric Difference")

print(A.symmetric_difference(B))

print(A ^ B)


# =====================================
# 18. Subset
# =====================================

print("\n18. Subset")

X = {1, 2}

Y = {1, 2, 3, 4}

print(X.issubset(Y))


# =====================================
# 19. Superset
# =====================================

print("\n19. Superset")

print(Y.issuperset(X))


# =====================================
# 20. Disjoint Set
# =====================================

print("\n20. Disjoint")

P = {1, 2}

Q = {5, 6}

print(P.isdisjoint(Q))


# =====================================
# 21. Frozen Set
# =====================================

print("\n21. Frozen Set")

F = frozenset([10, 20, 30])

print(F)


# =====================================
# 22. Set Comprehension
# =====================================

print("\n22. Set Comprehension")

square_set = {x ** 2 for x in range(1, 11)}

print(square_set)


# =====================================
# 23. Removing Duplicates
# =====================================

print("\n23. Removing Duplicates")

cities = [
    "Bangalore",
    "Delhi",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Mumbai"
]

unique_cities = set(cities)

print(unique_cities)


# =====================================
# 24. Common Subjects
# =====================================

print("\n24. Common Subjects")

student1 = {"Math", "Python", "AI"}

student2 = {"Python", "AI", "Physics"}

common = student1 & student2

print(common)


# =====================================
# 25. Unique Skills
# =====================================

print("\n25. Unique Skills")

employee1 = {"Python", "SQL", "Excel"}

employee2 = {"Python", "Power BI", "Tableau"}

print(employee1 ^ employee2)


# =====================================
# 26. Convert List to Set
# =====================================

print("\n26. List to Set")

my_list = [10, 20, 30, 10, 40, 50]

my_set = set(my_list)

print(my_set)


# =====================================
# 27. Convert String to Set
# =====================================

print("\n27. String to Set")

letters = set("MachineLearning")

print(letters)


# =====================================
# 28. Maximum and Minimum
# =====================================

print("\n28. max() and min()")

nums = {12, 45, 3, 78, 15}

print(max(nums))

print(min(nums))


# =====================================
# 29. Sum of Set
# =====================================

print("\n29. sum()")

print(sum(nums))


# =====================================
# 30. Sorting Set
# =====================================

print("\n30. sorted()")

print(sorted(nums))


# =====================================
# Practice Exercise 1
# =====================================

print("\nExercise 1")

colors = {"Red", "Blue"}

colors.add("Green")

colors.update(["Black", "White"])

print(colors)


# =====================================
# Practice Exercise 2
# =====================================

print("\nExercise 2")

A = {10, 20, 30}

B = {30, 40, 50}

print("Union:", A | B)

print("Intersection:", A & B)

print("Difference:", A - B)

print("Symmetric Difference:", A ^ B)


# =====================================
# Practice Exercise 3
# =====================================

print("\nExercise 3")

programming_languages = {
    "Python",
    "Java",
    "C++",
    "Python",
    "Java"
}

print(programming_languages)


# =====================================
# Mini Challenge 1
# =====================================

print("\nMini Challenge 1")

students = [
    "Ali",
    "Sara",
    "John",
    "Ali",
    "Sara",
    "David",
    "John"
]

unique_students = set(students)

print("Unique Students")

print(unique_students)


# =====================================
# Mini Challenge 2
# =====================================

print("\nMini Challenge 2")

online_users = {
    "Alice",
    "Bob",
    "Charlie",
    "David"
}

offline_users = {
    "Charlie",
    "Emma",
    "Frank",
    "Alice"
}

print("Online:", online_users)

print("Offline:", offline_users)

print("Common Users:", online_users & offline_users)

print("All Users:", online_users | offline_users)

print("Only Online:", online_users - offline_users)

print("Only Offline:", offline_users - online_users)

print("Exclusive Users:", online_users ^ offline_users)


# =====================================
# Mini Challenge 3
# =====================================

print("\nMini Challenge 3")

skills = {
    "Python",
    "SQL",
    "Machine Learning",
    "Python",
    "Power BI",
    "SQL",
    "Excel"
}

print(skills)

print("Total Unique Skills:", len(skills))


# =====================================
# End of Program
# =====================================

print("\n" + "=" * 50)
print("Congratulations! You have completed Day 09.")
print("Topics Covered:")
print("✔ Creating Sets")
print("✔ Adding and Removing Elements")
print("✔ Membership Operators")
print("✔ Set Operations")
print("✔ Frozen Sets")
print("✔ Set Comprehension")
print("✔ Practical Examples")
print("=" * 50)