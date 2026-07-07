# Day 7 - Tuples in Python

# 📌 What is a Tuple?

A tuple is an ordered, immutable collection of elements.

Unlike lists, tuples cannot be modified after creation.

```python
fruits = ("Apple", "Banana", "Mango")
print(fruits)
```

Output

```
('Apple', 'Banana', 'Mango')
```

---

# Why Use Tuples?

- Faster than lists
- Immutable (safe from accidental changes)
- Can be used as dictionary keys
- Store fixed collections of data

---

# Creating Tuples

## Empty Tuple

```python
empty = ()
```

## Tuple with Values

```python
numbers = (1,2,3,4)
```

## Mixed Data Types

```python
data = ("Athiya",22,8.5,True)
```

## Single Element Tuple

```python
single = (5,)
```

Without comma:

```python
single = (5)
```

This becomes an integer.

---

# Accessing Elements

```python
colors = ("Red","Green","Blue")

print(colors[0])
print(colors[2])
```

Negative Indexing

```python
print(colors[-1])
print(colors[-2])
```

---

# Slicing

```python
numbers = (10,20,30,40,50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
```

---

# Tuple Length

```python
fruits = ("Apple","Banana","Mango")

print(len(fruits))
```

---

# Membership Operator

```python
print("Apple" in fruits)
print("Orange" not in fruits)
```

---

# Loop Through Tuple

```python
for fruit in fruits:
    print(fruit)
```

Using Index

```python
for i in range(len(fruits)):
    print(fruits[i])
```

---

# Tuple Concatenation

```python
a = (1,2)
b = (3,4)

print(a+b)
```

---

# Tuple Repetition

```python
print((1,2)*3)
```

Output

```
(1,2,1,2,1,2)
```

---

# Tuple Packing

```python
person = "Athiya",22,"Engineer"

print(person)
```

---

# Tuple Unpacking

```python
name,age,profession = person

print(name)
print(age)
print(profession)
```

---

# Nested Tuples

```python
student = (
    ("Athiya",22),
    ("Rahul",23)
)

print(student[0])
print(student[1][0])
```

---

# Tuple Methods

Tuples only have two methods.

## count()

```python
numbers = (1,2,2,3,2)

print(numbers.count(2))
```

---

## index()

```python
numbers = (10,20,30)

print(numbers.index(20))
```

---

# Built-in Functions

```python
numbers = (4,7,1,9)

print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sorted(numbers))
```

---

# Converting Between List and Tuple

Tuple to List

```python
numbers = (1,2,3)

lst = list(numbers)

print(lst)
```

List to Tuple

```python
lst = [1,2,3]

numbers = tuple(lst)

print(numbers)
```

---

# Tuple vs List

| List | Tuple |
|------|--------|
| Mutable | Immutable |
| [] | () |
| More Methods | Only count() and index() |
| Slower | Faster |
| Larger Memory | Less Memory |

---

# Advantages

- Faster execution
- Memory efficient
- Safe data storage
- Hashable
- Good for fixed datasets

---

# Limitations

- Cannot modify elements
- Cannot append/remove
- Less flexible

---

# Real-world Examples

Coordinates

```python
location = (12.97,77.59)
```

RGB Color

```python
color = (255,0,0)
```

Student Record

```python
student = ("Athiya",22,"ECE")
```

Days of Week

```python
days = (
"Mon",
"Tue",
"Wed",
"Thu",
"Fri",
"Sat",
"Sun"
)
```

---

# Summary

- Ordered
- Immutable
- Indexed
- Allows duplicates
- Faster than lists
- Supports packing and unpacking