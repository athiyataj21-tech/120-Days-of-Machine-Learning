# 1. Simple Function
def greet():
    print("Welcome to Machine Learning")

greet()

# 2. Function with Parameters
def add(a, b):
    print("Sum:", a + b)

add(5, 10)

# 3. Function with Return
def multiply(a, b):
    return a * b

result = multiply(4, 6)
print(result)

# 4. Default Argument
def country(name="India"):
    print(name)

country()
country("Japan")

# 5. Keyword Argument
def student(name, age):
    print(name, age)

student(age=21, name="Athiya")

# 6. *args
def total(*numbers):
    print(sum(numbers))

total(10, 20, 30, 40)

# 7. **kwargs
def details(**info):
    for key, value in info.items():
        print(key, value)

details(name="Athiya", city="Mysuru", age=21)

# 8. Lambda
square = lambda x: x * x
print(square(7))

# 9. Recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# 10. Local & Global Variable
x = 100

def demo():
    x = 50
    print("Local:", x)

demo()
print("Global:", x)