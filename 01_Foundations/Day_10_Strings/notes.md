````markdown
# 📘 Day 10 – Python Strings (Quick Notes)

> **120 Days of Machine Learning**

---

# 📖 What is a String?

A **string** is a sequence of characters enclosed in quotes.

Python treats strings as **immutable** objects, meaning once a string is created, it cannot be changed.

```python
name = "Athiya"
```

---

# Types of Quotes

## Single Quotes

```python
s = 'Python'
```

## Double Quotes

```python
s = "Python"
```

## Triple Quotes

Used for multi-line strings.

```python
text = """Machine
Learning
Python"""
```

---

# String Properties

- Ordered
- Immutable
- Iterable
- Supports Indexing
- Supports Slicing
- Can contain duplicate characters

---

# Creating Strings

```python
name = "Athiya"

course = 'Machine Learning'

paragraph = """Python
is
awesome"""
```

---

# Indexing

Positive indexing starts from **0**.

```
P  y  t  h  o  n
0  1  2  3  4  5
```

```python
text = "Python"

print(text[0])
print(text[3])
```

Output

```
P
h
```

---

# Negative Indexing

```
P  y  t  h  o  n
-6 -5 -4 -3 -2 -1
```

```python
text = "Python"

print(text[-1])

print(text[-2])
```

Output

```
n
o
```

---

# String Slicing

Syntax

```python
string[start:stop]
```

Example

```python
text = "Machine"

print(text[0:4])
```

Output

```
Mach
```

---

## Skip Characters

```python
text = "Python"

print(text[::2])
```

Output

```
Pto
```

---

## Reverse String

```python
text = "Python"

print(text[::-1])
```

Output

```
nohtyP
```

---

# String Length

```python
text = "Machine Learning"

print(len(text))
```

---

# String Concatenation

```python
first = "Machine"

second = "Learning"

print(first + " " + second)
```

Output

```
Machine Learning
```

---

# String Repetition

```python
print("ML " * 3)
```

Output

```
ML ML ML
```

---

# Membership Operator

```python
text = "Machine Learning"

print("Machine" in text)

print("AI" in text)
```

Output

```
True

False
```

---

# Comparison Operators

```python
print("apple" == "apple")

print("apple" > "banana")
```

---

# Common String Methods

## upper()

```python
text = "python"

print(text.upper())
```

Output

```
PYTHON
```

---

## lower()

```python
text = "PYTHON"

print(text.lower())
```

Output

```
python
```

---

## capitalize()

```python
text = "machine learning"

print(text.capitalize())
```

Output

```
Machine learning
```

---

## title()

```python
text = "machine learning"

print(text.title())
```

Output

```
Machine Learning
```

---

## swapcase()

```python
text = "PyThOn"

print(text.swapcase())
```

Output

```
pYtHoN
```

---

## strip()

Removes spaces from both sides.

```python
text = " Python "

print(text.strip())
```

---

## lstrip()

```python
text = " Python"

print(text.lstrip())
```

---

## rstrip()

```python
text = "Python "

print(text.rstrip())
```

---

## replace()

```python
text = "I like Java"

print(text.replace("Java","Python"))
```

Output

```
I like Python
```

---

## split()

```python
text = "Machine Learning Python"

print(text.split())
```

Output

```
['Machine','Learning','Python']
```

---

## join()

```python
words = ["Machine","Learning"]

print("-".join(words))
```

Output

```
Machine-Learning
```

---

## find()

Returns index if found else -1.

```python
text = "Machine"

print(text.find("h"))
```

---

## index()

```python
text = "Machine"

print(text.index("h"))
```

Difference

- find() → returns -1
- index() → raises error

---

## count()

```python
text = "banana"

print(text.count("a"))
```

Output

```
3
```

---

## startswith()

```python
text = "Python"

print(text.startswith("Py"))
```

---

## endswith()

```python
print("Python".endswith("on"))
```

---

# String Checking Methods

## isalpha()

```python
"Python".isalpha()
```

---

## isdigit()

```python
"12345".isdigit()
```

---

## isalnum()

```python
"Python123".isalnum()
```

---

## isspace()

```python
"   ".isspace()
```

---

## islower()

```python
"python".islower()
```

---

## isupper()

```python
"PYTHON".isupper()
```

---

## istitle()

```python
"Machine Learning".istitle()
```

---

# String Formatting

## f-Strings

```python
name = "Athiya"

print(f"Hello {name}")
```

---

## format()

```python
print("Hello {}".format("Athiya"))
```

---

## Percent Formatting

```python
print("Hello %s" % "Athiya")
```

---

# Escape Characters

| Escape | Meaning |
|---------|----------|
| \n | New Line |
| \t | Tab |
| \\ | Backslash |
| \' | Single Quote |
| \" | Double Quote |

Example

```python
print("Hello\nWorld")
```

---

# Raw Strings

```python
path = r"C:\Users\Athiya"

print(path)
```

---

# Useful Built-in Functions

```python
len()

max()

min()

sorted()

reversed()

enumerate()
```

---

# String Iteration

```python
for ch in "Python":
    print(ch)
```

---

# Palindrome

```python
text = "madam"

print(text == text[::-1])
```

---

# Anagram

```python
sorted("listen") == sorted("silent")
```

---

# String Time Complexity

| Operation | Complexity |
|------------|------------|
| Indexing | O(1) |
| Slicing | O(n) |
| Concatenation | O(n) |
| Membership | O(n) |
| Reverse | O(n) |
| Replace | O(n) |
| Split | O(n) |
| Join | O(n) |
| Find | O(n) |

---

# Common Mistakes

❌

```python
text = "Python"

text[0] = "J"
```

Error

```
TypeError
```

Reason

Strings are immutable.

---

# Real-World Applications

- Password Validation
- Email Validation
- Text Cleaning
- NLP Preprocessing
- Chatbots
- Search Engines
- Sentiment Analysis
- Data Cleaning
- Log File Processing
- Username Formatting

---

# Interview Questions

1. What is a string?
2. Why are strings immutable?
3. Difference between find() and index()?
4. Difference between split() and join()?
5. Explain slicing.
6. Reverse a string.
7. Check palindrome.
8. Count vowels.
9. Remove spaces.
10. Difference between capitalize() and title().

---

# Cheat Sheet

```text
len()

upper()

lower()

title()

capitalize()

swapcase()

strip()

replace()

split()

join()

find()

index()

count()

startswith()

endswith()

isalpha()

isdigit()

isalnum()

isspace()

format()

f-strings

[::-1]
```

---

# Key Takeaways

- Strings are immutable.
- Indexing starts from 0.
- Negative indexing starts from -1.
- Slicing extracts parts of a string.
- Python provides many built-in string methods.
- f-Strings are the recommended way for formatting.
- Strings are widely used in Machine Learning, NLP, and Data Science.

---

# 🎯 Day 10 Completed ✅

Next Topic:

**📂 Day 11 – File Handling**
````
