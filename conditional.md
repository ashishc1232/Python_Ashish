

# Conditional Statements (if-else, Nested Conditions)

Conditional statements allow us to **make decisions** in a program.
They let the program choose **different paths** of execution depending on conditions (true/false).

---

## 1. **Simple if Statement**

The `if` block runs only when the condition is **true**.

### Example:

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

**Logic:**

* `age >= 18` is **true**, so the message is printed.
* If `age` was less than 18, nothing would print.

---

## 2. **if-else Statement**

The `else` block runs when the condition is **false**.

### Example:

```python
marks = 40

if marks >= 35:
    print("You passed the exam.")
else:
    print("You failed the exam.")
```

**Logic:**

* If condition `marks >= 35` is **true**, print "Passed".
* If condition is **false**, print "Failed".

---

## 3. **if-elif-else (Multiple Conditions)**

Use when you have more than 2 possibilities.

### Example:

```python
temperature = 25

if temperature > 35:
    print("It's very hot.")
elif temperature > 20:
    print("It's a pleasant day.")
else:
    print("It's cold.")
```

**Logic:**

* Program checks conditions **in order**.
* Only the **first true condition** will run.

---

## 4. **Nested if (if inside another if)**

Sometimes decisions depend on **multiple levels** of conditions.

### Example:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can enter the club.")
    else:
        print("You need an ID to enter.")
else:
    print("You are too young to enter.")
```

**Logic:**

1. First check if `age >= 18`.
2. If true → check if `has_id` is True.
3. Based on both conditions, decide the output.

---
a = 10
b = 25
c = 17

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("The largest number is:", largest)

# Practice Questions for Students

1. Write a program to check if a number is **positive, negative, or zero**.
2. Write a program to check if a person is eligible for a **driving license**. (age ≥ 18 and must have learner’s license first).
3. Write a program to find the **largest of three numbers** using if-elif-else.
4. Write a program to check if a year is a **leap year**. (Condition: divisible by 4 but not 100, unless also divisible by 400).
5. A student’s marks are given. Print grade:

   * ≥90 → A
   * ≥75 → B
   * ≥50 → C
   * Else → Fail


