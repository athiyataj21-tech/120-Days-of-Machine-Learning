# Day 1: Variables and Data Types in Python

## What is a Variable?

A variable is a named memory location used to store data values. Variables allow us to save information and reuse it throughout a program.

### Example

```python
name = "Athiya"
age = 24
```

Here:

* `name` stores a string value.
* `age` stores an integer value.

---

## Rules for Naming Variables

* Must start with a letter or underscore (_)
* Cannot start with a number
* Cannot contain spaces
* Case-sensitive (`Age` and `age` are different)

### Valid Examples

```python
student_name = "Athiya"
_age = 24
salary2025 = 50000
```

### Invalid Examples

```python
2name = "Athiya"
student name = "Athiya"
```

---

## Python Data Types

### String (str)

Used for text data.

```python
name = "Athiya"
```

### Integer (int)

Used for whole numbers.

```python
age = 24
```

### Float (float)

Used for decimal values.

```python
cgpa = 8.4
```

### Boolean (bool)

Represents True or False.

```python
is_placed = True
```

---

## Checking Data Types

```python
print(type(name))
print(type(age))
```

---

## Type Conversion

### Integer to Float

```python
age = 24
float_age = float(age)
```

### Float to Integer

```python
cgpa = 8.4
int_cgpa = int(cgpa)
```

### Number to String

```python
age = 24
age_str = str(age)
```

---

## Why Variables Matter in Machine Learning?

Variables are used to:

* Store datasets
* Save model parameters
* Track evaluation metrics
* Manage predictions and outputs

Every machine learning model relies heavily on variables and data types.
