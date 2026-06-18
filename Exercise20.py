# Exercise 20
"""
Student Report Card

Write these functions:

- `addStudent(classRoom, name, scores)` — `scores` is a list of numbers (test scores). Adds the student to the class list.
- `getAverage(scores)` — returns the average of a list of scores (write the loop yourself, no `sum()`)
- `getLetterGrade(average)` — same rules as Exercise 3
- `getTopStudent(classRoom)` — returns the name of the student with the highest average
- `printReportCard(student)` — prints a report for one student:

```
==============================
Student: Manali Singh
Scores:  88, 92, 79, 95, 84
Average: 87.6
Grade:   B
==============================
```

- `printClassReport(classRoom)` — prints every student's report card, then at the bottom prints:
```
Top student: Manali Singh (avg: 87.6)
Class average: 81.2
```

Create a class of 5 students with 5 scores each and print the full class report.
"""

def addStudent(classRoom, name, scores):
    classRoom.append({
        "name": name,
        "scores": scores
    })

def getAverage(scores):
    total = 0

    for score in scores:
        total += score

    return total / len(scores)

def getLetterGrade(average):
    if average < 0 or average > 100:
        return "Invalid score"
    elif average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def getTopStudent(classRoom):
    top_student = classRoom[0]["name"]
    highest_average = getAverage(classRoom[0]["scores"])

    for student in classRoom:
        avg = getAverage(student["scores"])

        if avg > highest_average:
            highest_average = avg
            top_student = student["name"]

    return top_student

def printReportCard(student):
    average = getAverage(student["scores"])
    grade = getLetterGrade(average)

    scores_string = ""

    for i in range(len(student["scores"])):
        scores_string += str(student["scores"][i])

        if i < len(student["scores"]) - 1:
            scores_string += ", "

    print("=" * 30)
    print(f"Student: {student['name']}")
    print(f"Scores:  {scores_string}")
    print(f"Average: {average:.1f}")
    print(f"Grade:   {grade}")
    print("=" * 30)

def printClassReport(classRoom):
    class_total = 0
    for student in classRoom:
        printReportCard(student)
        print()

        class_total += getAverage(student['scores'])

    top_student_name = getTopStudent(classRoom)

    top_avg = 0

    for student in classRoom:
        if student["name"] == top_student_name:
            top_avg = getAverage(student['scores'])
            break
        
    class_avg = class_total / len(classRoom)

    print(f"Top Student: {top_student_name} (avg: {top_avg:.1f})")
    print(f"Class average: {class_avg:.1f}")

# test
classRoom = []
addStudent(classRoom, "Manali Deb", [91, 99, 87, 95, 96])
addStudent(classRoom, "Benny Poon", [89, 90, 91, 97, 98])
addStudent(classRoom, "Basab Dey", [60, 65, 70, 72, 73])
addStudent(classRoom, "Cyrus Chau", [84, 80, 50, 90, 73])
addStudent(classRoom, "Mateo Sanchez", [40, 80, 64, 70, 55])

printClassReport(classRoom)