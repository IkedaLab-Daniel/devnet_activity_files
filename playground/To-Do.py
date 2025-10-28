def menu():
    print(""" 
    |--------- TO DO APP ------------|
    |   1 - View all to do           |
    |   2 - Add new to do            |
    |   3 - Edit a to do app         |
    |   4 - Delete a task            |
    |   5 - Clear task               |
    |   6 - Mark Complete            |
    |   7 - Add due date             |
    |   8 - View sort alphabetically |
    |   9 - Todos with deadlines     |
    |   10 - View completed tasks    |
    |--------------------------------|
    |    enter "quit"   to exit      |
    |--------------------------------|      
""")
    
def dispayToDos():
    print("\n>>>>> MY TODOs <<<<<<<\n")
    if not todo:
        print(">>> No To Dos Yet <<<")
    else:
        x = 1
        for i in todo:
            print(f"   {x}. {i}")
            x = x + 1

def addToDo(item):
    todo.append(item)
    print(f"{item} has been item")
    dispayToDos()


def edit(position, newToDo):
    todo[position - 1] = newToDo
    print(f"\n[  To do #{position} has been UPDATED!   ]")
    dispayToDos()


def delete(item):
    todo.pop(item - 1)
    print(f"\n[  To do #{item} has been DELETED!   ]")
    dispayToDos()

def clear():
    todo.clear()
    print("All To Do's are CLEARED!")
    dispayToDos()

def complete(item):
    todo[item - 1] = todo[item - 1] + " - Completed"
    print(f"To Do #{item} has been marked completed")
    dispayToDos()

def addDue(item, date, month, year):
    todo[item - 1] = todo[item - 1] + " - DUE (D:M:Y): " + date + "-" + month + "-" + year
    print(f"To Do #{item} now have a deadline")
    dispayToDos()

def viewSortAlp():
    if not todo:
        print(">>> No To Dos Yet <<<")
    else:
        sortedToDo = sorted(todo)
        print("\n>>>>> MY TODOs (Alphabetical) <<<<<<<\n")
        x = 1
        for i in sortedToDo:
            print(f"   {x}. {i}")
            x = x + 1
def viewWithDeadline():
    ice = 0
    if not todo:
        print(">>> No To Dos Yet <<<")
    else:
        print("\n   >>> Here's the ToDos with Deadlines <<<\n")
        x = 1
        for i in todo:
            if "DUE (D:M:Y):" in i:
                print(f"{x}. {i}")
                x = x + 1
                ice = ice + 1
        if ice == 0:
            print("   >>> No task has deadline yet <<<")
    

def viewCompleted():
    if not todo:
        print(">>> No To Dos Yet <<<")
    else:
        ice = 0
        print("\n   >>> Here's your COMPLETED ToDos <<<\n")
        x = 1
        for i in todo:
            if "- Completed" in i:
                print(f"{x}. {i}")
                x = x + 1
                ice = ice + 1
        if (ice == 0):
            print("   >>> No completed task yet<<<")
    

todo = []

while True:
    menu()
    choose = input("Enter choice: ")

    if choose == "1":
        dispayToDos()
    elif choose == "2":
        item = input("Enter new to Do: ")
        addToDo(item)
    elif choose == "3":
        dispayToDos()
        item = int(input("Enter number of what you want to EDIT: "))
        newToDo = input("Enter new value: ")
        edit(item, newToDo)
    elif choose == "4":
        dispayToDos()
        item = int(input("Enter number of what you want to DELETE: "))
        delete(item)
    elif choose == "5":
        surekaba = int(input("Are you sure? [1 - YES, 2 - NO]: "))
        if (surekaba == 1):
            clear()
    elif choose == "6":
        dispayToDos()
        item = int(input("While item number to mark complete?: "))
        complete(item)
    elif choose == "7":
        dispayToDos()
        item = int(input("While item number to set deadline: "))
        date = input("Enter due Day [1-31]: ")
        month = input("Enter due Month [1-12]: ")
        year = input("Enter year [####]: ")
        addDue(item, date, month, year)
    elif choose == "8":
        viewSortAlp()
    elif choose == "9":
        viewWithDeadline()
    elif choose == '10':
        viewCompleted()
    elif choose == "quit":
        break
    else:
        print("Invalid Input")

# > Note: Naubusan ng time kaya minimal validations lang :(