# Exercise 1
"""
Temperature Converter

Write three functions:

- `celsiusToFahrenheit(c)` — converts Celsius to Fahrenheit. Formula: `(c * 9/5) + 32`
- `fahrenheitToCelsius(f)` — converts Fahrenheit to Celsius. Formula: `(f - 32) * 5/9`
- `convertTemp(value, unit)` — takes a number and either `"C"` or `"F"` and calls the right function above

Print the results like:
```
100C = 212.0F
32F = 0.0C
```

Test with: `100C`, `32F`, `37C`, `98.6F`, `-40C`
"""

def celsiusToFahrenheit(c):
    return (c * 9  / 5) + 32

def fahrenheitToCelsius(f):
    return (f - 32) * 5 / 9

def convertTemp(value, unit):
    if unit == "C":
        converted = celsiusToFahrenheit(value)
        print(f"{value:.2f}C = {converted:.2f}F")
    elif unit == "F":
        converted = fahrenheitToCelsius(value)
        print(f"{value:.2f}F = {converted:.2f}C")
    else:
        "Invalid Input"

convertTemp(100, "C")
convertTemp(32, "F")
convertTemp(37, "C")
convertTemp(98.6, "F")
convertTemp(-40, "C")
