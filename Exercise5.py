# Exercise 5
"""
Tip Calculator

Write these functions:

- `calculateTip(billAmount, tipPercent)` — returns the tip amount
- `splitBill(billAmount, tipPercent, numPeople)` — returns how much each person pays (bill + tip divided equally)
- `printBillSummary(billAmount, tipPercent, numPeople)` — prints a full summary:

```
Bill:           $85.00
Tip (18%):      $15.30
Total:          $100.30
People:         4
Each person:    $25.08
```

Test with at least 3 different scenarios.

Hint: look up `round()` to keep it to 2 decimal places.
"""

def calculateTip(billAmount, tipPercent):
    return billAmount * (tipPercent/100)

def splitBill(billAmount, tipPercent, numPeople):
    tip = calculateTip(billAmount, tipPercent)
    total = billAmount + tip
    return total/numPeople

def printBillSummary(billAmount, tipPercent, numPeople):
    tip = calculateTip(billAmount, tipPercent)
    total = billAmount + tip
    eachPerson = splitBill(billAmount, tipPercent, numPeople)

    print(f"Bill:           ${billAmount:.2f}")
    print(f"Tip ({tipPercent}%):      ${tip:.2f}")
    print(f"Total:          ${total:.2f}")
    print(f"People:         {numPeople}")
    print(f"Each person:    ${eachPerson:.2f}")
    print()

# tests
printBillSummary(86.89, 19, 5)
printBillSummary(40, 10, 2)
printBillSummary(896, 30, 8)
