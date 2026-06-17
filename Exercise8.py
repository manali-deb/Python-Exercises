# Exercise 8
"""
Shopping Cart

Write these four functions:

- `addItem(cart, item, price)` — adds `{"item": item, "price": price}` to the cart list, returns the cart
- `removeItem(cart, item)` — removes the item from the cart by name, returns `"Removed"` or `"Item not found"`
- `getTotal(cart)` — adds up all prices and returns the total
- `printReceipt(cart, customerName)` — prints a formatted receipt:

```
Receipt for Manali:
--------------------------------
T-Shirt              $25.00
Jeans                $60.00
Sneakers             $90.00
--------------------------------
Total:               $175.00
```

Start with an empty list. Add 5 items. Remove 1. Print the receipt.
"""
def addItem(cart, item, price):
    cart.append({"item": item, "price": price,})
    return cart

def removeItem(cart, item):
    for product in cart:
        if product["item"] == item:
            cart.remove(product)
            return "Removed"
        
    return "Item not found"

def getTotal(cart):
    total = 0

    for product in cart:
        total += product["price"]

    return total

def printReceipt(cart, customerName):
    print(f"Receipt for {customerName}:")
    print("-" * 32)

    for product in cart:
        print(f"{product['item']} ${product['price']:.2f}")
    
    print("-" * 32)
    print(f"{'Total:'} ${getTotal(cart):.2f}")

# test
cart = []

# add 5 items
addItem(cart, "T-Shirt", 25)
addItem(cart, "Jeans", 60)
addItem(cart, "Sneakers", 90)
addItem(cart, "Bracelet", 900)
addItem(cart, "Socks", 5)

# remove 1
removeItem(cart, "Bracelet")

# give receipt
printReceipt(cart, "Manali")