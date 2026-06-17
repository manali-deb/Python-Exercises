# Exercise 9
"""
BMI Calculator

Write a function `calculateBMI(weightKg, heightM)` that returns the BMI value (formula: `weight / height²`).

Write a function `getBMICategory(bmi)` that returns:
- `"Underweight"` — below 18.5
- `"Normal"` — 18.5 to 24.9
- `"Overweight"` — 25 to 29.9
- `"Obese"` — 30 and above

Write a function `printBMIReport(name, weightKg, heightM)` that prints:
```
Name:     Manali
Weight:   65 kg
Height:   1.65 m
BMI:      23.88
Category: Normal
```

Test with at least 4 different people.
"""
def calculateBMI(weightKG, heightM):
    bmi = weightKG / heightM ** 2
    return bmi

def getBMICategory(bmi):
    if bmi > 30:
        return "Obese"
    elif bmi > 25:
        return "Overweight"
    elif bmi > 18.5:
        return "Normal"
    else:
        return "Underweight"
    
def printBMIReport(name, weightKG, heightM):
    bmi = calculateBMI(weightKG, heightM)

    print(f"Name:     {name}")
    print(f"Weight:   {weightKG:.2f} kg")
    print(f"Height:   {heightM:.2f} m")
    print(f"BMI:      {bmi:.2f}")
    print(f"Category: {getBMICategory(bmi)}")
    print()

# tests
printBMIReport("Manali", 65, 1.65)
printBMIReport("Benny", 100, 2)
printBMIReport("Basab", 300, 1.8)
printBMIReport("John", 85, 0.65)
