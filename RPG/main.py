import utilities

def title():
    print("Welcome to my game")

def login(username):
    try:
        with open(f'player_{username}.txt', 'x') as file:
            print(f""" {username} not found, registering... """)
            print(f"Success! Welcome {username}.")
            game(username, True)
    except:
        print(f"{username} exists. Logging in...")
        print(f"Welcome {username}")

def game(username, new):
    # > Since bago yung user, pa-select natin siya ng class
    if (new):
        with open(f'player_{username}.txt', 'w') as file:
            for index, char_class in enumerate(utilities.character_classes, 1):
                    print(f"{index}. {char_class}")

            character_class_choice = input("Select a class above [0-5]: ")

            if character_class_choice == '1':
                # ? Warrior
                file.write("100 50 80")
                print("You Selected Warrior")
            elif character_class_choice == '2':
                # ? Mage
                file.write("100 65 60")
                print("You Selected Mage")
            elif character_class_choice == '3':
                # ? Assasin
                file.write("100 80 30")
                print("You Selected Assasic")

            elif character_class_choice == '4':
                # ? Shooter
                file.write("You 150 30 60")
                print("You Selected Shooter")
            elif character_class_choice == '5':
                # ? Healer
                file.write("You 200 10 100")
                print("Selected Healer")

            else:
                print("Invalid input")

        show_stats(username)
    
def show_stats(username):
    try:
        with open(f'player_{username}.txt', 'r') as file:
            stat_label = ["HP", "Attack", "Defence"]
            stat = file.read()

            print("=== Your Stats ===")
            for index, stat in enumerate(stat.split()):
                print(f"   {stat_label[index]}: {stat}")
            print("==================")
    except: 
        print("Err")


def menu():
    print("Start!")
    username = input("Enter Username: ")
    login(username)

def main():
    title()
    menu()

main()