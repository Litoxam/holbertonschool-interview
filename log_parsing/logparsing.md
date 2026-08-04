# Log Parsing

## Objective

This script reads log entries from **standard input (`stdin`)**, computes metrics, and prints them every **10 lines** or when the program is interrupted with **`Ctrl + C`**.

---

## Expected Input Format

Each line must match the following format:

```text
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

Example:

```text
192.168.1.1 - [2026-08-04 15:30:00.123456] "GET /projects/260 HTTP/1.1" 200 512
```

If a line does not match this format, it is ignored.

---

## Main Variables

### `total_size`

Stores the total size of all valid log entries.

```python
total_size = 0
```

---

### `line_count`

Counts how many lines have been read.

```python
line_count = 0
```

Every 10 lines, the current statistics are printed.

---

### `status_codes`

A dictionary used to count how many times each valid HTTP status code appears.

Example:

```python
{
    "200": 4,
    "404": 2,
    "500": 1
}
```

---

## Regular Expression

```python
pattern = re.compile(
    r'^\S+ - \[.*\] "GET /projects/260 HTTP/1.1" (\S+) (\S+)$'
)
```

This regular expression checks that a log line has the expected format.

The parentheses create two capture groups:

* **Group 1:** HTTP status code
* **Group 2:** File size

These values are retrieved using:

```python
status = match.group(1)
size = int(match.group(2))
```

---

## Reading the Input

```python
for line in sys.stdin:
```

The program reads one log line at a time from standard input.

Each line increases the line counter.

---

## Validating a Line

```python
match = pattern.fullmatch(line.strip())
```

`fullmatch()` verifies that the entire line matches the regular expression.

If the line is valid:

* the status code is extracted;
* the file size is extracted;
* the file size is added to the total;
* the status code counter is updated.

---

## Updating the Total File Size

```python
total_size += size
```

Every valid line contributes its file size to the total.

---

## Counting Status Codes

Only the following status codes are counted:

* 200
* 301
* 400
* 401
* 403
* 404
* 405
* 500

If a valid status code is found:

```python
if status in status_codes:
    status_codes[status] += 1
else:
    status_codes[status] = 1
```

---

## Printing Statistics

Every 10 processed lines:

```python
if line_count % 10 == 0:
    print_stats(total_size, status_codes)
```

The output format is:

```text
File size: 1024
200: 5
301: 2
404: 1
```

Only status codes that appeared at least once are displayed.

---

## Keyboard Interrupt

If the program is interrupted with **Ctrl + C**, the current statistics are printed before exiting.

```python
except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise
```

---

## Algorithm

1. Read a line from `stdin`.
2. Check whether the line matches the expected format.
3. Extract the HTTP status code and file size.
4. Add the file size to the total.
5. Count the status code if it is one of the valid codes.
6. Every 10 lines, print the current statistics.
7. Print the final statistics when the program ends or is interrupted.

---
