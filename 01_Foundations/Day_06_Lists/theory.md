# Day 06 — Python Lists

## What is a List?

A list is an ordered, mutable (changeable) collection in Python that can store multiple items of different data types.

Example:

```python
numbers = [10, 20, 30, 40]
```

---

## Characteristics of Lists

- Ordered
- Mutable
- Allows duplicate values
- Can store different data types
- Indexed (starts from 0)

Example:

```python
items = [10, "Python", 5.5, True]
```

---

## Creating Lists

```python
fruits = ["Apple", "Banana", "Orange"]
numbers = [1,2,3,4]
empty = []
```

---

## Accessing Elements

```python
print(fruits[0])
print(fruits[-1])
```

---

## Slicing

```python
print(fruits[0:2])
print(fruits[1:])
print(fruits[::-1])
```

---

## Updating Elements

```python
fruits[1] = "Mango"
```

---

## Adding Elements

append()

```python
fruits.append("Grapes")
```

insert()

```python
fruits.insert(1,"Kiwi")
```

extend()

```python
fruits.extend(["Pineapple","Guava"])
```

---

## Removing Elements

remove()

```python
fruits.remove("Apple")
```

pop()

```python
fruits.pop()
```

clear()

```python
fruits.clear()
```

del

```python
del fruits[0]
```

---

## List Functions

```python
len(list)

max(list)

min(list)

sum(list)

sorted(list)
```

---

## Useful Methods

```python
append()

insert()

extend()

remove()

pop()

index()

count()

sort()

reverse()

copy()

clear()
```

---

## Nested Lists

```python
matrix = [
    [1,2],
    [3,4]
]

print(matrix[0][1])
```

---

## List Comprehension

```python
squares = [x*x for x in range(10)]

print(squares)
```

Example

```python
even = [x for x in range(20) if x%2==0]
```

---

## Membership Operator

```python
if "Apple" in fruits:
    print("Found")
```

---

## Iterating

```python
for item in fruits:
    print(item)
```

Using enumerate

```python
for index,value in enumerate(fruits):
    print(index,value)
```

---

## Applications in Machine Learning

- Store datasets
- Feature values
- Labels
- Predictions
- Data preprocessing