# Day 3: Conditional Statements in Python

## Introduction

Conditional statements allow a program to make decisions based on whether a condition is True or False. They control the flow of execution in a Python program.

Python uses the following conditional statements:

- if
- if...else
- if...elif...else
- Nested if

---

# 1. if Statement

The if statement executes a block of code only when the given condition is True.

### Syntax

```python
if condition:
    statement
```

### Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

---

# 2. if...else Statement

Used when there are two possible outcomes.

### Syntax

```python
if condition:
    statement1
else:
    statement2
```

### Example

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

# 3. if...elif...else Statement

Used to check multiple conditions.

### Syntax

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

### Example

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
```

---

# 4. Nested if

An if statement inside another if statement.

Example

```python
age = 21
citizen = True

if age >= 18:
    if citizen:
        print("Eligible")
```

---

# 5. Comparison Operators

| Operator | Meaning |
|----------|---------|
| == | Equal |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

---

# 6. Logical Operators

## and

Returns True only if both conditions are True.

```python
if age >= 18 and salary >= 30000:
    print("Approved")
```

## or

Returns True if at least one condition is True.

```python
if marks > 90 or sports:
    print("Scholarship")
```

## not

Reverses the result.

```python
if not logged_in:
    print("Login First")
```

---

# 7. Membership Operators

Used to check membership.

```python
name = "Athiya"

if "A" in name:
    print("Found")
```

---

# 8. Identity Operators

```python
is
is not
```

Example

```python
a = [1,2]
b = a

print(a is b)
```

---

# 9. Ternary Operator

Short form of if...else.

```python
age = 20

message = "Adult" if age >= 18 else "Minor"
```

---

# Advantages

- Easy decision making
- Improves readability
- Controls program execution
- Used in every ML project

---

# Applications in Machine Learning

- Data filtering
- Data cleaning
- Feature engineering
- Missing value handling
- Model evaluation
- Rule-based systems