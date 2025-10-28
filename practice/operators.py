print("=" * 50)
print("         PYTHON OPERATORS PRACTICE")
print("=" * 50)

# =============================================================================
# COMPARISON OPERATORS
# =============================================================================
print("\n1. COMPARISON OPERATORS")
print("-" * 30)

# Sample variables for comparison
a = 10
b = 20
c = 10
name1 = "Alice"
name2 = "Bob"
name3 = "Alice"

print(f"Variables: a={a}, b={b}, c={c}")
print(f"Names: name1='{name1}', name2='{name2}', name3='{name3}'")

print("\n== (Equal to)")
print("-" * 15)
print(f"a == b: {a == b}")  # False
print(f"a == c: {a == c}")  # True
print(f"name1 == name2: {name1 == name2}")  # False
print(f"name1 == name3: {name1 == name3}")  # True

print("\n!= (Not equal to)")
print("-" * 17)
print(f"a != b: {a != b}")  # True
print(f"a != c: {a != c}")  # False
print(f"name1 != name2: {name1 != name2}")  # True

print("\n< (Less than)")
print("-" * 13)
print(f"a < b: {a < b}")   # True
print(f"b < a: {b < a}")   # False
print(f"'Alice' < 'Bob': {'Alice' < 'Bob'}")  # True (alphabetical)

print("\n> (Greater than)")
print("-" * 16)
print(f"a > b: {a > b}")   # False
print(f"b > a: {b > a}")   # True
print(f"'Bob' > 'Alice': {'Bob' > 'Alice'}")  # True

print("\n<= (Less than or equal to)")
print("-" * 26)
print(f"a <= b: {a <= b}")  # True
print(f"a <= c: {a <= c}")  # True
print(f"b <= a: {b <= a}")  # False

print("\n>= (Greater than or equal to)")
print("-" * 29)
print(f"a >= b: {a >= b}")  # False
print(f"a >= c: {a >= c}")  # True
print(f"b >= a: {b >= a}")  # True

# =============================================================================
# COMPARISON WITH DIFFERENT DATA TYPES
# =============================================================================
print("\n📊 COMPARISONS WITH DIFFERENT TYPES")
print("-" * 37)

# Numbers
int_val = 5
float_val = 5.0
print(f"5 == 5.0: {int_val == float_val}")  # True

# Strings
str1 = "hello"
str2 = "Hello"
print(f"'hello' == 'Hello': {str1 == str2}")  # False (case sensitive)
print(f"'hello'.lower() == 'Hello'.lower(): {str1.lower() == str2.lower()}")  # True

# Lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]
print(f"[1,2,3] == [1,2,3]: {list1 == list2}")  # True
print(f"[1,2,3] == [3,2,1]: {list1 == list3}")  # False

# =============================================================================
# LOGICAL OPERATORS
# =============================================================================
print("\n2. LOGICAL OPERATORS")
print("-" * 25)

# Boolean variables for examples
is_sunny = True
is_warm = True
is_raining = False
has_umbrella = True

print(f"Variables: sunny={is_sunny}, warm={is_warm}, raining={is_raining}, umbrella={has_umbrella}")

print("\nand (Logical AND)")
print("-" * 17)
print(f"sunny and warm: {is_sunny and is_warm}")  # True
print(f"sunny and raining: {is_sunny and is_raining}")  # False
print(f"warm and not raining: {is_warm and not is_raining}")  # True

# Practical example
age = 25
has_license = True
print(f"Can drive (age >= 18 and has_license): {age >= 18 and has_license}")

print("\nor (Logical OR)")
print("-" * 16)
print(f"sunny or raining: {is_sunny or is_raining}")  # True
print(f"raining or has_umbrella: {is_raining or has_umbrella}")  # True
print(f"not sunny or not warm: {not is_sunny or not is_warm}")  # False

# Practical example
is_weekend = True
is_holiday = False
print(f"Can relax (weekend or holiday): {is_weekend or is_holiday}")

print("\nnot (Logical NOT)")
print("-" * 17)
print(f"not sunny: {not is_sunny}")  # False
print(f"not raining: {not is_raining}")  # True
print(f"not (sunny and warm): {not (is_sunny and is_warm)}")  # False

# =============================================================================
# COMPLEX LOGICAL EXPRESSIONS
# =============================================================================
print("\n🧠 COMPLEX LOGICAL EXPRESSIONS")
print("-" * 32)

# Multiple conditions
temperature = 25
humidity = 60
is_indoors = True

comfortable = (temperature >= 20 and temperature <= 28) and humidity < 70
print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
print(f"Comfortable conditions: {comfortable}")

# Using parentheses for clarity
can_go_outside = (is_sunny and not is_raining) or (is_raining and has_umbrella)
print(f"Can go outside: {can_go_outside}")

# =============================================================================
# TRUTH VALUES AND SHORT-CIRCUIT EVALUATION
# =============================================================================
print("\n3. TRUTH VALUES & SHORT-CIRCUIT")
print("-" * 35)

print("Truthy and Falsy values:")
print("-" * 25)

# Falsy values
falsy_values = [False, 0, 0.0, "", [], {}, None]
for val in falsy_values:
    print(f"{repr(val)} is {'truthy' if val else 'falsy'}")

print("\nTruthy values:")
truthy_values = [True, 1, -1, "hello", [1], {"a": 1}, 3.14]
for val in truthy_values:
    print(f"{repr(val)} is {'truthy' if val else 'falsy'}")

print("\nShort-circuit evaluation:")
print("-" * 25)

# AND short-circuit: if first is False, second is not evaluated
x = 0
result1 = x != 0 and 10 / x > 5  # Won't cause division by zero
print(f"x != 0 and 10/x > 5: {result1}")

# OR short-circuit: if first is True, second is not evaluated
name = "Alice"
result2 = len(name) > 0 or len(name) / 0 > 1  # Won't cause division by zero
print(f"len(name) > 0 or len(name)/0 > 1: {result2}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n4. PRACTICAL EXAMPLES")
print("-" * 25)

# Age verification system
age = 20
is_student = True
has_id = True

can_enter_club = age >= 18 and has_id
gets_discount = is_student and age < 25
print(f"Age: {age}, Student: {is_student}, Has ID: {has_id}")
print(f"Can enter club: {can_enter_club}")
print(f"Gets student discount: {gets_discount}")

# Password validation
password = "MyPassword123"
min_length = 8
has_digit = any(c.isdigit() for c in password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)

is_valid_password = (len(password) >= min_length and 
                    has_digit and 
                    has_upper and 
                    has_lower)

print(f"\nPassword validation for '{password}':")
print(f"Length >= {min_length}: {len(password) >= min_length}")
print(f"Has digit: {has_digit}")
print(f"Has uppercase: {has_upper}")
print(f"Has lowercase: {has_lower}")
print(f"Valid password: {is_valid_password}")

# Grade calculation
score = 85
attendance = 90

# Multiple conditions for grade determination
if score >= 90 and attendance >= 95:
    grade = "A+"
elif score >= 85 and attendance >= 90:
    grade = "A"
elif score >= 80 or attendance >= 85:
    grade = "B"
else:
    grade = "C"

print(f"\nScore: {score}, Attendance: {attendance}%")
print(f"Final grade: {grade}")

# =============================================================================
# CHAINING COMPARISONS
# =============================================================================
print("\n5. CHAINING COMPARISONS")
print("-" * 27)

score = 85
print(f"Score: {score}")

# Chained comparisons (Pythonic way)
is_passing = 60 <= score <= 100
is_excellent = 90 <= score <= 100
is_good = 80 <= score < 90

print(f"Passing (60-100): {is_passing}")
print(f"Excellent (90-100): {is_excellent}")
print(f"Good (80-89): {is_good}")

# Multiple chaining
x = 5
result = 1 < x < 10 < 20
print(f"1 < {x} < 10 < 20: {result}")

print("\n" + "=" * 50)
print("         END OF OPERATORS PRACTICE")
print("=" * 50)