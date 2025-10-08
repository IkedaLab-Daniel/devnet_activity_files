# Sample math utilities module
"""
math_utils.py - A collection of mathematical utility functions
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """Calculate base to the power of exponent"""
    return base ** exponent

def factorial(n):
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Module-level variable
PI = 3.14159265359

# Module-level constant
GOLDEN_RATIO = 1.618033988749

def circle_area(radius):
    """Calculate area of a circle"""
    return PI * radius ** 2

def circle_circumference(radius):
    """Calculate circumference of a circle"""
    return 2 * PI * radius

print("Factorial of 5: ", factorial(5))