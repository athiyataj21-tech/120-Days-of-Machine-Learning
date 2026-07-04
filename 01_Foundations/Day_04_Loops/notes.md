# Day 4 Quick Revision Notes

## Loops

Loops are used to execute a block of code repeatedly until a condition becomes False or all items in a sequence are processed.

Python provides two types of loops:

- for loop
- while loop

---

## for Loop

Used when the number of iterations is known.

### Syntax

```python
for variable in iterable:
    # code
```

### Example

```python
for i in range(5):
    print(i)
```

---

## while Loop

Used when the number of iterations is unknown.

### Syntax

```python
while condition:
    # code
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## range() Function

Used to generate a sequence of numbers.

### Syntax

```python
range(stop)

range(start, stop)

range(start, stop, step)
```

### Example

```python
for i in range(1, 11):
    print(i)
```

---

## break Statement

Terminates the loop immediately.

### Example

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

---

## continue Statement

Skips the current iteration and moves to the next iteration.

### Example

```python
for i in range(10):

    if i % 2 == 0:
        continue

    print(i)
```

---

## pass Statement

Acts as a placeholder. It does nothing.

### Example

```python
for i in range(5):
    pass

print("Loop Completed")
```

---

## Nested Loop

A loop inside another loop is called a nested loop.

### Example

```python
for i in range(3):

    for j in range(3):
        print(i, j)
```

---

## Pattern Printing

Loops are commonly used for printing star and number patterns.

Example:

```python
for i in range(5):

    for j in range(i + 1):
        print("*", end=" ")

    print()
```

---

## Remember

- Indentation is mandatory in Python.
- A `for` loop is best when the number of iterations is known.
- A `while` loop is best when the condition decides the number of iterations.
- `break` exits the loop immediately.
- `continue` skips only the current iteration.
- `pass` is a placeholder statement.
- Avoid creating infinite loops.

---

## Interview Tips

Know the difference between:

- for loop vs while loop
- break vs continue
- continue vs pass
- range() vs list()
- Nested loop vs Single loop

---

## Machine Learning Usage

✔ Iterating through datasets

✔ Data preprocessing

✔ Feature engineering

✔ Batch processing

✔ Model training (Epochs)

✔ Reading files row by row

✔ Data validation

---

## Quick Practice

- Print numbers from 1 to 100.
- Print even numbers from 1 to 50.
- Print odd numbers from 1 to 50.
- Find the sum of first N natural numbers.
- Find the factorial of a number.
- Print the multiplication table of a number.
- Print a star triangle pattern.
- Reverse a string using a loop.
- Count vowels in a string.
- Print Fibonacci series using a loop.