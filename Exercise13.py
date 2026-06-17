# Exercise 13
"""
Rock Paper Scissors

Write a function `getResult(player, computer)` where both values are `"rock"`, `"paper"`, or `"scissors"`. Return:
- `"You win!"` if the player beats the computer
- `"Computer wins!"` if the computer wins
- `"It's a tie!"` if they're equal
- `"Invalid move"` if either value is not one of the three options

Then write `printGame(player, computer)` that prints:
```
Player:   rock
Computer: scissors
Result:   You win!
```

Test all possible combinations (there are 9).
"""

def getResult(player, computer):
    valid_moves = ['rock', 'paper', 'scissors']

    if player not in valid_moves or computer not in valid_moves:
        return "Invalid move"
    
    if player == computer:
        return "It's a tie!"
    
    if (
        (player == 'rock' and computer == 'scissors') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'paper' and computer == 'rock')
    ):
        return "You win!"
    
    return "Computer wins!"

def printGames(player, computer):
    result = getResult(player, computer)
    print(f"Player:   {player}")
    print(f"Computer: {computer}")
    print(f"Result:   {result}")
    print()

# tests
moves = ['rock', 'paper', 'scissors']

for player in moves:
    for computer in moves:
        printGames(player, computer)