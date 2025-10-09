character_classes = ['Warrrior', 'Mage', 'Assasin', 'Shooter', 'Supporter']

#> Save function to save changes after events
def save(username, new_hp, attack, defence):
    try:
        with open(f'player_{username}.txt', 'w') as file:
            file.write(f"{new_hp} {attack} {defence}")
            print("New stat save")
    except:
        print("Save error")


# > Events
def monstah(username):
    with open(f'player_{username}.txt', 'r') as file:
        read_file = file.read().split()
        hp = read_file[0]
        attack = read_file[1]
        defence = read_file[2]

    newHP = float(hp) - (10 * (int(defence) / 200)) 
    reduced = (10 * (int(defence) / 200)) 
    print(f""" 
        |===================== Event ===================|
                   You encountered a huge bear!
                        HP:   -{reduced}

                            New Stats
                        HP:    {newHP}
                        Attack: {attack}
                        Defence: {defence}
        |===============================================|
    """)
    save(username, newHP, attack, defence)