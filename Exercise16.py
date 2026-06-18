# Exercise 16
"""
Simple ATM

Write these functions to simulate an ATM:

- `createAccount(name, pin, initialBalance)` — returns an account dictionary
- `checkBalance(account)` — prints `"Balance: $500.00"`
- `deposit(account, amount)` — adds money, returns `"Deposited $X. New balance: $Y"` or `"Amount must be positive"`
- `withdraw(account, amount)` — removes money, returns the right message or `"Insufficient funds"` or `"Amount must be positive"`
- `login(account, pin)` — returns `True` if pin matches, `False` otherwise

Write a script that creates an account, logs in with a wrong pin (should fail), logs in with the correct pin, deposits money, withdraws money, tries to overdraft, and prints the balance at each step.
"""

def createAccount(name, pin, initialBalance):
    return {
        "name": name,
        "pin": pin,
        "balance": initialBalance
    }

def checkBalance(account):
    print(f"Balance: ${account['balance']:.2f}")

def deposit(account, amount):
    if amount <= 0:
        return "Amount must be positive"
    
    account["balance"] += amount
    return (
        f"Deposited ${amount:.2f}"
        f"\nNew balance: ${account['balance']:.2f}"
    )

def withdraw(account, amount):
    if amount <= 0:
        return "Amount must be positive"
    
    if amount > account['balance']:
        return "Insufficient funds"
    
    account['balance'] -= amount

    return (
        f"Withdrew ${amount:.2f}"
        f"\nNew balance: ${account['balance']:.2f}"
    )

def login(account, pin):
    return account['pin'] == pin

# test
account = createAccount("Manali", "1234", 500)

print("login attempt with wrong pin:")
print(login(account, "9999"))

print("\nlogin attempt with correct pin:")
print(login(account, "1234"))

print("\ninitial balance:")
checkBalance(account)

print("\ndeposit:")
print(deposit(account, 250))
checkBalance(account)

print("\nwithdraw:")
print(withdraw(account, 100))
checkBalance(account)

print("\nwithdraw too much money:")
print(withdraw(account, 1000))
checkBalance(account)