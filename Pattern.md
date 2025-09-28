
##  1. Introduction to Loops (30 min)

* What are loops?
* Why we need them? (repetition of tasks, automation, iterations)
* Two main loops in Python: **for** and **while**

### Example 1: Print numbers from 1 to 5 (for loop)

```python
for i in range(1, 6):
    print(i)
```

### Example 2: Print numbers from 1 to 5 (while loop)

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

 **Activity:**Write a program that prints numbers 1 to 10 using both `for` and `while`.

---

##  2. `for` Loop in Depth (45 min)

* Iterating over `range()`
* Iterating over **lists, tuples, strings**
* Iterating with step size
* Iterating in reverse

### Examples:

```python
# Print even numbers between 1 and 20
for i in range(2, 21, 2):
    print(i)

# Print characters of a string
for ch in "Python":
    print(ch)

# Print list items with index
fruits = ["apple", "banana", "mango"]
for i in range(len(fruits)):
    print(i, fruits[i])

# Reverse loop
for i in range(10, 0, -1):
    print(i)
```

 **Activity:** Write a program to print the **multiplication table** of any number entered by the user.

---

##  3. `while` Loop in Depth (45 min)

* Condition-based iteration
* Infinite loop (danger & control)
* Using `break` and `continue` inside while

### Examples:

```python
# Print numbers until user enters 0
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    print("You entered:", num)
    num = int(input("Enter a number (0 to stop): "))

# Break example
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1

# Continue example
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)   # prints only even numbers
```

 **Activity:**Write a **number guessing game** using `while`.

---

##  4. Nested Loops (1 hour)

* Loop inside another loop
* Printing patterns (stars, numbers, alphabets)
* Iterating through 2D lists

### Examples:

#### Example 1: Square Pattern

```python
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
```

 Output:

```
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

---

#### Example 2: Right-Angled Triangle

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
```

 Output:

```
*
* *
* * *
* * * *
* * * * *
```

---

#### Example 3: Number Pyramid

```python
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
```
 Output:

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

#### Example 4: Reverse Triangle

```python
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```
 Output:

```
* * * * *
* * * *
* * *
* *
*
```

---

#### Example 5: Iterating 2D List

```python
matrix = [[1,2,3], [4,5,6], [7,8,9]]

for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
```
 Output:

```
1 2 3
4 5 6
7 8 9
```

 **Activity:**Design a **diamond shape pattern** using nested loops.

---

##  5. Iteration Patterns (30 min)

* **Sum of numbers**
* **Factorial calculation**
* **Fibonacci series**
* **Prime number check**
* **Armstrong number check**

### Examples:

#### Example 1: Sum of first 10 natural numbers

```python
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)
```

#### Example 2: Factorial

```python
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial of", n, "is", fact)
```

#### Example 3: Fibonacci

```python
n = 10
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b
```

---

##  6. Assignments & Practice Problems (30 min)
Solve these:

1. Print multiplication tables from **1 to 10** (nested loop).
2. Write a program to find the **sum of digits of a number**.
3. Print the following pattern:

   ```
   1
   1 2
   1 2 3
   1 2 3 4
   1 2 3 4 5
   ```
4. Write a program to check if a number is **prime** using loops.
5. Write a program to reverse a string using a loop.
6. Print all numbers divisible by **3 and 5** between 1 and 100.
7. Write a program to print **Armstrong numbers** between 1 and 500.
8. Write a program to print a **diamond pattern** using stars.
9. Write a program that takes 10 numbers and prints the **maximum and minimum**.
10. Write a program that prints all **palindrome numbers** between 100 and 500.




