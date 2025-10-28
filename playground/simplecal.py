def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x, y):
    return x % y

def loop_prompt():
    while True:

        num1 = int(input("\n\nNUM 1: "))
        num2 = int(input("NUM 2: "))
        operation = int(input(""" 
            Operations:
            1 - Add
            2 - Substract
            3 - Multiply
            4 - Divide
            5 - Modulo
                            
        My operation:
        """))

        if operation == 1:
            print(f"Result: {num1} + {num2} = ", add(num1, num2))
        elif operation == 2:
            print(f"Result: {num1} - {num2} = ", substract(num1, num2))
        elif operation == 3:
            print(f"Result: {num1} * {num2} = ", multiply(num1, num2))
        elif operation == 4:
            print(f"Result: {num1} / {num2} = ", divide(num1, num2))
        elif operation == 5:
            print(f"Result: {num1} % {num2} = ", substract(num1, num2))
        else:
            print("Invalid operator number")
        
        prompt = int(input("Continue? [1 - Yes, 2 - No]: "))

        if prompt == 2:
            break
    
if __name__ == "__main__":
    print("THIS IS PRINT ON MODULE")