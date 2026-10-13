# Loops and Lists: Notes

## Lists
```python
names = ["Ana", "Ben", "Cara"]
names[0]            # "Ana" (index starts at 0)
names[2]            # "Cara"
names.append("Dev") # adds to the end
len(names)          # number of items
names[0:2]          # ["Ana", "Ben"] (end index not included)
```

## The for loop
```python
for n in [1, 2, 3]:
    print(n * 2)
```
- `n` is a box that gets refilled with the next item on every lap.
- The indented lines are the loop body. They run once per lap.
- Prints 2, 4, 6 on separate lines.
- When the list runs out, the loop stops and the program moves on.

## Indentation matters
```python
total = 0
for n in [1, 2, 3]:
    total = total + n
print(total)        # outside the loop: prints 6 once
```
If `print(total)` were indented under the `for`, it would run every lap and print 1, 3, 6.

## Two patterns
**Counter**: adds 1 each time. Counts laps or events.
```python
count = 0
for n in [5, 10, 15]:
    count = count + 1
print(count)        # 3 (the values never mattered)
```

**Accumulator**: adds the item's value. Builds a running total.
```python
total = 0
for n in [1, 2, 3]:
    total = total + n   # new total = old total + current n
```

| Lap | n | total before | total after |
|---|---|---|---|
| start | | | 0 |
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |

Use a table like this to trace any loop by hand before running it.

## Where I used it
`tester.py` in threatline loops over a list of attack strings and uses a counter (`leaks`) that goes up by 1 only when the secret code leaks. `len(attacks)` gives the total.

## Gotchas
- A missing comma between two strings in a list glues them into one string.
- Loop body must be indented, or it is not part of the loop.