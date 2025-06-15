print("=" * 50)
print("         PYTHON DATA TYPES PRACTICE")
print("=" * 50)

# =============================================================================
# PRIMITIVE DATA TYPES
# =============================================================================
print("\n1. PRIMITIVE DATA TYPES")
print("-" * 30)

# =============================================================================
# INTEGER (int)
# =============================================================================
print("\n📊 INTEGER (int)")
print("-" * 15)

# Integer examples
age = 25
negative_num = -10
large_num = 1000000
zero = 0

print(f"Age: {age} (type: {type(age)})")
print(f"Negative: {negative_num}")
print(f"Large number: {large_num}")
print(f"Zero: {zero}")

# Integer operations
print(f"Addition: 10 + 5 = {10 + 5}")
print(f"Subtraction: 10 - 3 = {10 - 3}")
print(f"Multiplication: 4 * 6 = {4 * 6}")
print(f"Division: 15 / 3 = {15 / 3}")
print(f"Floor division: 17 // 5 = {17 // 5}")
print(f"Modulus: 17 % 5 = {17 % 5}")
print(f"Exponent: 2 ** 3 = {2 ** 3}")

# =============================================================================
# FLOAT (float)
# =============================================================================
print("\n🔢 FLOAT (float)")
print("-" * 15)

# Float examples
pi = 3.14159
price = 19.99
temperature = -5.5
scientific = 1.5e6  # Scientific notation

print(f"Pi: {pi} (type: {type(pi)})")
print(f"Price: ${price}")
print(f"Temperature: {temperature}°C")
print(f"Scientific notation: {scientific}")

# Float operations
print(f"Float division: 7 / 2 = {7 / 2}")
print(f"Rounded: {round(pi, 2)}")
print(f"Absolute value: {abs(temperature)}")

# =============================================================================
# STRING (str)
# =============================================================================
print("\n📝 STRING (str)")
print("-" * 15)

# String examples
name = "Alice"
message = 'Hello, World!'
multiline = """This is a
multiline string"""
empty_string = ""

print(f"Name: {name} (type: {type(name)})")
print(f"Message: {message}")
print(f"Multiline: {(multiline)}")
print(f"Empty string: '{empty_string}' (length: {len(empty_string)})")

# String operations
text = "Python Programming"
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Length: {len(text)}")
print(f"Replace: {text.replace('Python', 'Java')}")
print(f"Split: {text.split(' ')}")
print(f"Starts with 'Python': {text.startswith('Python')}")

# String formatting
first_name = "John"
last_name = "Doe"
age = 30
print(f"Formatted string: {first_name} {last_name} is {age} years old")

# =============================================================================
# BOOLEAN (bool)
# =============================================================================
print("\n✅ BOOLEAN (bool)")
print("-" * 17)

# Boolean examples
is_active = True
is_complete = False
is_valid = bool(1)  # Converting to boolean
is_empty = bool("")  # Converting empty string

print(f"Active: {is_active} (type: {type(is_active)})")
print(f"Complete: {is_complete}")
print(f"Valid (from 1): {is_valid}")
print(f"Empty (from ''): {is_empty}")

# Boolean operations
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# =============================================================================
# COLLECTION DATA TYPES
# =============================================================================
print("\n2. COLLECTION DATA TYPES")
print("-" * 32)

# =============================================================================
# LIST (Mutable, Ordered)
# =============================================================================
print("\n📋 LIST (Mutable, Ordered)")
print("-" * 25)

# List examples
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
nested_list = [[1, 2], [3, 4], [5, 6]]
empty_list = []

print(f"Numbers: {numbers} (type: {type(numbers)})")
print(f"Mixed types: {mixed_list}")
print(f"Nested list: {nested_list}")
print(f"Empty list: {empty_list}")

# List operations
fruits = ["apple", "banana", "cherry"]
print(f"Original fruits: {fruits}")

# Adding elements
fruits.append("date")
print(f"After append: {fruits}")

fruits.insert(1, "blueberry")
print(f"After insert: {fruits}")

# Removing elements
fruits.remove("banana")
print(f"After remove: {fruits}")

popped = fruits.pop()
print(f"After pop: {fruits}, popped item: {popped}")

# Accessing elements
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}")

# =============================================================================
# TUPLE (Immutable, Ordered)
# =============================================================================
print("\n📦 TUPLE (Immutable, Ordered)")
print("-" * 28)

# Tuple examples
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (42,)  # Note the comma for single item
mixed_tuple = (1, "hello", 3.14)

print(f"Coordinates: {coordinates} (type: {type(coordinates)})")
print(f"Colors: {colors}")
print(f"Single item: {single_item}")
print(f"Mixed tuple: {mixed_tuple}")

# Tuple operations
print(f"First coordinate: {coordinates[0]}")
print(f"Second coordinate: {coordinates[1]}")
print(f"Length: {len(colors)}")
print(f"Count of 'red': {colors.count('red')}")
print(f"Index of 'green': {colors.index('green')}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked coordinates: x={x}, y={y}")

# =============================================================================
# SET (Mutable, Unordered, Unique)
# =============================================================================
print("\n🔢 SET (Mutable, Unordered, Unique)")
print("-" * 35)

# Set examples
unique_numbers = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14}
from_list = set([1, 2, 2, 3, 3, 4])  # Duplicates removed
empty_set = set()  # Note: {} creates a dict, not set

print(f"Unique numbers: {unique_numbers} (type: {type(unique_numbers)})")
print(f"Mixed set: {mixed_set}")
print(f"From list (duplicates removed): {from_list}")
print(f"Empty set: {empty_set}")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

# Adding and removing from set
letters = {"a", "b", "c"}
letters.add("d")
print(f"After add: {letters}")

letters.remove("a")
print(f"After remove: {letters}")

# =============================================================================
# TYPE CONVERSION
# =============================================================================
print("\n3. TYPE CONVERSION")
print("-" * 20)

# Converting between types
num_str = "123"
float_str = "45.67"
bool_val = True

print(f"String to int: '{num_str}' -> {int(num_str)}")
print(f"String to float: '{float_str}' -> {float(float_str)}")
print(f"Int to string: 42 -> '{str(42)}'")
print(f"Bool to int: {bool_val} -> {int(bool_val)}")
print(f"List to tuple: [1,2,3] -> {tuple([1, 2, 3])}")
print(f"Tuple to list: (1,2,3) -> {list((1, 2, 3))}")
print(f"List to set: [1,2,2,3] -> {set([1, 2, 2, 3])}")

# =============================================================================
# CHECKING DATA TYPES
# =============================================================================
print("\n4. CHECKING DATA TYPES")
print("-" * 25)

sample_data = [42, 3.14, "hello", True, [1, 2, 3], (4, 5, 6), {7, 8, 9}]

for item in sample_data:
    print(f"{item} is of type {type(item).__name__}")
    
    # Using isinstance()
    if isinstance(item, int):
        print(f"  -> {item} is an integer")
    elif isinstance(item, float):
        print(f"  -> {item} is a float")
    elif isinstance(item, str):
        print(f"  -> {item} is a string")
    elif isinstance(item, bool):
        print(f"  -> {item} is a boolean")
    elif isinstance(item, list):
        print(f"  -> {item} is a list")
    elif isinstance(item, tuple):
        print(f"  -> {item} is a tuple")
    elif isinstance(item, set):
        print(f"  -> {item} is a set")

print("\n" + "=" * 50)
print("         END OF DATA TYPES PRACTICE")
print("=" * 50)