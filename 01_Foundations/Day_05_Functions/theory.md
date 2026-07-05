# Day 5 – Python Functions

## What is a Function?

A function is a reusable block of code that performs a specific task. Functions help reduce code duplication, improve readability, and make programs modular.

---

## Why Use Functions?

- Avoid writing repetitive code
- Improve code readability
- Make debugging easier
- Promote code reusability
- Break complex problems into smaller parts

---

## Syntax

```python
def function_name(parameters):
    # Function body
    return value
```

Example:

```python
def greet():
    print("Hello, World!")

greet()
```

Output:

```
Hello, World!
```

---

## Types of Functions

### 1. Built-in Functions

Python provides many built-in functions.

Examples:

```python
print()
len()
type()
sum()
max()
min()
```

Example:

```python
numbers = [10, 20, 30]
print(sum(numbers))
```

Output:

```
60
```

---

### 2. User-defined Functions

Functions created by the programmer.

Example:

```python
def add(a, b):
    return a + b

print(add(5, 8))
```

Output:

```
13
```

---

## Function Parameters

### Positional Arguments

```python
def student(name, age):
    print(name, age)

student("Athiya", 21)
```

---

### Keyword Arguments

```python
student(age=21, name="Athiya")
```

---

### Default Arguments

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Athiya")
```

Output:

```
Hello Guest
Hello Athiya
```

---

### Variable-Length Arguments

#### *args

Allows multiple positional arguments.

```python
def total(*numbers):
    return sum(numbers)

print(total(10,20,30))
```

Output:

```
60
```

---

#### **kwargs

Allows multiple keyword arguments.

```python
def details(**info):
    for key, value in info.items():
        print(key, value)

details(name="Athiya", age=21)
```

---

## Return Statement

The return statement sends a value back to the caller.

```python
def square(x):
    return x*x

result = square(5)
print(result)
```

Output:

```
25
```

---

## Scope of Variables

### Local Variable

```python
def demo():
    x = 10
    print(x)

demo()
```

---

### Global Variable

```python
x = 100

def show():
    print(x)

show()
```

---

## Lambda Functions

Anonymous functions written in one line.

Syntax:

```python
lambda arguments : expression
```

Example:

```python
square = lambda x: x*x

print(square(6))
```

Output:

```
36
```

---

## Recursive Functions

A function calling itself.

Example:

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
```

Output:

```
120
```

---

## Advantages of Functions

- Code Reusability
- Easier Maintenance
- Modular Programming
- Better Testing
- Improved Readability

---

## Summary

✔ Built-in Functions

✔ User-defined Functions

✔ Parameters

✔ Arguments

✔ Return Statement

✔ Local & Global Variables

✔ Lambda Functions

✔ Recursion