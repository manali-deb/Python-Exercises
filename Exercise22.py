# Exercise 22
"""
Inventory System

Build a product inventory with these functions:

- `addProduct(inventory, name, price, quantity)` — adds a product, returns `"Added"` or `"Product already exists"`
- `restock(inventory, name, quantity)` — increases quantity, returns `"Restocked"` or `"Product not found"`
- `sell(inventory, name, quantity)` — decreases quantity, returns `"Sold"`, `"Not enough stock"`, or `"Product not found"`
- `getLowStock(inventory, threshold)` — returns a list of products where quantity is at or below the threshold
- `getTotalValue(inventory)` — returns the total value of all stock (price × quantity for each product)
- `printInventory(inventory)` — prints a table:

```
INVENTORY
================================================
Product          Price     Qty    Value
------------------------------------------------
T-Shirt          $25.00    50     $1,250.00
Jeans            $60.00    12     $720.00
Sneakers         $90.00    3      $270.00
------------------------------------------------
Total value: $2,240.00
Low stock (<=5): Sneakers
================================================
```

Write a script that adds 5 products, sells some, restocks one, and prints the full inventory.
"""
def addProduct(inventory, name, price, quantity):
    for product in inventory:
        if product["name"] == name:
            return "Product already exists"
        
    inventory.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

    return "Added"

def restock(inventory, name, quantity):
    for product in inventory:
        if product["name"] == name:
            product["quantity"] += quantity
            return "Restocked"
        
    return "Product not found"

def sell(inventory, name, quantity):
    for product in inventory:
        if product["name"] == name:
            if quantity > product["quantity"]:
                return "Not enough stock"
            
            product["quantity"] -= quantity
            return "Sold"
    
    return "Product not found"

def getLowStock(inventory, threshold):
    low_stock = []

    for product in inventory:
        if product["quantity"] <= threshold:
            low_stock.append(product["name"])

    return low_stock

def getTotalValue(inventory):
    total_value = 0

    for product in inventory:
        total_value += product["price"] * product["quantity"]

    return total_value

def printInventory(inventory):
    print("INVENTORY")
    print("=" * 48)
    print(f"{'Product':<15} {'Price':<10} {'Qty':<6} {'Value'}")
    print("-" * 48)

    for product in inventory:
        value = product["price"] * product["quantity"]

        print(
            f"{product['name']:<15} "
            f"${product['price']:<9.2f} "
            f"{product['quantity']:<6} "
            f"${value:,.2f}"
        )

    print("-" * 48)

    total_value = getTotalValue(inventory)
    low_stock = getLowStock(inventory, 5)

    print(f"Total value: ${total_value:,.2f}")

    if low_stock:
        print(f"Low stock (<=5): {', '.join(low_stock)}")
    else:
        print("Low stock (<=5): None")

    print("=" * 48)

# test
inventory = []

print(addProduct(inventory, "T-Shirt", 25.00, 50))
print(addProduct(inventory, "Jeans", 60.00, 12))
print(addProduct(inventory, "Sneakers", 90.00, 3))
print(addProduct(inventory, "Hat", 20.00, 8))
print(addProduct(inventory, "Socks", 10.00, 30))

print(sell(inventory, "T-Shirt", 5))
print(sell(inventory, "Jeans", 2))
print(sell(inventory, "Socks", 10))

print(restock(inventory, "Sneakers", 4))

print()
printInventory(inventory)