# Day 08 — Python Dictionaries

## 📖 What is a Dictionary?

A dictionary is a built-in Python data structure that stores data as **key-value pairs**.

Unlike lists and tuples, dictionaries are:

- Mutable
- Unordered (before Python 3.7)
- Ordered (Python 3.7+)
- Keys must be unique
- Keys are immutable
- Values can be any data type

Example:

```python
student = {
    "name": "Athiya",
    "age": 22,
    "course": "Machine Learning"
}
```

---

# Creating Dictionaries

## Empty Dictionary

```python
d = {}
```

or

```python
d = dict()
```

## Dictionary with Values

```python
person = {
    "name": "John",
    "age": 25,
    "city": "Bangalore"
}
```

---

# Accessing Values

Using keys

```python
print(person["name"])
```

Using get()

```python
print(person.get("age"))
```

Difference:

```python
person["salary"]      # KeyError

person.get("salary")  # None
```

---

# Adding Items

```python
person["salary"] = 50000
```

---

# Updating Values

```python
person["age"] = 26
```

Using update()

```python
person.update({"city":"Mysore"})
```

---

# Removing Items

Using pop()

```python
person.pop("age")
```

Using popitem()

```python
person.popitem()
```

Using del

```python
del person["city"]
```

Clear dictionary

```python
person.clear()
```

---

# Dictionary Methods

## keys()

```python
student.keys()
```

## values()

```python
student.values()
```

## items()

```python
student.items()
```

---

# Looping Through Dictionary

```python
for key in student:
    print(key)
```

Keys and Values

```python
for key, value in student.items():
    print(key, value)
```

---

# Nested Dictionary

```python
students = {
    "101":{
        "name":"Alice",
        "age":21
    },
    "102":{
        "name":"Bob",
        "age":22
    }
}
```

Access

```python
print(students["101"]["name"])
```

---

# Dictionary Comprehension

```python
square = {x:x*x for x in range(5)}
```

Output

```python
{
0:0,
1:1,
2:4,
3:9,
4:16
}
```

---

# Membership Operator

```python
"name" in person
```

```python
"salary" not in person
```

---

# Copy Dictionary

```python
copy_dict = person.copy()
```

---

# Merge Dictionaries

Python 3.9+

```python
dict3 = dict1 | dict2
```

Older Version

```python
dict1.update(dict2)
```

---

# Length

```python
len(person)
```

---

# Advantages

- Fast lookup
- Unique keys
- Flexible
- Easy to manage structured data

---

# Disadvantages

- Slightly higher memory usage
- Keys must be immutable

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Access | O(1) |
| Insert | O(1) |
| Delete | O(1) |
| Search | O(1) |

---

# Real World Uses

- Student Records
- Employee Database
- JSON Data
- API Responses
- Machine Learning Configuration Files
- Web Development