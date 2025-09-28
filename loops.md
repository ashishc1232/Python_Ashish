
#  Introduction to Loops

Loops are used to **execute a block of code repeatedly** until a condition is met.
Python mainly has **two types of loops**:

1. **for loop** → used when we know how many times we want to repeat.
2. **while loop** → used when we don’t know how many times, but we repeat until a condition becomes false.

---

##  **for Loop**

The `for` loop is used to iterate over a **sequence** (list, tuple, string, range, etc.).

### Example 1: Print numbers from 1 to 5

```python
for i in range(1, 6):
    print(i)
```

 Output:

```
1
2
3
4
5
```

---

### Example 2: Iterate over a list

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I like", fruit)
```

 Output:

```
I like apple
I like banana
I like cherry
```

---

##  **while Loop**

The `while` loop executes as long as the condition is `True`.

### Example 1: Print numbers from 1 to 5

```python
i = 1
while i <= 5:
    print(i)
    i += 1   # increase i to avoid infinite loop
```

 Output:

```
1
2
3
4
5
```

---

### Example 2: Sum of numbers until user enters 0

```python
total = 0
num = int(input("Enter a number (0 to stop): "))

while num != 0:
    total += num
    num = int(input("Enter a number (0 to stop): "))

print("Total sum is:", total)
```

---

##  Difference Between `for` and `while`

* Use **for loop** when number of iterations is known (like range, list).
* Use **while loop** when number of iterations is unknown (like user input until a condition is met).

---

##  Bonus: Using `break` and `continue`

### `break` → exit the loop

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

 Output:

```
1
2
3
4
```

---

### `continue` → skip current iteration

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

 Output:

```
1
2
4
5
```
 Assignment for You:

1. Print the multiplication table of 7 using a `for loop`.
2. Print all even numbers from 1 to 20 using a `while loop`.
3. Write a program that asks the user to guess a number until they guess correctly.


##  Multiplication Table of 7 (using `for loop`)

```python
num = 7

print("Multiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```

 Output:
```
Multiplication Table of 7
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

---

##  Print Even Numbers from 1 to 20 (using `while loop`)

```python
i = 1

print("Even numbers from 1 to 20:")
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
```

 Output:

```
Even numbers from 1 to 20:
2
4
6
8
10
12
14
16
18
20
```

---

##  Guess the Number Game (using `while loop`)

```python
secret_number = 9
guess = int(input("Guess the number: "))

while guess != secret_number:
    print("Wrong guess! Try again.")
    guess = int(input("Guess the number: "))

print(" Correct! You guessed it.")
```

 Sample Run:

```
Guess the number: 5
Wrong guess! Try again.
Guess the number: 7
Wrong guess! Try again.
Guess the number: 9
 Correct! You guessed it.
```

