# Exercise 4
"""
Password Validator

Write a function `checkPassword(password)` that checks all these rules in order and returns the FIRST rule that fails:

1. Must be at least 8 characters → `"Too short"`
2. Must not be the word password → `"Too obvious"`
3. Must contain at least one number → `"Needs a number"`
4. Must contain at least one uppercase letter → `"Needs an uppercase letter"`
5. Must not contain spaces → `"No spaces allowed"`

If all rules pass, return `"Password accepted"`

Test with:
- `"abc"`
- `"password"`
- `"hellothere"`
- `"HelloThere"`
- `"Hello There1"`
- `"Hello123"`
- `"Tr0ub4dor"`
"""

def checkPassword(password):
    if len(password) < 8:
        return "Too Short"
    
    if password.lower() == "password":
        return "Too obvious"
    
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
    
    if not has_number:
        return "Needs a number"
    
    has_uppercase = False
    for char in password:
        if char.isupper():
            has_uppercase = True
            break
    
    if not has_uppercase:
        return "Needs an uppercase letter"
    
    if " " in password:
        return "No spaces allowed"
    
    return "Password accepted"

# tests
print(f'"abc" -> {checkPassword("abc")}')
print(f'"password" -> {checkPassword("password")}')
print(f'"hellothere" -> {checkPassword("hellothere")}')
print(f'"HelloThere" -> {checkPassword("HelloThere")}')
print(f'"Hello There1" -> {checkPassword("Hello There1")}')
print(f'"Hello123" -> {checkPassword("Hello123")}')
print(f'"Tr0ub4dor" -> {checkPassword("Tr0ub4dor")}')