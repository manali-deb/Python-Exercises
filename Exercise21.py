# Exercise 21
"""
Currency Converter

Write a function `convert(amount, fromCurrency, toCurrency)` using these fixed exchange rates (store them in a dictionary):

```
USD = 1.0
CAD = 1.36
EUR = 0.92
GBP = 0.79
JPY = 149.50
INR = 83.12
```

The function should:
1. Convert `fromCurrency` to USD first
2. Then convert USD to `toCurrency`
3. Return the converted amount rounded to 2 decimal places
4. Return `"Unknown currency"` if either currency code is not in the dictionary

Then write `printConversion(amount, fromCurrency, toCurrency)`:
```
500 CAD = 367.65 USD
367.65 USD = 47,582.68 JPY
```

Test at least 8 different conversions.
"""
def convert(amount, fromCurrency, toCurrency):
    exchange_rates = {
        "USD": 1.0,
        "CAD": 1.36,
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 149.50,
        "INR": 83.12
    }

    if (
        fromCurrency not in exchange_rates
        or toCurrency not in exchange_rates
    ):
        return "Unknown currency"
    
    usd_amount = amount / exchange_rates[fromCurrency]

    converted_amount = usd_amount * exchange_rates[toCurrency]

    return round(converted_amount, 2)

def printConversion(amount, fromCurrency, toCurrency):
    result = convert(amount, fromCurrency, toCurrency)

    if result == "Unknown currency":
        print(result)
    else:
        print(
            f"{amount:.2f} {fromCurrency} = "
            f"{result:.2f} {toCurrency}"
        )

# tests
printConversion(500, "CAD", "USD")
printConversion(367.65, "USD", "JPY")
printConversion(100, "USD", "CAD")
printConversion(250, "EUR", "GBP")
printConversion(1000, "JPY", "USD")
printConversion(5000, "INR", "EUR")
printConversion(100, "GBP", "INR")
printConversion(50, "CAD", "EUR")
printConversion(100, "USD", "ABC") # invalid test