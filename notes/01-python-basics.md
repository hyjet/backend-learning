# 01-python-basics.md

# Python Basics

## Variables

Variables store data.

```python
name = "Kevin"
age = 30
```

## Data Types

```python
name = "Kevin"      # string
age = 30             # integer
height = 170.5       # float
is_student = False   # boolean
```

## Lists

Lists store multiple values.

```python
numbers = [1, 2, 3, 4, 5]
```

## Dictionaries

Dictionaries store data using keys and values.

```python
user = {
    "name": "Kevin",
    "age": 30
}
```

## List of Dictionaries

Useful for storing multiple users.

```python
users = [
    {"name": "Kevin", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17}
]
```

## If Else

```python
age = 20

if age >= 21:
    print("Adult")
else:
    print("Minor")
```

## For Loop

Used to go through each item in a list.

```python
for user in users:
    print(user["name"])
```

## Functions

Functions let you reuse logic.

```python
def greet(name):
    return f"Hello {name}"
```

Example:

```python
message = greet("Kevin")
print(message)
```

## List Comprehension

Short way to create or filter lists.

```python
[user for user in users if user["age"] >= 21]
```

Equivalent normal version:

```python
result = []

for user in users:
    if user["age"] >= 21:
        result.append(user)
```

## f-String

Used to insert variables into text.

```python
name = "Kevin"
print(f"Hello {name}")
```

## Main Block

```python
if __name__ == "__main__":
    print("Run this file directly")
```

This makes sure code only runs when the file is executed directly.

---