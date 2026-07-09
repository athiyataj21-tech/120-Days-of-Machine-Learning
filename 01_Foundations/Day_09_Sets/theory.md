# Day 09 — Python Sets

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand what Sets are in Python
- Create and initialize Sets
- Learn the properties of Sets
- Add, update, and remove elements
- Perform mathematical set operations
- Check subset, superset, and disjoint relationships
- Understand Frozen Sets
- Use Set Comprehensions
- Solve real-world problems using Sets
- Answer common Python interview questions

---

# 📖 Introduction to Sets

A **Set** is one of Python's built-in data structures used to store multiple items in a single variable.

Unlike Lists and Tuples, Sets store **only unique values** and do **not maintain any order**.

Python implements Sets using **Hash Tables**, making them extremely fast for searching, inserting, and deleting elements.

Example:

```python
fruits = {"Apple", "Banana", "Orange"}

print(fruits)
```

Output

```text
{'Apple', 'Banana', 'Orange'}
```

---

# Why Use Sets?

Sets are useful when:

- Removing duplicate values
- Performing mathematical operations
- Fast membership testing
- Comparing collections
- Finding common or unique elements

Example

```python
numbers = [1,2,2,3,4,5,5,6]

unique_numbers = set(numbers)

print(unique_numbers)
```

Output

```text
{1,2,3,4,5,6}
```

---

# Characteristics of Sets

Python Sets have the following properties:

- Unordered
- Mutable
- Unique elements only
- No indexing
- No slicing
- Fast lookup
- Cannot contain mutable data types

Example

```python
A = {1,2,3}

print(A)
```

---

# Creating Sets

## Method 1

Using curly braces

```python
colors = {"Red", "Green", "Blue"}

print(colors)
```

---

## Method 2

Using set()

```python
numbers = set([1,2,3,4])

print(numbers)
```

---

## Method 3

Creating from a String

```python
letters = set("Machine")

print(letters)
```

Output

```text
{'M','a','c','h','i','n','e'}
```

Duplicate letters are automatically removed.

---

# Creating an Empty Set

Incorrect

```python
A = {}
```

This creates a Dictionary.

Correct

```python
A = set()

print(type(A))
```

Output

```text
<class 'set'>
```

---

# Duplicate Values

Sets automatically remove duplicates.

Example

```python
numbers = {1,2,2,3,3,3,4,5}

print(numbers)
```

Output

```text
{1,2,3,4,5}
```

---

# Data Types Allowed in Sets

Allowed

```python
A = {1,2,3}

B = {"Python","Java"}

C = {True, False}

D = {(1,2),(3,4)}
```

---

Not Allowed

```python
A = {[1,2],[3,4]}
```

Output

```text
TypeError: unhashable type: 'list'
```

Lists, dictionaries, and sets cannot be elements of another set because they are mutable.

---

# Accessing Set Elements

Sets do not support indexing.

Wrong

```python
A = {10,20,30}

print(A[0])
```

Output

```text
TypeError
```

Correct method

```python
for item in A:
    print(item)
```

---

# Checking Membership

Use the **in** operator.

```python
numbers = {10,20,30,40}

print(20 in numbers)

print(100 in numbers)
```

Output

```text
True

False
```

---

# Adding Elements

Use **add()**

```python
fruits = {"Apple","Banana"}

fruits.add("Orange")

print(fruits)
```

Output

```text
{'Apple','Banana','Orange'}
```

---

# Adding Multiple Elements

Use **update()**

```python
fruits.update(["Mango","Kiwi","Grapes"])

print(fruits)
```

---

# Removing Elements

## remove()

```python
numbers = {1,2,3,4}

numbers.remove(2)

print(numbers)
```

Raises an error if the element is not present.

---

## discard()

```python
numbers.discard(10)
```

No error if the element does not exist.

---

## pop()

```python
numbers = {1,2,3}

removed = numbers.pop()

print(removed)

print(numbers)
```

Removes a random element because Sets are unordered.

---

## clear()

```python
numbers.clear()

print(numbers)
```

Output

```text
set()
```

---

# Copying a Set

```python
A = {1,2,3}

B = A.copy()

print(B)
```

---

# Length of a Set

```python
A = {1,2,3,4}

print(len(A))
```

Output

```text
4
```

---

# Set Operations

Python supports mathematical operations on Sets.

---

## Union

Combines all unique elements.

```python
A = {1,2,3}

B = {3,4,5}

print(A | B)
```

or

```python
print(A.union(B))
```

Output

```text
{1,2,3,4,5}
```

---

## Intersection

Returns common elements.

```python
print(A & B)
```

or

```python
print(A.intersection(B))
```

Output

```text
{3}
```

---

## Difference

Returns elements present only in the first Set.

```python
print(A - B)
```

Output

```text
{1,2}
```

---

## Symmetric Difference

Returns elements present in only one Set.

```python
print(A ^ B)
```

Output

```text
{1,2,4,5}
```

---

# Subset

Checks whether every element of one Set exists in another.

```python
A = {1,2}

B = {1,2,3}

print(A.issubset(B))
```

Output

```text
True
```

---

# Superset

```python
print(B.issuperset(A))
```

Output

```text
True
```

---

# Disjoint Sets

Returns True if no common elements exist.

```python
A = {1,2}

B = {5,6}

print(A.isdisjoint(B))
```

Output

```text
True
```

---

# Frozen Sets

A Frozen Set is an immutable version of a Set.

Once created, it cannot be modified.

```python
A = frozenset([1,2,3])

print(A)
```

Trying to modify it results in an error.

```python
A.add(4)
```

Output

```text
AttributeError
```

---

# Set Comprehension

Like List Comprehension but returns a Set.

Example

```python
squares = {x*x for x in range(6)}

print(squares)
```

Output

```text
{0,1,4,9,16,25}
```

---

# Practical Example 1

Removing duplicate student names.

```python
students = [
    "Ali",
    "Sara",
    "Ali",
    "John",
    "Sara"
]

unique_students = set(students)

print(unique_students)
```

Output

```text
{'Ali','Sara','John'}
```

---

# Practical Example 2

Finding common subjects.

```python
student1 = {"Math","Physics","Python"}

student2 = {"Python","Math","AI"}

print(student1 & student2)
```

Output

```text
{'Math','Python'}
```

---

# Practical Example 3

Finding unique skills.

```python
employee1 = {"Python","SQL","Excel"}

employee2 = {"Python","Power BI","Tableau"}

print(employee1 ^ employee2)
```

Output

```text
{'SQL','Excel','Power BI','Tableau'}
```

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Add | O(1) |
| Remove | O(1) |
| Search | O(1) |
| Union | O(n) |
| Intersection | O(min(n,m)) |
| Difference | O(n) |

---

# Common Set Methods

| Method | Description |
|---------|-------------|
| add() | Add one element |
| update() | Add multiple elements |
| remove() | Remove an element |
| discard() | Remove safely |
| pop() | Remove random element |
| clear() | Remove all elements |
| copy() | Copy the Set |
| union() | Combine Sets |
| intersection() | Common elements |
| difference() | Difference |
| symmetric_difference() | Unique elements |
| issubset() | Check subset |
| issuperset() | Check superset |
| isdisjoint() | Check common elements |

---

# Set vs List

| Feature | List | Set |
|----------|------|-----|
| Ordered | ✅ | ❌ |
| Duplicates | ✅ | ❌ |
| Indexing | ✅ | ❌ |
| Mutable | ✅ | ✅ |
| Fast Search | ❌ | ✅ |

---

# Common Mistakes

### Mistake 1

```python
A = {}
```

Creates a Dictionary instead of a Set.

Correct

```python
A = set()
```

---

### Mistake 2

Trying to access by index.

```python
A[0]
```

Not allowed.

---

### Mistake 3

Adding a list inside a Set.

```python
A = {[1,2]}
```

Raises TypeError.

---

# Interview Questions

## 1. What is a Set?

A Set is an unordered collection of unique elements.

---

## 2. Why are Sets faster than Lists?

Sets use Hash Tables, making search operations approximately O(1).

---

## 3. Difference between remove() and discard()?

- remove() raises an error if the element is missing.
- discard() does not.

---

## 4. Difference between Set and Frozen Set?

Set → Mutable

Frozen Set → Immutable

---

## 5. Can Sets contain duplicate values?

No.

---

## 6. Can Sets be indexed?

No.

---

## 7. Can Sets contain Lists?

No, because Lists are mutable.

---

# Summary

In this chapter, you learned:

- ✅ Creating Sets
- ✅ Set Properties
- ✅ Adding and Removing Elements
- ✅ Set Operations
- ✅ Membership Testing
- ✅ Subsets and Supersets
- ✅ Frozen Sets
- ✅ Set Comprehensions
- ✅ Practical Applications
- ✅ Interview Questions

---

# 🚀 Next Topic

**Day 10 — Python Strings**

You will learn:

- String Creation
- Indexing
- Slicing
- String Methods
- Formatting
- Escape Characters
- Regular Expressions Basics
- Real-world String Manipulation
```