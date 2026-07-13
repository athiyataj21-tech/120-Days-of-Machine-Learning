# 📘 Day 10 – Python Strings (Theory)

> **120 Days of Machine Learning**

---

# 📖 Table of Contents

1. Introduction to Strings
2. What is a String?
3. Characteristics of Strings
4. Creating Strings
5. Types of Quotes
6. Multiline Strings
7. String Immutability
8. String Indexing
9. Negative Indexing
10. String Slicing
11. Step Slicing
12. Reversing Strings
13. String Memory Representation
14. Built-in Functions
15. Summary

---

# 📖 Introduction

Strings are one of the most commonly used data types in Python.

Almost every real-world application uses strings.

Examples include:

- User names
- Passwords
- Email addresses
- Phone numbers
- Messages
- Chat applications
- Websites
- Machine Learning datasets
- Natural Language Processing (NLP)
- Search engines

Without strings, handling textual data would be impossible.

---

# What is a String?

A **string** is a sequence of characters enclosed within quotes.

A string may contain:

- Alphabets
- Numbers
- Symbols
- Spaces
- Emojis
- Unicode characters

Python treats strings as **objects**.

Example:

```python
name = "Athiya"

course = "Machine Learning"

city = "Bangalore"
```

Output

```
Athiya
Machine Learning
Bangalore
```

---

# Real-World Examples

```
Name

Athiya Taj

Email

athiya@gmail.com

Password

Athiya@123

Address

Bangalore, India

Sentence

Python is easy.

Website

www.python.org
```

All of these are stored as strings.

---

# Characteristics of Strings

Python strings have the following properties:

✅ Ordered

Characters maintain their order.

```
Python

P y t h o n
```

---

✅ Immutable

Strings cannot be modified after creation.

```python
text = "Python"

text[0] = "J"
```

Output

```
TypeError
```

Instead, create a new string.

```python
text = "Python"

text = "Jython"

print(text)
```

Output

```
Jython
```

---

✅ Iterable

Every character can be accessed using loops.

```python
text = "Python"

for letter in text:
    print(letter)
```

Output

```
P
y
t
h
o
n
```

---

✅ Supports Indexing

Each character has a position.

```
Python

P y t h o n

0 1 2 3 4 5
```

---

✅ Supports Slicing

You can extract part of a string.

```python
text = "Machine"

print(text[0:4])
```

Output

```
Mach
```

---

✅ Allows Duplicate Characters

```python
text = "banana"

print(text)
```

Output

```
banana
```

Duplicates remain unchanged.

---

# Creating Strings

Python provides multiple ways to create strings.

---

## Method 1 – Single Quotes

```python
language = 'Python'
```

---

## Method 2 – Double Quotes

```python
language = "Python"
```

---

## Method 3 – Triple Quotes

```python
paragraph = """Python is
simple
powerful
easy."""
```

---

## Method 4 – str() Constructor

```python
number = 100

text = str(number)

print(text)
```

Output

```
100
```

---

# Types of Quotes

| Quote Type | Example |
|------------|---------|
| Single | `'Python'` |
| Double | `"Python"` |
| Triple Single | `'''Python'''` |
| Triple Double | `"""Python"""` |

---

# When to Use Each?

Single Quotes

```python
'Python'
```

Double Quotes

```python
"Machine Learning"
```

Triple Quotes

```python
"""
Hello

World
"""
```

Useful for:

- Documentation
- Paragraphs
- SQL Queries
- HTML Content

---

# Multiline Strings

Example

```python
message = """
Welcome

to

Machine Learning
"""

print(message)
```

Output

```
Welcome

to

Machine Learning
```

---

# String Immutability

One of the most important interview topics.

Strings are immutable.

Meaning:

Once created,

they cannot be changed.

Incorrect

```python
name = "Athiya"

name[0] = "R"
```

Output

```
TypeError
```

Correct

```python
name = "Athiya"

new_name = "R" + name[1:]

print(new_name)
```

Output

```
Rthiya
```

---

# Why Are Strings Immutable?

Python makes strings immutable because:

- Faster execution
- Better memory optimization
- Safe sharing between variables
- Easier hashing
- Better dictionary performance

---

# String Indexing

Every character has an index.

Example

```
Machine

M a c h i n e

0 1 2 3 4 5 6
```

Example

```python
text = "Machine"

print(text[0])

print(text[3])

print(text[6])
```

Output

```
M

h

e
```

---

# Negative Indexing

Python also supports negative indexing.

```
Machine

M a c h i n e

-7 -6 -5 -4 -3 -2 -1
```

Example

```python
text = "Machine"

print(text[-1])

print(text[-2])

print(text[-7])
```

Output

```
e

n

M
```

Negative indexing is useful when working from the end of a string.

---

# IndexError

Accessing an invalid index causes an error.

Example

```python
text = "Python"

print(text[20])
```

Output

```
IndexError
```

Always ensure the index is within the valid range.

---

# String Slicing

Slicing extracts a portion of a string.

Syntax

```python
string[start:stop]
```

Where:

- **start** → Starting index (included)
- **stop** → Ending index (excluded)

Example

```python
text = "MachineLearning"

print(text[0:7])
```

Output

```
Machine
```

---

# Omitting Start Index

```python
text = "Machine"

print(text[:4])
```

Output

```
Mach
```

---

# Omitting Stop Index

```python
text = "Machine"

print(text[4:])
```

Output

```
ine
```

---

# Full Copy of a String

```python
text = "Python"

copy = text[:]

print(copy)
```

Output

```
Python
```

---

# Step Slicing

Syntax

```python
string[start:stop:step]
```

Example

```python
text = "MachineLearning"

print(text[::2])
```

Output

```
McieLann
```

---

# Reverse a String

One of the most common interview questions.

```python
text = "Python"

print(text[::-1])
```

Output

```
nohtyP
```

---

# String Memory Representation

```
String

Python

Memory

+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
  0   1   2   3   4   5
```

---

# Built-in Functions for Strings

Some useful built-in functions:

```python
len()

max()

min()

sorted()

reversed()

enumerate()
```

Example

```python
text = "Python"

print(len(text))

print(max(text))

print(min(text))
```

Output

```
6
y
P
```

---

# Key Points

- Strings are ordered sequences of characters.
- Strings are immutable.
- Strings support indexing and slicing.
- Positive indexing starts at **0**.
- Negative indexing starts at **-1**.
- Slicing excludes the stop index.
- `[::-1]` is the easiest way to reverse a string.
- Strings are extensively used in Data Science, NLP, Web Development, and Machine Learning.

---

# End of Part 1

In **Part 2**, we'll cover:
- String Operations
- Membership & Comparison Operators
- String Methods (all important methods with examples)
- Built-in String Functions
- Time Complexity