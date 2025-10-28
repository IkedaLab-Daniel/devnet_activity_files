print("=" * 50)
print("          PYTHON MODULES PRACTICE")
print("=" * 50)

# =============================================================================
# IMPORTING BUILT-IN MODULES
# =============================================================================
print("\n1. IMPORTING BUILT-IN MODULES")
print("-" * 32)

# Import entire module
import math
import random
import datetime

print("Using math module:")
print(f"math.pi = {math.pi}")
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.ceil(4.3) = {math.ceil(4.3)}")
print(f"math.floor(4.7) = {math.floor(4.7)}")

print("\nUsing random module:")
print(f"random.randint(1, 10) = {random.randint(1, 10)}")
print(f"random.choice(['a', 'b', 'c']) = {random.choice(['a', 'b', 'c'])}")

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

print("\nUsing datetime module:")
now = datetime.datetime.now()
print(f"Current datetime: {now}")
print(f"Current year: {now.year}")
print(f"Current month: {now.month}")

# =============================================================================
# SPECIFIC IMPORTS (FROM...IMPORT)
# =============================================================================
print("\n2. SPECIFIC IMPORTS (FROM...IMPORT)")
print("-" * 38)

# Import specific functions/classes
from math import sqrt, pow, sin, cos
from datetime import date, timedelta
from random import randint, choice

print("Using specific imports:")
print(f"sqrt(25) = {sqrt(25)}")
print(f"pow(2, 3) = {pow(2, 3)}")
print(f"sin(π/2) ≈ {sin(math.pi/2):.2f}")

print("\nDate calculations:")
today = date.today()
tomorrow = today + timedelta(days=1)
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")

print(f"\nRandom number: {randint(1, 100)}")
print(f"Random choice: {choice(['apple', 'banana', 'cherry'])}")

# =============================================================================
# IMPORT WITH ALIASES
# =============================================================================
print("\n3. IMPORT WITH ALIASES")
print("-" * 26)

# Import with alias
import datetime as dt
import math as m
from collections import Counter as cnt

print("Using aliases:")
current_time = dt.datetime.now()
print(f"Current time (using dt alias): {current_time}")

print(f"Using math alias: m.pi = {m.pi}")

# Using Counter with alias
text = "hello world"
letter_count = cnt(text)
print(f"Letter count in '{text}': {dict(letter_count)}")

# =============================================================================
# IMPORTING CUSTOM MODULES
# =============================================================================
print("\n4. IMPORTING CUSTOM MODULES")
print("-" * 31)

# Import our custom modules
try:
    import math_utils
    import string_utils
    
    print("Using math_utils module:")
    print(f"math_utils.add(5, 3) = {math_utils.add(5, 3)}")
    print(f"math_utils.multiply(4, 7) = {math_utils.multiply(4, 7)}")
    print(f"math_utils.PI = {math_utils.PI}")
    print(f"Circle area (radius=5): {math_utils.circle_area(5):.2f}")
    
    print("\nUsing string_utils module:")
    text = "hello world"
    print(f"Original: '{text}'")
    print(f"Capitalized: '{string_utils.capitalize_words(text)}'")
    print(f"Reversed: '{string_utils.reverse_string(text)}'")
    print(f"Vowel count: {string_utils.count_vowels(text)}")
    print(f"Is palindrome: {string_utils.is_palindrome('racecar')}")
    
except ImportError as e:
    print(f"Could not import custom modules: {e}")
    print("Make sure math_utils.py and string_utils.py are in the same directory")

# =============================================================================
# SPECIFIC IMPORTS FROM CUSTOM MODULES
# =============================================================================
print("\n5. SPECIFIC IMPORTS FROM CUSTOM MODULES")
print("-" * 44)

try:
    from math_utils import add, subtract, PI, factorial
    from string_utils import reverse_string, count_vowels, VOWELS
    
    print("Using specific imports from custom modules:")
    print(f"add(10, 15) = {add(10, 15)}")
    print(f"subtract(20, 8) = {subtract(20, 8)}")
    print(f"PI constant = {PI}")
    print(f"factorial(5) = {factorial(5)}")
    
    sample_text = "Python Programming"
    print(f"\nString operations on '{sample_text}':")
    print(f"Reversed: '{reverse_string(sample_text)}'")
    print(f"Vowel count: {count_vowels(sample_text)}")
    print(f"Available vowels: {VOWELS}")
    
except ImportError as e:
    print(f"Could not import from custom modules: {e}")

# =============================================================================
# COMMON BUILT-IN MODULES
# =============================================================================
print("\n6. COMMON BUILT-IN MODULES")
print("-" * 29)

# os module - Operating system interface
import os
print("OS module examples:")
print(f"Current working directory: {os.getcwd()}")
print(f"Environment variable PATH exists: {'PATH' in os.environ}")

# sys module - System-specific parameters
import sys
print(f"\nPython version: {sys.version}")
print(f"Platform: {sys.platform}")

# collections module - Specialized container datatypes
from collections import Counter, defaultdict, namedtuple

print("\nCollections module examples:")
# Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(f"Word count: {dict(word_count)}")

# defaultdict
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
print(f"Default dict: {dict(dd)}")

# namedtuple
Person = namedtuple('Person', ['name', 'age', 'city'])
person1 = Person('Alice', 30, 'New York')
print(f"Named tuple: {person1.name} is {person1.age} years old")

# json module - JSON encoder/decoder
import json
print("\nJSON module examples:")
data = {"name": "Alice", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(f"JSON string: {json_string}")

parsed_data = json.loads(json_string)
print(f"Parsed data: {parsed_data}")

# =============================================================================
# MODULE SEARCH PATH AND __NAME__
# =============================================================================
print("\n7. MODULE INFORMATION")
print("-" * 22)

print(f"Current module name: {__name__}")
print(f"Math module location: {math.__file__}")

# Module attributes
print(f"\nMath module attributes:")
math_attributes = [attr for attr in dir(math) if not attr.startswith('_')]
print(f"First 10 attributes: {math_attributes[:10]}")

# Check if running as main module
if __name__ == "__main__":
    print("\nThis script is being run directly (not imported)")
else:
    print("\nThis script has been imported as a module")

# =============================================================================
# THIRD-PARTY MODULES (EXAMPLES)
# =============================================================================
print("\n8. THIRD-PARTY MODULES (EXAMPLES)")
print("-" * 37)

print("Common third-party modules you can install:")
print("- requests: HTTP library (pip install requests)")
print("- numpy: Numerical computing (pip install numpy)")
print("- pandas: Data analysis (pip install pandas)")
print("- matplotlib: Plotting (pip install matplotlib)")
print("- pillow: Image processing (pip install pillow)")

# Example of what you could do with requests (if installed)
print("\nExample usage (if installed):")
print("import requests")
print("response = requests.get('https://api.github.com')")
print("print(response.status_code)")

# =============================================================================
# MODULE BEST PRACTICES
# =============================================================================
print("\n9. MODULE BEST PRACTICES")
print("-" * 28)

print("Import order best practices:")
print("1. Standard library imports")
print("2. Third-party library imports") 
print("3. Local application imports")
print()
print("Example:")
print("# Standard library")
print("import os")
print("import sys")
print("from datetime import datetime")
print()
print("# Third-party")
print("import requests")
print("import numpy as np")
print()
print("# Local modules")
print("from . import my_module")
print("from .utils import helper_function")

# =============================================================================
# CREATING PACKAGES
# =============================================================================
print("\n10. CREATING PACKAGES")
print("-" * 23)

print("To create a package:")
print("1. Create a directory with your package name")
print("2. Add an __init__.py file (can be empty)")
print("3. Add your module files")
print()
print("Example structure:")
print("my_package/")
print("    __init__.py")
print("    module1.py")
print("    module2.py")
print("    subpackage/")
print("        __init__.py")
print("        submodule.py")
print()
print("Usage:")
print("import my_package.module1")
print("from my_package.module2 import function")
print("from my_package.subpackage import submodule")

# =============================================================================
# RELOADING MODULES (DEVELOPMENT)
# =============================================================================
print("\n11. RELOADING MODULES (DEVELOPMENT)")
print("-" * 37)

print("In interactive development, you might need to reload modules:")
print("import importlib")
print("importlib.reload(module_name)")
print()
print("Note: This is mainly useful in interactive sessions like")
print("Jupyter notebooks or Python REPL during development.")

# =============================================================================
# PRACTICAL EXAMPLE: USING MULTIPLE MODULES
# =============================================================================
print("\n12. PRACTICAL EXAMPLE")
print("-" * 23)

def demonstrate_module_usage():
    """Demonstrate using multiple modules together"""
    import random
    from datetime import datetime, timedelta
    import json
    
    # Create sample data
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    ages = [random.randint(20, 60) for _ in range(5)]
    cities = ["New York", "London", "Tokyo", "Paris", "Sydney"]
    
    # Create people data
    people = []
    for i in range(5):
        person = {
            "name": random.choice(names),
            "age": random.choice(ages),
            "city": random.choice(cities),
            "created": (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat()
        }
        people.append(person)
    
    # Convert to JSON
    json_data = json.dumps(people, indent=2)
    print("Generated people data (JSON):")
    print(json_data)
    
    return people

# Run the demonstration
sample_data = demonstrate_module_usage()

print(f"\nGenerated {len(sample_data)} people records using multiple modules:")
print("- random: for generating sample data")
print("- datetime: for timestamps")
print("- json: for data serialization")

print("\n" + "=" * 50)
print("         END OF MODULES PRACTICE")
print("=" * 50)