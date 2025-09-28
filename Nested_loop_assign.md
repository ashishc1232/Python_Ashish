#  Assignments with Solutions

##  Multiplication Tables (1 to 10)

```python
for i in range(1, 11):      # tables from 1 to 10
    print("Table of", i)
    for j in range(1, 11):  # numbers 1 to 10
        print(i, "x", j, "=", i*j)
    print()   # blank line for separation
```



##  Sum of Digits of a Number

```python
num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits:", total)
```

---

##  Number Pattern

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

```python
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
```

---

##  Prime Number Check

```python
num = int(input("Enter a number: "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is Prime")
else:
    print(num, "is NOT Prime")
```

---

##  Reverse a String

```python
text = input("Enter a string: ")
reversed_str = ""

for ch in text:
    reversed_str = ch + reversed_str

print("Reversed string:", reversed_str)
```

---

##  Numbers Divisible by 3 and 5 (1 to 100)

```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
```

---

##  Armstrong Numbers (1 to 500)

 Armstrong = sum of digits^power = number itself.

```python
for num in range(1, 501):
    power = len(str(num))  # number of digits
    temp = num
    total = 0
    
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    
    if total == num:
        print(num)
```

 Output:

```
1
153
370
371
407
```

---

##  Diamond Pattern

```python
n = 5  # height of half diamond

# upper half
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))

# lower half
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "*" * (2*i-1))
```

 Output:

```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

---

##  Max and Min from 10 Numbers

```python
numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
```

---

##  Palindrome Numbers (100 to 500)

 Palindrome = same forward & backward.

```python
for num in range(100, 501):
    if str(num) == str(num)[::-1]:
        print(num)
```

 Output:

```
101
111
121
131
...
494
```






