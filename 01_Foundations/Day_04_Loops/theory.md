# Day 4 - Loops in Python

## Introduction

In programming, there are many situations where we need to execute the same block of code multiple times. Writing the same code repeatedly makes the program lengthy, difficult to read, and harder to maintain.

To solve this problem, Python provides **loops**. A loop allows a block of code to execute repeatedly until a specified condition becomes false or until all items in a sequence have been processed.

Loops make programs shorter, cleaner, and more efficient. They are one of the most important concepts in Python and are widely used in automation, data processing, and Machine Learning.

---

## Why Loops?

Imagine you want to print the numbers from 1 to 100.

Without using loops, you would have to write:

```python
print(1)
print(2)
print(3)
...
print(100)
```

This approach is repetitive, time-consuming, and difficult to maintain.

Using a loop, the same task becomes:

```python
for i in range(1, 101):
    print(i)
```

The loop automatically repeats the print statement for every value in the specified range.

### Advantages of Loops

- Reduces repetitive code.
- Improves readability.
- Saves development time.
- Makes programs easier to maintain.
- Handles repetitive tasks efficiently.

---

# for Loop

The **for loop** is used to iterate over a sequence such as a string, list, tuple, dictionary, set, or range.

It is generally used when the number of iterations is known.

## Syntax

```python
for variable in iterable:
    # code block
```

- **variable** stores the current value.
- **iterable** is the object being traversed.
- The indented block executes once for each item.

### Example 1

```python
for i in range(5):
    print(i)
```

**Output**

```
0
1
2
3
4
```

### Example 2

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

**Output**

```
Apple
Banana
Mango
```

### Example 3

```python
name = "Python"

for letter in name:
    print(letter)
```

The loop prints one character at a time.

---

# while Loop

A **while loop** executes as long as the specified condition remains True.

It is mainly used when the number of iterations is unknown.

## Syntax

```python
while condition:
    # code block
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

**Output**

```
1
2
3
4
5
```

The loop stops automatically when the condition becomes False.

### Infinite Loop

If the condition never becomes False, the loop runs forever.

```python
while True:
    print("Hello")
```

Be careful while using `while` loops.

---

# range() Function

The **range()** function generates a sequence of numbers.

It is mostly used with `for` loops.

## Syntax

```python
range(stop)

range(start, stop)

range(start, stop, step)
```

### Example 1

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

### Example 2

```python
for i in range(1, 6):
    print(i)
```

Output:

```
1
2
3
4
5
```

### Example 3

```python
for i in range(2, 11, 2):
    print(i)
```

Output:

```
2
4
6
8
10
```

---

# Nested Loops

A loop inside another loop is called a **Nested Loop**.

Nested loops are useful for working with tables, matrices, grids, and patterns.

### Example

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

Output

```
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```

---

# break Statement

The **break** statement immediately terminates the loop.

Once `break` is executed, the remaining iterations are skipped.

### Example

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

Output

```
0
1
2
3
4
```

---

# continue Statement

The **continue** statement skips the current iteration and moves to the next iteration.

### Example

```python
for i in range(10):

    if i % 2 == 0:
        continue

    print(i)
```

Output

```
1
3
5
7
9
```

---

# pass Statement

The **pass** statement is a placeholder.

It does nothing and is often used when a block of code is required syntactically but no action needs to be performed.

### Example

```python
for i in range(5):
    pass

print("Loop Completed")
```

Output

```
Loop Completed
```

---

# Pattern Printing

Loops are commonly used to print star, number, and alphabet patterns.

### Right Triangle

```python
for i in range(5):

    for j in range(i + 1):
        print("*", end=" ")

    print()
```

Output

```
*
* *
* * *
* * * *
* * * * *
```

### Inverted Triangle

```python
for i in range(5, 0, -1):
    print("* " * i)
```

Output

```
* * * * *
* * * *
* * *
* *
*
```

Pattern printing helps improve logical thinking and understanding of nested loops.

---

# Common Mistakes

- Forgetting to indent the loop body.
- Creating an infinite `while` loop.
- Modifying the loop variable incorrectly.
- Using `break` when `continue` is needed.
- Using a `while` loop when a `for` loop is more suitable.

---

# Best Practices

- Use `for` loops when the number of iterations is known.
- Use `while` loops only when necessary.
- Keep loop bodies simple and readable.
- Avoid deeply nested loops whenever possible.
- Write meaningful variable names like `student`, `number`, or `item`.
- Always ensure that a `while` loop has a terminating condition.

---

# Machine Learning Applications

Loops are extensively used in Machine Learning and Data Science.

Some common applications include:

- Iterating through datasets.
- Reading rows from CSV files.
- Data preprocessing.
- Feature engineering.
- Model training over multiple epochs.
- Batch processing.
- Calculating evaluation metrics.
- Making predictions on multiple records.

Although libraries like NumPy and Pandas reduce the need for explicit loops, understanding loops is essential for building machine learning algorithms from scratch.

---

# Summary

In this chapter, you learned:

- What loops are.
- Why loops are important.
- How to use `for` loops.
- How to use `while` loops.
- Working with the `range()` function.
- Nested loops.
- Loop control statements (`break`, `continue`, and `pass`).
- Pattern printing using loops.
- Common mistakes and best practices.
- Real-world applications of loops in Machine Learning.

Loops are one of the most fundamental programming concepts. Mastering them will help you write efficient programs and build a strong foundation for Data Science and Machine Learning.