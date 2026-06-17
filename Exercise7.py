# Exercise 7
"""
FizzBuzz Function

Write a function called `fizzBuzz(n)` that returns:
- `"FizzBuzz"` if n is divisible by both 3 and 5
- `"Fizz"` if n is divisible by 3 only
- `"Buzz"` if n is divisible by 5 only
- The number itself (as a string) if none of the above

Then write `printFizzBuzz(start, end)` that calls `fizzBuzz()` for every number from start to end and prints the result.

Call `printFizzBuzz(1, 30)`.

Hint: look up the `%` (modulo) operator
"""
def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0 and not n % 5 == 0:
        return "Fizz"
    elif n % 5 == 0 and not n % 3 == 0:
        return "Buzz"
    else:
        return str(n)
    
def printFizzBuzz(start, end):
    for num in range(start, end + 1):
        print(fizzBuzz(num))

# test
printFizzBuzz(1, 30)