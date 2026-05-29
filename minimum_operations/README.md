# Minimum Operations

## Description

This project contains a function that calculates the minimum number of operations needed to get exactly `n` characters `H` in a text file.

The file starts with one character:

```text
H
```

Only two operations are allowed:

- Copy All
- Paste

The goal is to reach exactly `n` characters using the minimum number of operations.

## Reflexion

If you want exactly 6 H in your file you must copy it once, and you can paste it 5 times, but it probably won't be the minimum number of operations :

```H | Copy -->(paste) HH -->(paste) HHH -->(paste) HHHH -->(paste) HHHHH --> (paste) HHHHHH```

It takes 6 operations to get 6 H in our file.

You can also paste it to get 3 H, and then copy it again to paste the 3 H again :
```H | Copy -->(paste) HH -->(paste) HHH --> Copy -->(paste) HHHHHH```

With that method, it takes 5 operations.
Instead of doing 
```text 
1 Copy + 5 Pastes = 6 operations
```

We did 

```text
1 Copy + 2 Pastes + 1 Copy + 1 Paste = 5 operations
```


## Solution

The solution uses the prime factors of `n`.

<i>Prime factors : 2, 3, 5, 7, 11, 13...etc</i>

For example:

```text
12 = 2 × 2 × 3
```

The minimum number of operations is:

```text
4 = 2 x 2
```

The function finds the factors of `n` and adds them together.

```text
for n = 12 ----> 2 + 2 + 3 = 7 operations
for n = 4 -----> 2 + 2 = 4 operations
```

## Example

```python
>>> minOperations(12)
7

>>> minOperations(9)
6

>>> minOperations(1)
0
```
