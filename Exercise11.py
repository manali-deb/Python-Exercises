# Exercise 11
"""
Number Statistics

Write a function `getStats(numbers)` that takes a list of numbers and returns a dictionary with:
- `"count"` — how many numbers are in the list
- `"total"` — the sum of all numbers
- `"average"` — the average
- `"minimum"` — the smallest number
- `"maximum"` — the largest number
- `"range"` — the difference between max and min

Then write `printStats(numbers)` that prints each stat on its own line.

Test with: `[4, 8, 15, 16, 23, 42]`, `[100, 200, 50, 75, 125]`, `[3]`

Do NOT use Python's built-in `sum()`, `min()`, or `max()` — write the logic yourself using a loop.
"""
def getStats(numbers):
    count = len(numbers)

    total = 0
    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers:
        total += num
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    average = total / count
    range = maximum - minimum

    numDict = {
        "count": count,
        "total": total,
        "average": average,
        "minimum": minimum,
        "maximum": maximum,
        "range": range
    }

    return numDict

def printStats(numbers):
    numDict = getStats(numbers)
    print(f"Statistics for {numbers}:")
    for key, value in numDict.items():
        print(f"{key}: {value}")

    print()

# test
set1 = [4, 8, 15, 16, 23, 42]
set2 = [100, 200, 50, 75, 125]
set3 = [3]

printStats(set1)
printStats(set2)
printStats(set3)