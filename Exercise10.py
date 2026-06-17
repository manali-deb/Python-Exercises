# Exercise 10
"""
Sentence Analyzer

Write a function `analyzeSentence(sentence)` that returns a dictionary with:
- `"word_count"` — number of words
- `"char_count"` — number of characters (not counting spaces)
- `"longest_word"` — the longest word in the sentence
- `"shortest_word"` — the shortest word in the sentence
- `"uppercase_sentence"` — the full sentence in caps

Then write `printSentenceReport(sentence)` that prints everything neatly.

Test with:
- `"The quick brown fox jumps over the lazy dog"`
- `"Python is a great programming language"`
- `"I love coding"`

Hint: look up `.split()` and `len()`.
"""
def analyzeSentence(sentence):
    words = sentence.split()
    longest_word = words[0]
    shortest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

        if len(word) < len(shortest_word):
            shortest_word = word

    analysis = {
        "word_count": len(words),
        "char_count": len(sentence.replace(" ", "")),
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "uppercase_sentence": sentence.upper()
    }

    return analysis

def printSentenceReport(sentence):
    analysis = analyzeSentence(sentence)
    
    print(f"Analysis for '{sentence}':")

    for key, value in analysis.items():
        print(f"{key}: {value}")
    
    print()

# tests
printSentenceReport("The quick brown fox jumps over the lazy dog")
printSentenceReport("Python is a great programming language")
printSentenceReport("I love coding")

