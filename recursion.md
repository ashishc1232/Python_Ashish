
## 1. What is **Recursion**?

> **Recursion** is when a function **calls itself** to solve a smaller part of the same problem, until it reaches a **base case** that stops the recursion.

###  Basic Structure of a Recursive Function

```python
def recursive_function(parameters):
    # Base case: stop the recursion
    if stopping_condition:
        return result

    # Recursive case: call itself with smaller input
    return recursive_function(modified_parameters)
```

---

## 2. **Simple Examples** (to Understand the Flow)

### Example 1: Print Numbers from 1 to N

```python
def print_numbers(n):
    if n == 0:               # Base case
        return
    print_numbers(n - 1)     # Recursive call with smaller problem
    print(n)                 # After recursion

print_numbers(5)
```

**Output:**

```
1
2
3
4
5
```

**How it works:**

* `print_numbers(5)` calls `print_numbers(4)`
* … keeps going until `print_numbers(0)` (base case)
* Then numbers print while returning back → **Recursive Stack**

---

### Example 2: Factorial of a Number

> `factorial(n) = n × factorial(n-1)` and `factorial(0) = 1`

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

**Call stack for factorial(5):**
`factorial(5)` → `5 * factorial(4)` → `4 * factorial(3)` → … → `1`

---

### Example 3: Sum of First N Natural Numbers

```python
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(10))  # 55
```

This example shows recursion can replace loops when problems can be divided into smaller versions of themselves.

---

### Example 4: Reverse a String Using Recursion

```python
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  # "olleh"
```

Here the recursive call keeps slicing off the first character until empty, then concatenates in reverse.

---

## 3. Backtracking – Introduction

> **Backtracking** is a special kind of recursion where we **explore all possibilities** for a problem, and **backtrack** (undo a step) when a path does not lead to a solution.

Think of:

* Going through a **maze**
* Trying all combinations / permutations
* Solving Sudoku

---

### Key Idea of Backtracking

```python
def backtrack(current_state):
    if solution_found(current_state):
        record_solution(current_state)
        return

    for choice in possible_choices(current_state):
        make_choice(choice)
        backtrack(updated_state)
        undo_choice(choice)  # backtrack
```

---

## 4. Backtracking Examples (Step by Step)

### Example 1: Generate All Subsets of a List

For list `[1, 2, 3]`, subsets are:
`[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]`

```python
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])  # copy current subset
        for i in range(start, len(nums)):
            current.append(nums[i])        # choose
            backtrack(i + 1, current)      # explore
            current.pop()                  # backtrack

    backtrack(0, [])
    return result

print(subsets([1, 2, 3]))
```

---

### Example 2: Generate All Permutations of a List

For `[1, 2, 3]` → 6 permutations

```python
def permutations(nums):
    result = []

    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        for num in nums:
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()  # backtrack

    backtrack([])
    return result

print(permutations([1, 2, 3]))
```

---

### Example 3: N-Queens Problem (Classic)

> Place N queens on an N×N chessboard such that no two queens attack each other.

For simplicity, N = 4:

```python
def solve_n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        # Check column
        for r in range(row):
            if board[r][col] == "Q":
                return False

        # Check left diagonal
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        # Check right diagonal
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        return True

    def backtrack(row):
        if row == n:
            solutions.append(["".join(r) for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."  # backtrack

    backtrack(0)
    return solutions

solutions = solve_n_queens(4)
for s in solutions:
    for row in s:
        print(row)
    print()
```

---

## 5. Performance Considerations

Recursive and backtracking solutions are elegant but can be **slow or memory-heavy** if not used carefully. Here’s why:

| Aspect               | Recursion                                                                                | Backtracking                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Call Stack Usage** | Each recursive call takes memory (stack frame). Deep recursion can cause stack overflow. | Same, but typically even deeper calls due to exploring multiple choices             |
| **Time Complexity**  | Depends on the recurrence relation. Some are O(n), some exponential.                     | Often **exponential** because it tries many combinations (e.g., O(2^n) for subsets) |
| **Space Complexity** | At least O(depth of recursion)                                                           | Also includes extra space for choices/state                                         |
| **Optimization**     | Use memoization (caching results) for overlapping subproblems                            | Use pruning (stop exploring when a partial path is invalid)                         |

### Example: Fibonacci with Naive Recursion (Bad Performance)

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(35))  # very slow
```

This runs in **O(2^n)** time because it recalculates the same subproblems repeatedly.

### Optimized Fibonacci with Memoization

```python
memo = {}

def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

print(fib_memo(35))  # much faster
```

---

## 6. When to Use Recursion and Backtracking

 **Good use cases:**

* Problems naturally defined recursively (factorial, tree traversal)
* Divide-and-conquer algorithms (Merge Sort, Quick Sort)
* Combinatorial problems (permutations, subsets)
* Backtracking problems (Sudoku, N-Queens, Maze)

 **Avoid if:**

* Recursion depth might exceed Python’s limit (default ~1000)
* The problem is easily solved with iteration
* Performance-critical paths where recursion overhead matters

---

## 7. Practice Problems for You

Try writing recursive or backtracking solutions for:

1. Sum of digits of a number using recursion
2. Count the number of ways to climb N stairs (1 or 2 steps at a time)
3. Generate all binary strings of length N
4. Solve a maze using backtracking (path from start to end)
5. Combination Sum: given a list and a target, find all combinations that sum to target



