print("=" * 50)
print("          PYTHON FUNCTIONS PRACTICE")
print("=" * 50)

# =============================================================================
# BASIC FUNCTION DEFINITION AND CALLING
# =============================================================================
print("\n1. BASIC FUNCTION DEFINITION AND CALLING")
print("-" * 44)

# Simple function with no parameters
def greet():
    """A simple greeting function"""
    print("Hello, World!")

# Calling the function
print("Calling greet():")
greet()

# Function with parameters
def greet_person(name):
    """Greet a specific person"""
    print(f"Hello, {name}!")

print("\nCalling greet_person():")
greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def introduce(name, age, city):
    """Introduce a person with their details"""
    print(f"Hi, I'm {name}. I'm {age} years old and I live in {city}.")

print("\nCalling introduce():")
introduce("Charlie", 25, "New York")

# =============================================================================
# RETURN VALUES
# =============================================================================
print("\n2. FUNCTIONS WITH RETURN VALUES")
print("-" * 34)

# Function that returns a value
def add_numbers(a, b):
    """Add two numbers and return the result"""
    result = a + b
    return result

# Using the returned value
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")

# Function with multiple return values
def get_name_and_age():
    """Return multiple values"""
    return "Alice", 30

name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")

# Function returning different types
def calculate_circle(radius):
    """Calculate circle area and circumference"""
    import math
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

area, circumference = calculate_circle(5)
print(f"Circle (radius=5): Area={area:.2f}, Circumference={circumference:.2f}")

# =============================================================================
# DEFAULT PARAMETERS
# =============================================================================
print("\n3. DEFAULT PARAMETERS")
print("-" * 22)

def greet_with_title(name, title="Mr./Ms."):
    """Greet with an optional title"""
    print(f"Hello, {title} {name}!")

print("Using default title:")
greet_with_title("Smith")

print("Using custom title:")
greet_with_title("Johnson", "Dr.")

# Multiple default parameters
def create_profile(name, age=25, city="Unknown", country="USA"):
    """Create a user profile with default values"""
    return {
        "name": name,
        "age": age,
        "city": city,
        "country": country
    }

profile1 = create_profile("Alice")
profile2 = create_profile("Bob", 30, "London", "UK")

print(f"Profile 1: {profile1}")
print(f"Profile 2: {profile2}")

# =============================================================================
# KEYWORD ARGUMENTS
# =============================================================================
print("\n4. KEYWORD ARGUMENTS")
print("-" * 23)

def order_pizza(size, toppings, crust="thin", extra_cheese=False):
    """Order a pizza with specified options"""
    cheese_text = "with extra cheese" if extra_cheese else "without extra cheese"
    return f"{size.title()} {crust} crust pizza with {toppings}, {cheese_text}"

# Positional arguments
order1 = order_pizza("large", "pepperoni")
print(f"Order 1: {order1}")

# Keyword arguments
order2 = order_pizza(size="medium", toppings="mushrooms", crust="thick", extra_cheese=True)
print(f"Order 2: {order2}")

# Mixed positional and keyword arguments
order3 = order_pizza("small", "vegetables", extra_cheese=True)
print(f"Order 3: {order3}")

# =============================================================================
# *ARGS AND **KWARGS
# =============================================================================
print("\n5. *ARGS AND **KWARGS")
print("-" * 24)

# *args - variable number of positional arguments
def sum_all(*args):
    """Sum all provided numbers"""
    total = 0
    for number in args:
        total += number
    return total

print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5): {sum_all(1, 2, 3, 4, 5)}")

# **kwargs - variable number of keyword arguments
def create_user(**kwargs):
    """Create user with flexible attributes"""
    user = {}
    for key, value in kwargs.items():
        user[key] = value
    return user

user1 = create_user(name="Alice", age=30, city="NYC")
user2 = create_user(name="Bob", occupation="Engineer", hobby="Reading")

print(f"User 1: {user1}")
print(f"User 2: {user2}")

# Combining *args and **kwargs
def flexible_function(*args, **kwargs):
    """Function that accepts any arguments"""
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print("\nCalling flexible_function:")
flexible_function(1, 2, 3, name="Alice", age=30)

# =============================================================================
# LOCAL AND GLOBAL SCOPE
# =============================================================================
print("\n6. VARIABLE SCOPE")
print("-" * 18)

# Global variable
global_counter = 0

def increment_global():
    """Increment the global counter"""
    global global_counter
    global_counter += 1
    print(f"Global counter: {global_counter}")

def local_example():
    """Example of local variable"""
    local_var = "I'm local"
    print(f"Local variable: {local_var}")

print("Before increment:")
print(f"Global counter: {global_counter}")

increment_global()
increment_global()
local_example()

# Variable shadowing
name = "Global Alice"

def shadowing_example():
    name = "Local Bob"  # This shadows the global variable
    print(f"Inside function: {name}")

print(f"Outside function: {name}")
shadowing_example()
print(f"After function: {name}")

# =============================================================================
# LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# =============================================================================
print("\n7. LAMBDA FUNCTIONS")
print("-" * 20)

# Basic lambda
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"add(3, 7) = {add(3, 7)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared_numbers}")

# Lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Lambda with sort
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
students_by_grade = sorted(students, key=lambda student: student[1])
print(f"Students by grade: {students_by_grade}")

# =============================================================================
# RECURSIVE FUNCTIONS
# =============================================================================
print("\n8. RECURSIVE FUNCTIONS")
print("-" * 23)

def factorial(n):
    """Calculate factorial using recursion"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"factorial(5) = {factorial(5)}")
print(f"factorial(0) = {factorial(0)}")

def fibonacci(n):
    """Calculate Fibonacci number using recursion"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence:")
for i in range(8):
    print(f"fib({i}) = {fibonacci(i)}")

# =============================================================================
# HIGHER-ORDER FUNCTIONS
# =============================================================================
print("\n9. HIGHER-ORDER FUNCTIONS")
print("-" * 28)

def apply_operation(numbers, operation):
    """Apply an operation to each number in the list"""
    return [operation(num) for num in numbers]

def double(x):
    return x * 2

def triple(x):
    return x * 3

numbers = [1, 2, 3, 4, 5]
doubled = apply_operation(numbers, double)
tripled = apply_operation(numbers, triple)

print(f"Original: {numbers}")
print(f"Doubled: {doubled}")
print(f"Tripled: {tripled}")

# Function that returns a function
def create_multiplier(factor):
    """Create a function that multiplies by a factor"""
    def multiplier(x):
        return x * factor
    return multiplier

multiply_by_3 = create_multiplier(3)
multiply_by_5 = create_multiplier(5)

print(f"multiply_by_3(4) = {multiply_by_3(4)}")
print(f"multiply_by_5(6) = {multiply_by_5(6)}")

# =============================================================================
# DECORATORS (BONUS)
# =============================================================================
print("\n10. DECORATORS (BONUS)")
print("-" * 25)

def timer_decorator(func):
    """Decorator to time function execution"""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    """A function that takes some time"""
    import time
    time.sleep(0.1)  # Simulate work
    return "Done!"

result = slow_function()
print(f"Result: {result}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n11. PRACTICAL EXAMPLES")
print("-" * 26)

# Calculator functions
def calculator(operation, a, b):
    """Simple calculator function"""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

print("Calculator examples:")
print(f"Add: {calculator('add', 10, 5)}")
print(f"Divide: {calculator('divide', 10, 3)}")
print(f"Divide by zero: {calculator('divide', 10, 0)}")

# Password validator
def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        return False, "Password too short (minimum 8 characters)"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    if not (has_upper and has_lower and has_digit):
        return False, "Password must contain uppercase, lowercase, and digit"
    
    return True, "Password is valid"

passwords = ["weak", "StrongPass123", "NoDigits", "nocaps123"]
for pwd in passwords:
    is_valid, message = validate_password(pwd)
    print(f"'{pwd}': {message}")

# Grade calculator
def calculate_grade(scores):
    """Calculate letter grade from scores"""
    if not scores:
        return "No scores provided"
    
    average = sum(scores) / len(scores)
    
    if average >= 90:
        return f"A (Average: {average:.1f})"
    elif average >= 80:
        return f"B (Average: {average:.1f})"
    elif average >= 70:
        return f"C (Average: {average:.1f})"
    elif average >= 60:
        return f"D (Average: {average:.1f})"
    else:
        return f"F (Average: {average:.1f})"

student_scores = [85, 90, 78, 92, 88]
grade = calculate_grade(student_scores)
print(f"Student grade: {grade}")

# =============================================================================
# FUNCTION DOCUMENTATION
# =============================================================================
print("\n12. FUNCTION DOCUMENTATION")
print("-" * 30)

def complex_calculation(x, y, operation="multiply", precision=2):
    """
    Perform complex calculations on two numbers.
    
    Args:
        x (float): First number
        y (float): Second number
        operation (str): Operation to perform ('multiply', 'divide', 'power')
        precision (int): Decimal places for result
    
    Returns:
        float: Result of the calculation
        
    Raises:
        ValueError: If operation is not supported
        ZeroDivisionError: If dividing by zero
    """
    if operation == "multiply":
        result = x * y
    elif operation == "divide":
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = x / y
    elif operation == "power":
        result = x ** y
    else:
        raise ValueError(f"Unsupported operation: {operation}")
    
    return round(result, precision)

# Using the documented function
print("Complex calculation examples:")
print(f"Multiply: {complex_calculation(3.14159, 2)}")
print(f"Power: {complex_calculation(2, 8, 'power')}")

# Access function documentation
print(f"\nFunction documentation:\n{complex_calculation.__doc__}")

print("\n" + "=" * 50)
print("         END OF FUNCTIONS PRACTICE")
print("=" * 50)