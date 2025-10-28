def menu():
    print(""" 
    1. View all todo
    2. Add to do
    3. Edit to do
    4. Delete to do
""")
    
def decision():
    while True:
        choice = input("Select: ")
        if choice == '1':
            viewToDo()
        elif choice == '2':
            addToDo()
        elif choice == '3':
            editToDo()
        elif choice == 'q':
            break
        else:
            print("Invalid input")

def file_exists_create():
    try:
        with open('todo.txt', 'x') as file:
            print("Creating todo.txt...")
            pass
    except:
        print('To do list text file already exist. Ready to continue...')
        pass

def viewToDo():
    file_exists_create()
    with open('todo.txt', 'r') as file:
        file_read = file.readlines()
        if file_read == "":
            print("No to do yet")
        else:
            for index, todo in enumerate(file_read, 1):
                print(f"{index}. {todo[0:len(todo) - 1]}")

def addToDo():
    file_exists_create()
    with open('todo.txt', 'a') as file:
        toAdd = input("Write task to add: ")
        try:
            file.write(f"{toAdd}\n")
            print("Success")
        except:
            print("Add failed")

def editToDo():
    file_exists_create()
    with open('todo.txt', 'r') as file:
        file_read = file.readlines()
        old_list = []
        for line in file_read:
            old_list.append(line[0:len(line) - 1])
        for index, line in enumerate(old_list, 1):
            print(f"{index}. {line}")
        
        position_to_edit = int(input("Select position to Edit: "))
        updated_line = input("Edit: ")

    with open('todo.txt', 'w') as file:
        old_list[position_to_edit - 1] = updated_line
        for line in old_list:
            file.write(f"{line}\n")
        print("Selection has been edited")



def main():
    menu()
    decision()


main()