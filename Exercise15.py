# Exercise 15
"""
Contact Book

Build a contact book with these functions:

- `addContact(book, name, phone, email)` — adds a contact, returns `"Contact added"` or `"Contact already exists"` if name is already in the book
- `findContact(book, name)` — returns the contact's info or `"Contact not found"`
- `updatePhone(book, name, newPhone)` — updates a phone number, returns `"Updated"` or `"Not found"`
- `deleteContact(book, name)` — removes a contact, returns `"Deleted"` or `"Not found"`
- `printAllContacts(book)` — prints all contacts neatly:

```
Name:  Manali Singh
Phone: 416-555-1234
Email: manali@email.com
---------------------------
```

Write a script that:
1. Starts with an empty list
2. Adds 5 contacts
3. Prints all contacts
4. Searches for one contact
5. Updates a phone number
6. Deletes one contact
7. Prints the full list again to confirm
"""

def addContact(book, name, phone, email):
    for contact in book:
        if contact["name"] == name:
            return "Contact already exists"
        
    book.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    return "Contact added"


def findContact(book, name):
    for contact in book:
        if contact["name"] == name:
            return contact

    return "Contact not found"


def updatePhone(book, name, newPhone):
    for contact in book:
        if contact["name"] == name:
            contact["phone"] = newPhone
            return "Updated"
        
    return "Not found"


def deleteContact(book, name):
    for contact in book:
        if contact["name"] == name:
            book.remove(contact)
            return "Deleted"
        
    return "Not found"


def printAllContacts(book):
    for contact in book:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("-" * 32)

# tests
contact_book = []

print(addContact(contact_book, "Manali Deb", "416-555-1234", "manali@email.com"))
print(addContact(contact_book, "Benny Poon", "416-555-2345", "benny@email.com"))
print(addContact(contact_book, "Basab Dey", "416-555-3456", "basab@email.com"))
print(addContact(contact_book, "Cyrus Chau", "416-555-4567", "cyrus@email.com"))
print(addContact(contact_book, "Mateo Sanchez", "416-555-5678", "mateo@email.com"))

print("\nCONTACT LIST:")
printAllContacts(contact_book)

print("\nSEARCH RESULT:")
print(findContact(contact_book, "Basab Dey"))

print("\nUPDATE RESULT:")
print(updatePhone(contact_book, "Manali Deb", "416-999-9999"))

print("\nDELETE RESULT:")
print(deleteContact(contact_book, "Cyrus Chau"))

print("\nUPDATED CONTACT LIST:")
printAllContacts(contact_book)