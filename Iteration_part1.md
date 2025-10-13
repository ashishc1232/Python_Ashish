
# **1. For Loop**

Used when you know the number of iterations in advance (e.g., iterating over a list, string, range).

### Example 1: Print numbers from 1 to 10

```python
for i in range(1, 11):
    print(i)
```

### Example 2: Print even numbers from 2 to 20

```python
for i in range(2, 21, 2):
    print(i)
```

### Example 3: Iterate through a list

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---

# **2. While Loop**

Used when the number of iterations is **not fixed**, and the loop runs until a condition becomes `False`.

### Example 4: Print numbers from 1 to 10

```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

### Example 5: Sum of first 10 natural numbers

```python
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum:", total)
```

### Example 6: Reverse a number

```python
num = 1234
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed:", rev)
```

---

# **3. Nested Loops**

Loops inside another loop.

### Example 7: Multiplication table (1 to 5)

```python
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("------")
```

### Example 8: Print a rectangle of stars

```python
for i in range(4):  # 4 rows
    for j in range(5):  # 5 columns
        print("*", end=" ")
    print()
```

### Example 9: Print a right triangle pattern

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
```

---

# **4. Iteration Patterns**

### Example 10: Sum of numbers in a list

```python
numbers = [5, 10, 15, 20]
total = 0
for num in numbers:
    total += num
print("Sum:", total)
```

### Example 11: Find maximum number in a list

```python
numbers = [12, 45, 67, 23, 89, 34]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("Maximum:", max_num)
```

### Example 12: Count vowels in a string

```python
text = "Hello Python Loops"
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Vowel count:", count)
```

### Example 13: Factorial of a number

```python
num = 5
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial:", fact)
```

### Example 14: Fibonacci series (first 10 numbers)

```python
a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a+b
```

### Example 15: Prime number check

```python
num = 29
is_prime = True

for i in range(2, int(num**0.5)+1):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print(num, "is Prime")
else:
    print(num, "is Not Prime")
```

Sure. Here are the code solutions one by one as requested:

---

**I. WAP to check whether given number is prime or not**

```python
num = int(input("Enter a number: "))
if num <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
```

---

**II. WAP to check palindrome for string and number both**

```python
value = input("Enter a string or number: ")
if value == value[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
```

---

**III. WAP to check given value (string or number) is Armstrong or not**

```python
value = input("Enter a number: ")
if value.isdigit():
    num = int(value)
    power = len(value)
    total = sum(int(digit) ** power for digit in value)
    if total == num:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
else:
    print("Invalid input: not a number")
```

---

**IV. WAP of Fibonacci series**

```python
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
```

---

**V. Swap two variables without using third variable**

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, ", b =", b)
```

---

**VI. Check for even or odd without using % and /**

```python
num = int(input("Enter a number: "))
if (num & 1) == 0:
    print("Even number")
else:
    print("Odd number")
```

---

**VII. Swap three variables without using fourth variable**

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

a = a + b + c
b = a - (b + c)
c = a - (b + c)
a = a - (b + c)

print("After swapping: a =", a, ", b =", b, ", c =", c)
```



