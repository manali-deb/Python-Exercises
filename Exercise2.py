# Exercise 2
"""
Simple Calculator

Write a function called `calculate(a, b, operator)` where operator is `"+"`, `"-"`, `"*"`, or `"/"`.

- It should return the correct result
- If the operator is something else, return `"Invalid operator"`
- If dividing by zero, return `"Cannot divide by zero"`

Then write a `printCalculation(a, b, operator)` function that prints:
```
10 + 5 = 15
10 / 0 = Cannot divide by zero
```

Test with at least 8 different combinations.
"""

def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operator"
    
def printCalculation(a, b, operator):
    result = calculate(a, b, operator)
    print(f"{a} {operator} {b} = {result}")

# tests
printCalculation(10, 5, "+")
printCalculation(10, 0, "/")
printCalculation(8, 6, "+")
printCalculation(10, 15, "-") # negative numbers test
printCalculation(300, 84, "-")
printCalculation(18, 35, "*")
printCalculation(9, 8, "*")
printCalculation(95, 5, "/")
printCalculation(34, 6, "/") #decimal test