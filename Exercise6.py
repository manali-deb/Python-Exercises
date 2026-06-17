# Exercise 6
"""
Word Analyzer

Write a function `analyzeWord(word)` that returns a dictionary with:
- `"length"` — number of characters
- `"uppercase"` — word in all caps
- `"lowercase"` — word in all lowercase
- `"reversed"` — word spelled backwards
- `"vowel_count"` — count of vowels (a, e, i, o, u)
- `"is_palindrome"` — True if the word reads the same forwards and backwards

Then write `printAnalysis(word)` that prints each key and value neatly.

Test with: `"Python"`, `"racecar"`, `"Hello"`, `"level"`, `"Manali"`
"""
def analyzeWord(word):
    vowels = "aeiou"
    vowel_count = 0

    for char in word.lower():
        if char in vowels:
            vowel_count += 1

    analysis = {
        "length": len(word),
        "uppercase": word.upper(),
        "lowercase": word.lower(),
        "reversed": word[::-1],
        "vowel_count": vowel_count,
        "is_palindrome": word.lower() == word[::-1].lower()
    }

    return analysis

def printAnalysis(word):
    analysis = analyzeWord(word)

    print(f"Analysis for '{word}'")

    for key, value in analysis.items():
        print(f"{key}: {value}")

    print()

# tests
printAnalysis("Python")
printAnalysis("racecar")
printAnalysis("Hello")
printAnalysis("level")
printAnalysis("Manali")
