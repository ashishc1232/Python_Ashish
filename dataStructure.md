
# 🔹 Part 2: Data Structures + Conditional Statements

Data structures are ways to store and organize data. Common ones:

* **List (Array)**
* **Tuple**
* **Set**
* **Dictionary (HashMap)**

Conditional statements are often used to **check, search, update, or decide** things inside these data structures.

---

## Example Programs

### 1. **Check if a number exists in a List**

```python
numbers = [10, 20, 30, 40, 50]
search = 30

if search in numbers:
    print(f"{search} is found in the list.")
else:
    print(f"{search} is not in the list.")
```

**Logic:**

* `in` operator checks membership.
* Condition decides whether element exists.

---

### 2. **Find Maximum Number in a List**

```python
numbers = [12, 45, 9, 33, 27]

max_num = numbers[0]  # assume first number is max

for num in numbers:
    if num > max_num:
        max_num = num

print("Maximum number is:", max_num)
```

**Logic:**

* Compare each number with current max.
* Update max if condition `num > max_num` is true.

---

### 3. **Student Grades using Dictionary + if-else**

```python
students = {
    "Aman": 85,
    "Riya": 72,
    "Sohan": 40,
    "Priya": 91
}

for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print(name, "scored", marks, "Grade:", grade)
```

**Logic:**

* Loop through dictionary.
* Apply conditions on each student’s marks.

---

### 4. **Check if a String is a Palindrome (using Conditional + List/Tuple)**

```python
word = "madam"

if word == word[::-1]:   # reverse string using slicing
    print("Palindrome")
else:
    print("Not Palindrome")
```

**Logic:**

* Compare word with its reverse.
* Condition decides palindrome or not.

---

### 5. **Stack Operation Example (with Condition)**

```python
stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

# Pop element only if stack is not empty
if stack:
    print("Popped:", stack.pop())
else:
    print("Stack is empty")
```

**Logic:**

* Condition `if stack` checks if stack is not empty before popping.

---

## 🔹 Assignments for Students

1. Write a program to check if a given number is **present in a tuple**.
2. Write a program to find the **minimum number in a list** (using conditions, not built-in `min()`).
3. Write a program to count how many students passed or failed from a dictionary of `{name: marks}`.
4. Write a program to check if a given word is present in a **set** (case-insensitive).
5. Implement a **queue** using list. Before removing (dequeue), check if queue is empty.
6. Write a program to print the **second largest element** in a list.
7. From a list of numbers, separate **even and odd numbers** into two different lists using conditions.
8. Write a program to check whether a string contains **only vowels** or not.
9. Implement a dictionary where key = student name, value = age. Print only those students whose age > 18.
10. Write a program to check if a list is sorted in **ascending order** or not.





