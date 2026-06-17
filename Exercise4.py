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
    