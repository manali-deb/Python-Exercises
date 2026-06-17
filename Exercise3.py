# Exercise 3
"""
Grade Calculator

Write a function called `getGrade(score)`:
- 90 and above → `"A"`
- 80–89 → `"B"`
- 70–79 → `"C"`
- 60–69 → `"D"`
- Below 60 → `"F"`
- Below 0 or above 100 → `"Invalid score"`

Then write `printReport(name, score)` that calls `getGrade()` and prints:
```
Manali scored 85/100 and received a B
```

Test with scores: `105`, `95`, `83`, `74`, `61`, `45`, `-5`
"""
def getGrade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def printReport(name, score):
    grade = getGrade(score)
    print(f"{name} scored {score}/100 and received a {grade}")

# tests
printReport("Manali", 85)
printReport("John", 105)
printReport("Jane", 95)
printReport("Benny", 83)
printReport("Basab", 74)
printReport("Cyrus", 61)
printReport("Mateo", 45)
printReport("Utkarsh", -5)
printReport("Boundary Test", 79)