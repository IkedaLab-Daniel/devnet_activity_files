print("=" * 50)
print("           PYTHON LOOPS PRACTICE")
print("=" * 50)

# =============================================================================
# FOR LOOPS - BASIC EXAMPLES
# =============================================================================
print("\n1. BASIC FOR LOOPS")
print("-" * 20)

# Loop through a range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

print("\nCounting from 0 to 4:")
for i in range(5):
    print(f"Number: {i}")

print("\nCounting by 2s:")
for i in range(0, 11, 2):
    print(f"Even number: {i}")

print("\nCountdown:")
for i in range(10, 0, -1):
    print(f"Countdown: {i}")
print("Blast off! 🚀")

# =============================================================================
# FOR LOOPS WITH COLLECTIONS
# =============================================================================
print("\n2. FOR LOOPS WITH COLLECTIONS")
print("-" * 33)

# Loop through a list
fruits = ["apple", "banana", "cherry", "date"]
print("Fruits in the basket:")
for fruit in fruits:
    print(f"- {fruit}")

# Loop through a string
word = "Python"
print(f"\nLetters in '{word}':")
for letter in word:
    print(f"Letter: {letter}")

# Loop through a tuple
coordinates = (10, 20, 30)
print(f"\nCoordinates: {coordinates}")
for coord in coordinates:
    print(f"Value: {coord}")

# Loop through a set
unique_numbers = {1, 5, 3, 9, 2}
print(f"\nUnique numbers: {unique_numbers}")
for num in unique_numbers:
    print(f"Number: {num}")

# =============================================================================
# ENUMERATE AND ZIP
# =============================================================================
print("\n3. ENUMERATE AND ZIP")
print("-" * 23)

# Using enumerate to get index and value
colors = ["red", "green", "blue"]
print("Colors with indices:")
for index, color in enumerate(colors):
    print(f"{index}: {color}")

print("\nStarting enumerate from 1:")
for index, color in enumerate(colors, 1):
    print(f"{index}. {color}")

# Using zip to combine lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

print("\nPeople information:")
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# =============================================================================
# WHILE LOOPS - BASIC EXAMPLES
# =============================================================================
print("\n4. BASIC WHILE LOOPS")
print("-" * 22)

# Simple counter
count = 1
print("Counting with while loop:")
while count <= 5:
    print(f"Count: {count}")
    count += 1

# User input simulation (normally would use input())
attempts = 0
max_attempts = 3
correct_password = "secret"

print(f"\nPassword attempts (max {max_attempts}):")
while attempts < max_attempts:
    # Simulate user input
    passwords = ["wrong1", "wrong2", "secret"]  # Simulated inputs
    user_password = passwords[attempts] if attempts < len(passwords) else "wrong"
    
    attempts += 1
    print(f"Attempt {attempts}: Trying password '{user_password}'")
    
    if user_password == correct_password:
        print("Access granted!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password. {remaining} attempts remaining.")
        else:
            print("Too many failed attempts. Account locked.")

# =============================================================================
# BREAK AND CONTINUE
# =============================================================================
print("\n5. BREAK AND CONTINUE")
print("-" * 25)

# Using break to exit loop early
print("Finding first even number:")
numbers = [1, 3, 7, 8, 9, 10, 11]
for num in numbers:
    print(f"Checking {num}")
    if num % 2 == 0:
        print(f"Found first even number: {num}")
        break
    print(f"{num} is odd, continuing...")

# Using continue to skip iterations
print("\nPrinting only even numbers:")
for num in range(1, 11):
    if num % 2 != 0:
        continue  # Skip odd numbers
    print(f"Even number: {num}")

# Real-world example with continue
print("\nProcessing valid scores only:")
scores = [85, -5, 92, 150, 78, 88]  # Some invalid scores
for score in scores:
    if score < 0 or score > 100:
        print(f"Invalid score {score} - skipping")
        continue
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"
    
    print(f"Score {score} -> Grade {grade}")

# =============================================================================
# NESTED LOOPS
# =============================================================================
print("\n6. NESTED LOOPS")
print("-" * 17)

# Multiplication table
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()  # Empty line after each row

# Pattern printing
print("Number pyramid:")
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # New line after each row

# Grid processing
print("\nProcessing a 3x3 grid:")
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row_index, row in enumerate(grid):
    for col_index, value in enumerate(row):
        print(f"Position ({row_index},{col_index}): {value}")

# =============================================================================
# LOOP WITH ELSE
# =============================================================================
print("\n7. LOOP WITH ELSE")
print("-" * 20)

# For loop with else (executes if loop completes normally)
print("Searching for number 7:")
numbers = [1, 3, 5, 9, 7, 11]
for num in numbers:
    print(f"Checking {num}")
    if num == 7:
        print("Found 7!")
        break   # > if break did not trigger => Execute else block
else:
    print("Number 7 not found in the list")

# While loop with else
print("\nTrying to find even number:")
numbers = [1, 3, 5, 7, 9]
index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0:
        print(f"Found even number: {numbers[index]}")
        break
    index += 1
else:
    print("No even numbers found")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n8. PRACTICAL EXAMPLES")
print("-" * 25)

# Shopping cart total
shopping_cart = [
    {"item": "Apple", "price": 1.50, "quantity": 6},
    {"item": "Bread", "price": 2.00, "quantity": 2},
    {"item": "Milk", "price": 3.50, "quantity": 1},
    {"item": "Eggs", "price": 2.50, "quantity": 2}
]

print("Shopping Cart:")
print("-" * 40)
total = 0
for item in shopping_cart:
    item_total = item["price"] * item["quantity"]
    total += item_total
    print(f"{item['item']:<10} ${item['price']:.2f} x {item['quantity']} = ${item_total:.2f}")

print("-" * 40)
print(f"Total: ${total:.2f}")

# Grade statistics
print("\nGrade Statistics:")
grades = [85, 92, 78, 90, 88, 76, 94, 82, 89, 91]
total_grades = len(grades)
sum_grades = 0
highest = grades[0]
lowest = grades[0]

for grade in grades:
    sum_grades += grade
    if grade > highest:
        highest = grade
    if grade < lowest:
        lowest = grade

average = sum_grades / total_grades

print(f"Number of grades: {total_grades}")
print(f"Highest grade: {highest}")
print(f"Lowest grade: {lowest}")
print(f"Average grade: {average:.2f}")

# Counting grades by letter
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for grade in grades:
    if grade >= 90:
        grade_counts["A"] += 1
    elif grade >= 80:
        grade_counts["B"] += 1
    elif grade >= 70:
        grade_counts["C"] += 1
    elif grade >= 60:
        grade_counts["D"] += 1
    else:
        grade_counts["F"] += 1

print("\nGrade Distribution:")
for letter_grade, count in grade_counts.items():
    print(f"Grade {letter_grade}: {count} students")

# =============================================================================
# LIST COMPREHENSIONS (BONUS)
# =============================================================================
print("\n9. LIST COMPREHENSIONS (BONUS)")
print("-" * 32)

# Traditional loop
squares_traditional = []
for x in range(1, 6):
    squares_traditional.append(x ** 2)
print(f"Squares (traditional): {squares_traditional}")

# List comprehension
squares_comprehension = [x ** 2 for x in range(1, 6)]
print(f"Squares (comprehension): {squares_comprehension}")

# With condition
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# String processing
words = ["hello", "world", "python", "programming"]
uppercase_words = [word.upper() for word in words]
print(f"Uppercase words: {uppercase_words}")

# Filtering
numbers = [1, 5, 3, 8, 2, 9, 4, 7, 6]
large_numbers = [num for num in numbers if num > 5]
print(f"Numbers > 5: {large_numbers}")

# =============================================================================
# PERFORMANCE TIPS
# =============================================================================
print("\n10. PERFORMANCE TIPS")
print("-" * 22)

import time

# Timing different approaches
numbers = list(range(100000))

# Method 1: Traditional loop
start_time = time.time()
result1 = []
for num in numbers:
    if num % 2 == 0:
        result1.append(num * 2)
end_time = time.time()
traditional_time = end_time - start_time

# Method 2: List comprehension
start_time = time.time()
result2 = [num * 2 for num in numbers if num % 2 == 0]
end_time = time.time()
comprehension_time = end_time - start_time

print(f"Traditional loop time: {traditional_time:.4f} seconds")
print(f"List comprehension time: {comprehension_time:.4f} seconds")
print(f"List comprehension is {traditional_time/comprehension_time:.2f}x faster")

# Memory tip: Use generators for large datasets
def large_numbers():
    for i in range(1000000):
        yield i * i

print(f"\nGenerator created (memory efficient)")
print(f"First 5 squares: {[next(large_numbers()) for _ in range(5)]}")

print("\n" + "=" * 50)
print("         END OF LOOPS PRACTICE")
print("=" * 50)