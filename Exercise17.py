# Exercise 17
"""
Sentence Builder

Write a function `buildProfile(firstName, lastName, age, city, job)` that returns a formatted multi-line string:

```
====================
Name:  Manali Singh
Age:   25
City:  Toronto
Job:   Developer
====================
```

Write a function `buildTeam(members)` where `members` is a list of dictionaries, each with keys `firstName`, `lastName`, `age`, `city`, `job`. It should call `buildProfile()` for each member and print them all.

Create a team of at least 5 people and print the full team.
"""

def buildProfile(firstName, lastName, age, city, job):
    profile = (
        "===================="
        f"\nName:  {firstName} {lastName}"
        f"\nAge:   {age}"
        f"\nCity:  {city}"
        f"\nJob:   {job}"
        "\n===================="
    )
    return profile

def buildTeam(members):
    for member in members:
        print(
            buildProfile(
                member["firstName"],
                member["lastName"],
                member["age"],
                member["city"],
                member["job"]
            )
        )
        print()

# test
team = [
    {
        "firstName": "Manali",
        "lastName": "Deb",
        "age": 22,
        "city": "Chicago",
        "job": "Developer"
    },
    {
        "firstName": "Frodo",
        "lastName": "Baggins",
        "age": 33,
        "city": "The Shire",
        "job": "Ring Bearer"
    },
    {
        "firstName": "Gandalf",
        "lastName": "the Grey",
        "age": 2040,
        "city": "The Shire",
        "job": "Wizard"
    },
    {
        "firstName": "Aragorn",
        "lastName": "Telcontar",
        "age": 87,
        "city": "Isildur",
        "job": "Prince"
    },
    {
        "firstName": "Legolas",
        "lastName": "Thranduilion",
        "age": 2931,
        "city": "Rivendell",
        "job": "Prince"
    }
]

buildTeam(team)