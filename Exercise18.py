# Exercise 18
"""
Number Guessing Game Logic

Write these functions (no `input()` needed — test by calling them directly):

- `generateTarget(low, high)` — returns a random number between low and high. Use Python's `random` module: `import random` then `random.randint(low, high)`
- `checkGuess(guess, target)` — returns `"Too high"`, `"Too low"`, or `"Correct!"`
- `playGame(guesses)` — takes a list of guesses and a pre-set target. Goes through each guess in order, prints the result for each, and stops when the correct answer is guessed. Prints how many guesses it took.

Example output:
```
Guess 1: 50 → Too high
Guess 2: 25 → Too low
Guess 3: 37 → Too low
Guess 4: 43 → Correct! You got it in 4 guesses.
```

Test with a target of `43` and guesses `[50, 25, 37, 43]`.
"""
import random

def generateTarget(low, high):
    return random.randint(low, high)

def checkGuess(guess, target):
    if guess > target:
        return "Too high"
    elif guess < target:
        return "Too low"
    else:
        return "Correct!"

def playGame(guesses):
    target = 43 # Pre-set target for testing

    for i in range(len(guesses)):
        result = checkGuess(guesses[i], target)

        if result == "Correct!":
            print(
                f"Guess {i + 1}: {guesses[i]} -> "
                f"Correct! You got it in {i + 1} guesses."
            )
            break
        else:
            print(f"Guess {i + 1}: {guesses[i]} -> {result}")

# test
playGame([50, 25, 37, 43])