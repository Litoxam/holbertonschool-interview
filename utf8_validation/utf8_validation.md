# UTF-8 Validation

## Objective

The goal of this project is to determine whether a list of integers represents a valid UTF-8 encoding.

Each integer represents **one byte**, and only the **8 least significant bits** are considered.

A UTF-8 character can use:

* 1 byte
* 2 bytes
* 3 bytes
* 4 bytes

---

## UTF-8 Format

| Character Length | First Byte | Following Bytes                  |
| ---------------- | ---------- | -------------------------------- |
| 1 byte           | `0xxxxxxx` | None                             |
| 2 bytes          | `110xxxxx` | `10xxxxxx`                       |
| 3 bytes          | `1110xxxx` | `10xxxxxx` `10xxxxxx`            |
| 4 bytes          | `11110xxx` | `10xxxxxx` `10xxxxxx` `10xxxxxx` |

The `x` bits can be either `0` or `1`.

---

## Algorithm

The algorithm reads the list one byte at a time.

### 1. Start of a character

If no continuation bytes are expected (`bytes_left == 0`), the program checks the first bits of the current byte to determine the character length.

Possible cases:

* `0xxxxxxx` → 1-byte character
* `110xxxxx` → start of a 2-byte character
* `1110xxxx` → start of a 3-byte character
* `11110xxx` → start of a 4-byte character

If none of these patterns match, the encoding is invalid.

---

### 2. Continuation bytes

If the character requires additional bytes, every following byte must begin with:

```text
10xxxxxx
```

If one of these bytes does not start with `10`, the function returns `False`.

---

### 3. End of validation

After reading all bytes:

* If every character is complete, return `True`.
* If the program is still waiting for continuation bytes, return `False`.

---

## Important Variables

### `bytes_left`

Keeps track of how many continuation bytes are still expected.

Example:

* `110xxxxx` → `bytes_left = 1`
* `1110xxxx` → `bytes_left = 2`
* `11110xxx` → `bytes_left = 3`

Each valid continuation byte decreases this value by 1.

---

## Bit Operations

### `byte = num & 0xFF`

Keeps only the last 8 bits of the integer.

This follows the project requirement that only one byte must be processed.

---

### Right Shift (`>>`)

The `>>` operator moves the bits to the right.

It is used to check the first bits of a byte.

Examples:

```python
(byte >> 7) == 0
```

Checks for:

```text
0xxxxxxx
```

```python
(byte >> 5) == 0b110
```

Checks for:

```text
110xxxxx
```

```python
(byte >> 4) == 0b1110
```

Checks for:

```text
1110xxxx
```

```python
(byte >> 3) == 0b11110
```

Checks for:

```text
11110xxx
```

```python
(byte >> 6) == 0b10
```

Checks whether a continuation byte begins with `10`.

---
