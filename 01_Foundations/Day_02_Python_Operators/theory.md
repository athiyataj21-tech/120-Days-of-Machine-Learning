# Day 2 - Python Operators

## 🎯 Learning Objectives

In this lesson, you'll learn:

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Identity Operators
- Membership Operators
- Bitwise Operators
- Operator Precedence

---

# 1. Arithmetic Operators

Used to perform mathematical calculations.

| Operator | Description | Example |
|----------|-------------|---------|
| + | Addition | 5 + 2 |
| - | Subtraction | 5 - 2 |
| * | Multiplication | 5 * 2 |
| / | Division | 5 / 2 |
| // | Floor Division | 5 // 2 |
| % | Modulus | 5 % 2 |
| ** | Exponent | 5 ** 2 |

---

# 2. Assignment Operators

Used to assign values.

= += -= *= /= //= %= **=

Example

x = 10
x += 5

---

# 3. Comparison Operators

Return True or False.

==
!=
>
<
>=
<=

---

# 4. Logical Operators

and

or

not

---

# 5. Identity Operators

is

is not

---

# 6. Membership Operators

in

not in

---

# 7. Bitwise Operators

&
|
^
~
<<
>>

---

# 8. Operator Precedence

Highest

()
**
*, /
//, %
+, -
Comparison
not
and
or

---

## Machine Learning Example

```python
accuracy = 92

if accuracy >= 90 and accuracy <= 100:
    print("Excellent Model")