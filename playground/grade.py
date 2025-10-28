while True:

    name = input("\n\nEnter your name: ")
    section = input("Enter your section: ")
    grade = float(input("Enter your grade: "))

    if (grade >= 95 and grade <=100):
        print(f"""
        -------------------------------------------------
              {name} from {section}
              You are eligable for Summa Cum Laude
        -------------------------------------------------
              """)
    elif (grade >= 91 and grade <=94):
        print(f"""
        -------------------------------------------------
              {name} from {section}
              You are eligable for Magna Cum Laude
        -------------------------------------------------
              """)
    elif (grade >= 89 and grade <=91):
        print(f"""
        -------------------------------------------------
              {name} from {section}
              You are eligable for Cum Laude
        -------------------------------------------------
              """)
    elif (grade >= 75 and grade <= 88):
        print(f"""
        -------------------------------------------------
              {name} from {section}
              You Passed!
        -------------------------------------------------
              """)
    elif (grade > 0 and grade <= 75):
        print("\nYou failed!")
    else:
        print("\nInvalid input")

    prompt = input("Continue [1 Yes, 2 No]: ")

    if prompt == "2":
        break