# **Star Patterns**

### 1. Square Pattern

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

### 2. Right Triangle

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
```

```
*
* *
* * *
* * * *
* * * * *
```

---

### 3. Inverted Right Triangle

```python
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

```
* * * * *
* * * *
* * *
* *
*
```

---

### 4. Pyramid Pattern

```python
rows = 5
for i in range(1, rows+1):
    print(" "*(rows-i) + "* " * i)
```

```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

---

### 5. Inverted Pyramid

```python
rows = 5
for i in range(rows, 0, -1):
    print(" "*(rows-i) + "* " * i)
```

```
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
```

---

### 6. Diamond Pattern

```python
rows = 5
# upper
for i in range(1, rows+1):
    print(" "*(rows-i) + "* " * i)
# lower
for i in range(rows-1, 0, -1):
    print(" "*(rows-i) + "* " * i)
```

```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
```

---

# **Number Patterns**

### 7. Number Triangle

```python
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
```

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

### 8. Inverted Number Triangle

```python
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
```

```
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
```

---

### 9. Repeated Number Pattern

```python
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()
```

```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

---

### 10. Floyd’s Triangle

```python
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```

```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

---

# **Alphabet Patterns**

### 11. Alphabet Triangle

```python
import string
letters = string.ascii_uppercase

for i in range(5):
    for j in range(i+1):
        print(letters[j], end=" ")
    print()
```

```
A
A B
A B C
A B C D
A B C D E
```

---

### 12. Repeated Alphabet Triangle

```python
import string
letters = string.ascii_uppercase

for i in range(5):
    for j in range(i+1):
        print(letters[i], end=" ")
    print()
```

```
A
B B
C C C
D D D D
E E E E E
```

---

# **Complex Patterns**

### 13. Hollow Square

```python
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

```
* * * * *
*       *
*       *
*       *
* * * * *
```

---

### 14. X Pattern

```python
n = 5
for i in range(n):
    for j in range(n):
        if i == j or i+j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

```
*       *
  *   *  
    *    
  *   *  
*       *
```

---

### 15. Hourglass Pattern

```python
rows = 5
# upper inverted
for i in range(rows, 0, -1):
    print(" "*(rows-i) + "* " * i)
# lower pyramid
for i in range(2, rows+1):
    print(" "*(rows-i) + "* " * i)
```

```
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

