import random as pogiNiSir

welcome_message = """
----------------------------
|      Welcome to Random    |
|       guessing game!      |
----------------------------

----------------------------
|      Guess the number     |
|        from 1-10          |
----------------------------
"""

win_message = """
----------------------------
|           You Won!        |
|       the winning number  |
|            is {winningNumber}     |
----------------------------
"""

range_message = """
----------------------------
|        1 - 10 only        |
----------------------------
"""

lower_message = """
----------------------------
|       {guess} is wrong!   |
|       Lower!              |
|       {attempt} remaining!    |
----------------------------
"""

higher_message = """
----------------------------
|       {guess} is wrong!   |
|       Higher!             |
----------------------------
"""

print(welcome_message)
winningNumber = pogiNiSir.randint(1, 10)
attemps = 3

while True:
    print("Lives: ", "❤️ " * attemps)
    guess = int(input(f"My guest: "))

    if (guess == winningNumber):
        print(win_message.format(winningNumber=winningNumber))

    elif (guess > 10 or guess < 1):
        print(range_message)

    elif (guess > winningNumber):
        print(lower_message.format(guess=guess, attempt=attemps))
        attemps -= 1

    elif (guess < winningNumber):
        print(higher_message.format(guess=guess, attempt=attemps))
        attemps -= 1

    if attemps == 0:
        print("💔 No more lives!")
        break