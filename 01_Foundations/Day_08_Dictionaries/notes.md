# Day 08 Quick Notes

## Dictionary

- Stores key-value pairs
- Mutable
- Ordered (Python 3.7+)
- Keys must be unique

---

## Syntax

```python
student = {
    "name":"Athiya",
    "age":22
}
```

---

## Access

```python
student["name"]
student.get("age")
```

---

## Add

```python
student["city"]="Bangalore"
```

---

## Update

```python
student["age"]=23
```

---

## Remove

```python
pop()
popitem()
del
clear()
```

---

## Important Methods

```python
keys()
values()
items()
update()
copy()
get()
```

---

## Loop

```python
for k,v in student.items():
    print(k,v)
```

---

## Dictionary Comprehension

```python
{x:x*x for x in range(5)}
```

---

## Nested Dictionary

```python
students["101"]["name"]
```

---

## Complexity

Access → O(1)

Insert → O(1)

Delete → O(1)

Search → O(1)