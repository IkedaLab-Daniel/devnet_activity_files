import random
import utilities
import os # > will only be use for deleting dead players

def title():
    print("""
    |==================================|
            Welcome to PyCrawler!
    |==================================|
          """)
    

def game_menu():
    print(""" 
    |=============== Menu =============|
    |      1     |        Explore      |
    |      2     |      View Status    |
    ------------------------------------
    |  enter "quit" to save and exit   |
    ====================================
""")

def login(username):
    try:
        with open(f'player_{username}.txt', 'x') as file:
            print(f""" {username} not found, registering... """)
            print(f"Success! Welcome Player: {username}.")
            game(username, True)
    except:
        print(f"{username} exists. Logging in...")
        print(f"Welcome Player: {username}")
        game(username, False)

def game(username, new):
    while True:
        # > Since bago yung user, pa-select natin siya ng class
        if (new):
            with open(f'player_{username}.txt', 'w') as file:
                while True:     # > Validation loop
                    print("|========== Classes ============|\n")
                    for index, char_class in enumerate(utilities.character_classes, 1):
                            print(f"           {index}. {char_class}")
                    print("\n|========= (Select 1-5) ===========|\n")


                    character_class_choice = input("Select a class above [0-5]: ")

                    if character_class_choice == '1':
                        # ? Warrior
                        file.write("100 50 80")
                        print("You Selected Warrior")
                        new = False
                        break
                    elif character_class_choice == '2':
                        # ? Mage
                        file.write("100 65 60")
                        print("You Selected Mage")
                        new = False
                        break
                    elif character_class_choice == '3':
                        # ? Assasin
                        file.write("100 80 30")
                        print("You Selected Assasic")
                        new = False
                        break
                    elif character_class_choice == '4':
                        # ? Shooter
                        file.write("150 30 60")
                        print("You Selected Shooter")
                        new = False
                        break
                    elif character_class_choice == '5':
                        # ? Healer
                        file.write("200 10 100")
                        print("You Selected Healer")
                        new = False
                        break
                    else:
                        print("Invalid input")

        #> display stas after login
        show_stats(username)
        #> display menu
        game_menu()
        #> select on menu
        action = input("Enter: ")
        if action == 'quit':
            print(f"""
            |===================== Loggin out ================|
            |     Please don't forget your username T_T       |
                         > Username: "{username}"
            ---------------------------------------------------
            |                       Bye!                      |
            ===================================================
                  """)
            break
        elif action == '1':
            explore_result = explore(username)
            if explore_result == "player_died":
                break
        elif action == '2':
            # ! No need to show action again since always show siya every iterit
            pass
        else:
            print("       XXX Invalid Input XXX")
    
def show_stats(username):
    try:
        with open(f'player_{username}.txt', 'r') as file:
            stat_label = ["HP", "Attack", "Defence"]
            stat = file.read()

            print("\n     === Your Stats ===")
            for index, stat in enumerate(stat.split()):
                print(f"        {stat_label[index]}: {stat}")
            print("     ==================")
    except: 
        print("Err")

def explore(username):
    event = random.randint(1, 10)
    if event >= 6 and event <= 10:
        utilities.treasure(username)
    elif event >= 3 and event < 6:
        event_result = utilities.monstah(username)
        if event_result == 'dead':
            os.remove(f"player_{username}.txt")
            return 'player_died' # > para alam ni game(), then break na yung loop
    else:
        utilities.nothing() 


def menu():
    print("Start!")
    username = input("Enter Username: ")
    login(username)

def main():
    title()
    menu()

main()