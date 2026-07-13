"""
==========================================
Day 10 - Python Strings Practice
120 Days of Machine Learning
Part 1 (Programs 1–35)
==========================================
"""

print("=" * 50)
print("DAY 10 - PYTHON STRINGS PRACTICE")
print("=" * 50)

# ==========================================
# Program 1
# Create a String
# ==========================================

print("\nProgram 1")
text = "Machine Learning"
print(text)

# ==========================================
# Program 2
# Single Quotes
# ==========================================

print("\nProgram 2")
text = 'Python'
print(text)

# ==========================================
# Program 3
# Triple Quotes
# ==========================================

print("\nProgram 3")
text = """Welcome
to
Python"""
print(text)

# ==========================================
# Program 4
# String Length
# ==========================================

print("\nProgram 4")
text = "Machine Learning"
print(len(text))

# ==========================================
# Program 5
# Positive Indexing
# ==========================================

print("\nProgram 5")
text = "Python"
print(text[0])
print(text[2])
print(text[5])

# ==========================================
# Program 6
# Negative Indexing
# ==========================================

print("\nProgram 6")
text = "Python"
print(text[-1])
print(text[-2])
print(text[-6])

# ==========================================
# Program 7
# First Character
# ==========================================

print("\nProgram 7")
text = "Artificial"
print(text[0])

# ==========================================
# Program 8
# Last Character
# ==========================================

print("\nProgram 8")
text = "Artificial"
print(text[-1])

# ==========================================
# Program 9
# Basic Slicing
# ==========================================

print("\nProgram 9")
text = "MachineLearning"
print(text[0:7])

# ==========================================
# Program 10
# Slice From Beginning
# ==========================================

print("\nProgram 10")
text = "MachineLearning"
print(text[:7])

# ==========================================
# Program 11
# Slice Till End
# ==========================================

print("\nProgram 11")
text = "MachineLearning"
print(text[7:])

# ==========================================
# Program 12
# Reverse String
# ==========================================

print("\nProgram 12")
text = "Python"
print(text[::-1])

# ==========================================
# Program 13
# Every Second Character
# ==========================================

print("\nProgram 13")
text = "MachineLearning"
print(text[::2])

# ==========================================
# Program 14
# Reverse Using Step
# ==========================================

print("\nProgram 14")
text = "Artificial"
print(text[::-1])

# ==========================================
# Program 15
# Concatenation
# ==========================================

print("\nProgram 15")
a = "Machine"
b = "Learning"
print(a + " " + b)

# ==========================================
# Program 16
# Repetition
# ==========================================

print("\nProgram 16")
print("AI " * 5)

# ==========================================
# Program 17
# Membership Operator
# ==========================================

print("\nProgram 17")
text = "Machine Learning"
print("Machine" in text)
print("Python" in text)

# ==========================================
# Program 18
# Not In
# ==========================================

print("\nProgram 18")
text = "Python"
print("Java" not in text)

# ==========================================
# Program 19
# Compare Strings
# ==========================================

print("\nProgram 19")
print("apple" == "apple")
print("apple" == "Apple")

# ==========================================
# Program 20
# Lexicographical Comparison
# ==========================================

print("\nProgram 20")
print("apple" < "banana")

# ==========================================
# Program 21
# Uppercase
# ==========================================

print("\nProgram 21")
text = "python"
print(text.upper())

# ==========================================
# Program 22
# Lowercase
# ==========================================

print("\nProgram 22")
text = "PYTHON"
print(text.lower())

# ==========================================
# Program 23
# Title Case
# ==========================================

print("\nProgram 23")
text = "machine learning"
print(text.title())

# ==========================================
# Program 24
# Capitalize
# ==========================================

print("\nProgram 24")
text = "machine learning"
print(text.capitalize())

# ==========================================
# Program 25
# Swapcase
# ==========================================

print("\nProgram 25")
text = "PyThOn"
print(text.swapcase())

# ==========================================
# Program 26
# Strip Spaces
# ==========================================

print("\nProgram 26")
text = "   Python   "
print(text.strip())

# ==========================================
# Program 27
# Left Strip
# ==========================================

print("\nProgram 27")
text = "    Python"
print(text.lstrip())

# ==========================================
# Program 28
# Right Strip
# ==========================================

print("\nProgram 28")
text = "Python     "
print(text.rstrip())

# ==========================================
# Program 29
# Replace Word
# ==========================================

print("\nProgram 29")
text = "I love Java"
print(text.replace("Java", "Python"))

# ==========================================
# Program 30
# Split String
# ==========================================

print("\nProgram 30")
text = "Machine Learning Python"
print(text.split())

# ==========================================
# Program 31
# Join List
# ==========================================

print("\nProgram 31")
words = ["Machine", "Learning", "Python"]
print("-".join(words))

# ==========================================
# Program 32
# Find Method
# ==========================================

print("\nProgram 32")
text = "Machine"
print(text.find("h"))

# ==========================================
# Program 33
# Index Method
# ==========================================

print("\nProgram 33")
text = "Machine"
print(text.index("h"))

# ==========================================
# Program 34
# Count Characters
# ==========================================

print("\nProgram 34")
text = "banana"
print(text.count("a"))

# ==========================================
# Program 35
# Startswith & Endswith
# ==========================================

print("\nProgram 35")
text = "Machine Learning"
print(text.startswith("Machine"))
print(text.endswith("Learning"))

print("\n")
print("=" * 50)
print("End of Part 1 (Programs 1–35)")
print("=" * 50)