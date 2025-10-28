def menu():
    print(""" 
    |------------------------------|
    |    1. View to-do list        |
    |    2. Add to-do list item    |
    |    3. Edit to-do list item   |
    |    4. Delete to-do list item |
    |------------------------------|
""")

def add(item):
    toDos.append(item)
    print(f"""
    |------------------------------|
    |       {item} was added!      |
    |------------------------------|
    """)

def display():
    if not toDos:
        print("No To Do yet")
    else:
        print("All my to dos:")
        for i, do in enumerate(toDos, start=1):
            print(f"{i}. {do}")

def edit(newDescription, position):
    toDos[position - 1] = newDescription
    print("Editted")

def delete(position):
    toDos.pop(position - 1)

toDos = []
while True:
    menu()
    choice = int(input("Choice: "))

    if choice == 1:
        display()

    elif choice == 2:
        newItem = input("New to do: ")
        add(newItem)
        print(">>>> Updated ToDos <<<<<")
        display()

    elif choice == 3:
        position = int(input("What to edit?"))
        new = input("New description: ")
        edit(new, position)
        print("Updated To Dos:")
        display()
    
    elif choice == 4:
        position = int(input("What to delete? "))
        delete(position)
        print("Updated To Do")
        display()
