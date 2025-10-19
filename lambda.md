
## 1. Lambda Functions – Basics

> A **lambda function** is a small, anonymous (unnamed) function defined in a single line.

### Syntax

```python
lambda arguments: expression
```

* No `def` keyword
* Can have any number of arguments
* Must contain **one expression** (no multiple statements)
* Returns the result of the expression automatically

---

### Example 1: Square of a Number

```python
square = lambda x: x * x
print(square(5))   # 25
```

Equivalent using normal function:

```python
def square(x):
    return x * x
```

---

### Example 2: Add Two Numbers

```python
add = lambda a, b: a + b
print(add(10, 20))  # 30
```

---

### Example 3: Conditional Expression Inside Lambda

```python
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(7))  # Odd
```

---

### Example 4: Sorting with Lambda

You can use lambda to define **custom sorting keys**.

```python
names = ["Ravi", "Ashish", "Meena", "Anil"]
# Sort by length of name
names.sort(key=lambda name: len(name))
print(names)  # ['Ravi', 'Anil', 'Meena', 'Ashish']
```

---

## 2. map() – Apply a Function to Each Item

> `map(function, iterable)` applies a function to every element in an iterable (like a list) and returns a map object (which can be converted to a list).

---

### Example 1: Double Each Number

```python
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))   # [2, 4, 6, 8, 10]
```

---

### Example 2: Convert List of Strings to Uppercase

```python
names = ["ravi", "meena", "ashish"]
upper_names = map(lambda name: name.upper(), names)
print(list(upper_names))   # ['RAVI', 'MEENA', 'ASHISH']
```

---

### Example 3: Extract First Letters of Words

```python
words = ["apple", "banana", "cherry"]
first_letters = map(lambda w: w[0], words)
print(list(first_letters))   # ['a', 'b', 'c']
```

---

### Example 4: Apply Function Instead of Lambda

You can use normal functions too:

```python
def square(n):
    return n * n

nums = [1, 2, 3, 4]
squares = map(square, nums)
print(list(squares))  # [1, 4, 9, 16]
```

---

## 3. filter() – Filter Elements Based on a Condition

> `filter(function, iterable)` keeps only those elements for which the function returns `True`.

---

### Example 1: Filter Even Numbers

```python
numbers = [10, 15, 20, 25, 30]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))   # [10, 20, 30]
```

---

### Example 2: Keep Strings Longer Than 4 Characters

```python
words = ["dog", "elephant", "cat", "giraffe"]
long_words = filter(lambda w: len(w) > 4, words)
print(list(long_words))   # ['elephant', 'giraffe']
```

---

### Example 3: Filter Non-Empty Strings

```python
items = ["", "hello", "", "world", "python", ""]
non_empty = filter(lambda x: x != "", items)
print(list(non_empty))  # ['hello', 'world', 'python']
```

---

### Example 4: Using Named Function in Filter

```python
def is_positive(n):
    return n > 0

nums = [-5, 0, 3, 7, -2]
positives = filter(is_positive, nums)
print(list(positives))  # [3, 7]
```

---

## 4. reduce() – Reduce a Sequence to a Single Value

> `reduce(function, iterable)` repeatedly applies the function to **combine elements** into a single result.
> `reduce` is in `functools` module.

### Import First

```python
from functools import reduce
```

---

### Example 1: Sum of Numbers

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(total)   # 15
```

Process:

```
1+2=3 → 3+3=6 → 6+4=10 → 10+5=15
```

---

### Example 2: Product of Numbers

```python
from functools import reduce

numbers = [2, 3, 4]
product = reduce(lambda a, b: a * b, numbers)
print(product)  # 24
```

---

### Example 3: Find Maximum Element

```python
from functools import reduce

numbers = [5, 2, 9, 1, 7]
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)   # 9
```

---

### Example 4: Concatenate Strings

```python
from functools import reduce

words = ["Python", "is", "fun"]
sentence = reduce(lambda a, b: a + " " + b, words)
print(sentence)  # "Python is fun"
```

---

## 5. Combining map(), filter(), and reduce()

You can chain them for powerful data transformations.

### Example:

Given a list of numbers:

* First, filter even numbers
* Then, double each even number
* Finally, find the sum

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

evens = filter(lambda x: x % 2 == 0, numbers)
doubled = map(lambda x: x * 2, evens)
result = reduce(lambda a, b: a + b, doubled)

print(result)   # 24  (2→4, 4→8, 6→12 → sum = 4+8+12)
```

---

## 6. When to Use Functional Programming (FP) Tools

| Tool       | Best Use                                                                |
| ---------- | ----------------------------------------------------------------------- |
| **lambda** | Quick throwaway functions, especially inside map/filter/sort            |
| **map**    | Transforming each element of a list                                     |
| **filter** | Selecting elements based on a condition                                 |
| **reduce** | Combining a list into a single value (sum, product, max, concatenation) |

### Advantages

* Short and clean code for transformations
* Easy to combine operations
* Avoids writing explicit loops for simple operations

### When Not to Use

* When the logic is complex and readability matters more
* When multiple statements are needed → use normal `def` functions instead

---

## 7. Practice Problems

Try to solve these using `lambda`, `map`, `filter`, and `reduce`:

1. Given a list of integers, return a list of their cubes using `map`.
2. Filter out names that start with a vowel.
3. Given a list of strings, find the longest string using `reduce`.
4. Given a list of numbers, find the sum of squares of odd numbers.
5. Sort a list of tuples by the second element using lambda in the `sorted()` function.



