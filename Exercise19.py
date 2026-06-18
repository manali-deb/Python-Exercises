# Exercise 19
"""
To-Do List Manager

Build a to-do list with these functions:

- `addTask(todoList, task, priority)` — priority is `"high"`, `"medium"`, or `"low"`. Returns `"Task added"` or `"Invalid priority"`
- `completeTask(todoList, task)` — marks the task as done, returns `"Done"` or `"Task not found"`
- `deleteTask(todoList, task)` — removes a task entirely
- `getPending(todoList)` — returns a list of only the tasks not yet completed
- `printList(todoList)` — prints all tasks sorted by priority (high first, then medium, then low):

```
TO-DO LIST
====================
[HIGH]   ✗ Study for exam
[HIGH]   ✓ Read chapter 5
[MEDIUM] ✗ Call dentist
[LOW]    ✗ Clean desk
====================
Pending: 3  Completed: 1
```

Write a script that adds 6 tasks with different priorities, completes 2, deletes 1, and prints the list.
"""

def addTask(todoList, task, priority):
    priorities = ["high", "medium", "low"]

    if priority not in priorities:
        return "Invalid priority"
    
    todoList.append({
        "task": task,
        "priority": priority,
        "completed": False
    })

    return "Task added"

def completeTask(todoList, task):
    for item in todoList:
        if item["task"] == task:
            item["completed"] = True
            return "Done"
        
    return "Task not found"

def deleteTask(todoList, task):
    for item in todoList:
        if item["task"] == task:
            todoList.remove(item)
            return "Deleted"
        
    return "Task not found"

def getPending(todoList):
    pending = []

    for item in todoList:
        if not item["completed"]:
            pending.append(item)

    return pending

def printList(todoList):
    priority_order = {
        "high": 1,
        "medium": 2,
        "low": 3
    }

    sorted_tasks = sorted(
        todoList,
        key=lambda task: priority_order[task["priority"]]
    )

    completed_count = 0

    print("TO-DO LIST")
    print("====================")

    for item in sorted_tasks:
        status = "✓" if item["completed"] else "✗"

        if item["priority"] == "high":
            priority = "[HIGH]   "
        elif item["priority"] == "medium":
            priority = "[MEDIUM] "
        else:
            priority = "[LOW]    "
        
        print(f"{priority} {status} {item['task']}")

        if item["completed"]:
            completed_count += 1
    
    pending_count = len(todoList) - completed_count

    print("====================")
    print(f"Pending: {pending_count}  Completed: {completed_count}")

# test
todoList = []
print(addTask(todoList, "Study Klarna", "high"))
print(addTask(todoList, "Go grocery shopping", "high"))
print(addTask(todoList, "Go to the doctor", "medium"))
print(addTask(todoList, "Clean apartment", "medium"))
print(addTask(todoList, "Finish my book", "low"))
print(addTask(todoList, "Hang out with friends", "low"))

print(completeTask(todoList, "Go grocery shopping"))
print(completeTask(todoList, "Clean apartment"))

print(deleteTask(todoList, "Finish my book"))

print()
printList(todoList)