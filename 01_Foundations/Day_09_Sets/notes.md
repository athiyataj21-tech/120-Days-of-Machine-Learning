# Day 09 — Python Sets (Quick Revision Notes)

## 🎯 Key Points

- A **Set** is an unordered collection of **unique** elements.
- Duplicate values are automatically removed.
- Sets are mutable (modifiable).
- Sets do not support indexing or slicing.
- Sets are optimized for fast searching using hash tables.

---

# Creating Sets

Using curly braces

```python
fruits = {"Apple", "Banana", "Orange"}
```

Using `set()`

```python
numbers = set([1, 2, 3, 4])
```

Creating an empty set

```python
empty_set = set()
```

❌ Wrong

```python
empty = {}
```

Creates a dictionary instead of a set.

---

# Properties of Sets

- ✅ Unordered
- ✅ Mutable
- ✅ Unique elements only
- ✅ Fast lookup
- ❌ No indexing
- ❌ No slicing
- ❌ Cannot contain mutable objects like lists or dictionaries

---

# Duplicate Removal

```python
numbers = {1, 2, 2, 3, 4, 4, 5}

print(numbers)
```

Output

```text
{1, 2, 3, 4, 5}
```

---

# Adding Elements

## add()

Adds a single element.

```python
fruits.add("Mango")
```

---

## update()

Adds multiple elements.

```python
fruits.update(["Kiwi", "Grapes"])
```

---

# Removing Elements

## remove()

```python
fruits.remove("Banana")
```

Raises an error if the element does not exist.

---

## discard()

```python
fruits.discard("Banana")
```

Does not raise an error if the element is missing.

---

## pop()

```python
fruits.pop()
```

Removes a random element.

---

## clear()

```python
fruits.clear()
```

Removes all elements.

---

# Copying a Set

```python
copy_set = fruits.copy()
```

---

# Length of a Set

```python
len(fruits)
```

---

# Membership Operators

Check whether an element exists.

```python
10 in numbers
```

Check whether an element does not exist.

```python
100 not in numbers
```

---

# Set Operations

## Union

Returns all unique elements.

```python
A | B
```

or

```python
A.union(B)
```

---

## Intersection

Returns common elements.

```python
A & B
```

or

```python
A.intersection(B)
```

---

## Difference

Returns elements present only in the first set.

```python
A - B
```

or

```python
A.difference(B)
```

---

## Symmetric Difference

Returns elements present in either set but not both.

```python
A ^ B
```

or

```python
A.symmetric_difference(B)
```

---

# Subset

```python
A.issubset(B)
```

Returns `True` if all elements of A are present in B.

---

# Superset

```python
A.issuperset(B)
```

Returns `True` if A contains all elements of B.

---

# Disjoint Sets

```python
A.isdisjoint(B)
```

Returns `True` if both sets have no common elements.

---

# Frozen Set

Immutable version of a set.

```python
F = frozenset([1, 2, 3])
```

Cannot be modified after creation.

---

# Set Comprehension

```python
square_set = {x * x for x in range(6)}
```

Output

```text
{0, 1, 4, 9, 16, 25}
```

---

# Built-in Functions

```python
len(set_name)
```

Returns number of elements.

```python
max(set_name)
```

Returns largest element.

```python
min(set_name)
```

Returns smallest element.

```python
sum(set_name)
```

Returns sum of elements.

```python
sorted(set_name)
```

Returns a sorted list.

---

# Common Set Methods

| Method | Purpose |
|---------|---------|
| add() | Add one element |
| update() | Add multiple elements |
| remove() | Remove an element |
| discard() | Remove safely |
| pop() | Remove a random element |
| clear() | Remove all elements |
| copy() | Copy a set |
| union() | Combine two sets |
| intersection() | Find common elements |
| difference() | Find unique elements |
| symmetric_difference() | Find exclusive elements |
| issubset() | Check subset |
| issuperset() | Check superset |
| isdisjoint() | Check if sets are disjoint |

---

# Set vs List

| Feature | List | Set |
|----------|------|-----|
| Ordered | ✅ | ❌ |
| Allows Duplicates | ✅ | ❌ |
| Indexing | ✅ | ❌ |
| Mutable | ✅ | ✅ |
| Fast Search | ❌ | ✅ |

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Add | O(1) |
| Remove | O(1) |
| Search | O(1) |
| Union | O(n) |
| Intersection | O(min(n, m)) |
| Difference | O(n) |

---

# Real-World Applications

- Removing duplicate records
- Finding common interests
- Comparing datasets
- Database operations
- Recommendation systems
- Data preprocessing
- Machine Learning feature engineering
- Fast membership testing

---

# Common Mistakes

❌ Using `{}` for an empty set

```python
A = {}
```

Creates a dictionary.

✔ Correct

```python
A = set()
```

---

❌ Using indexing

```python
A[0]
```

Sets do not support indexing.

---

❌ Adding a list to a set

```python
A = {[1, 2]}
```

Raises `TypeError` because lists are mutable.

---

# Interview Questions

### 1. What is a Set?

A Set is an unordered collection of unique elements.

---

### 2. Why are Sets faster than Lists?

Because Sets use **Hash Tables**, allowing average O(1) search, insertion, and deletion.

---

### 3. Difference between `remove()` and `discard()`?

| remove() | discard() |
|------------|------------|
| Raises an error if element is missing | Does not raise an error |

---

### 4. Difference between Set and Frozen Set?

| Set | Frozen Set |
|------|------------|
| Mutable | Immutable |
| Can add/remove elements | Cannot be modified |

---

### 5. Can Sets contain duplicate values?

❌ No

---

### 6. Can Sets contain Lists?

❌ No, because Lists are mutable and unhashable.

---

### 7. Can Sets be indexed?

❌ No

---

# Quick Revision

✔ Unique elements only

✔ Unordered collection

✔ Mutable

✔ Fast lookup using hash tables

✔ Supports mathematical set operations

✔ No indexing or slicing

✔ Duplicate values are removed automatically

✔ Useful for data preprocessing and removing duplicates

---

# 🚀 Next Topic

**Day 10 — Python Strings**

Topics:

- String Creation
- Indexing
- Slicing
- String Methods
- Formatting
- Escape Characters
- String Manipulation
- Regular Expressions Basics
- Interview Questions