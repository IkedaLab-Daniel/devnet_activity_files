print("=" * 50)
print("       PYTHON CONDITIONAL STATEMENTS PRACTICE")
print("=" * 50)

# =============================================================================
# BASIC IF STATEMENTS
# =============================================================================
print("\n1. BASIC IF STATEMENTS")
print("-" * 25)

age = 18
print(f"Age: {age}")

if age >= 18:
    print("You are an adult!")

print("This line always executes.")

# Simple condition examples
temperature = 25
if temperature > 30:
    print("It's hot outside!")

score = 85
if score >= 80:
    print("Great job! You passed with a good score.")

# =============================================================================
# IF-ELSE STATEMENTS
# =============================================================================
print("\n2. IF-ELSE STATEMENTS")
print("-" * 23)

number = 7
print(f"Number: {number}")

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Password check example
password = "secret123"
correct_password = "secret123"

if password == correct_password:
    print("Access granted!")
else:
    print("Access denied!")

# Age verification
user_age = 16
if user_age >= 18:
    print("You can vote!")
else:
    print(f"You need to wait {18 - user_age} more years to vote.")

# =============================================================================
# IF-ELIF-ELSE STATEMENTS
# =============================================================================
print("\n3. IF-ELIF-ELSE STATEMENTS")
print("-" * 29)

# Grade calculation
score = 85
print(f"Score: {score}")

if score >= 90:
    grade = "A"
    print(f"Excellent! Grade: {grade}")
elif score >= 80:
    grade = "B"
    print(f"Good job! Grade: {grade}")
elif score >= 70:
    grade = "C"
    print(f"Average. Grade: {grade}")
elif score >= 60:
    grade = "D"
    print(f"Below average. Grade: {grade}")
else:
    grade = "F"
    print(f"Failed. Grade: {grade}")

# Weather recommendation
weather = "rainy"
print(f"\nWeather: {weather}")

if weather == "sunny":
    print("Perfect day for outdoor activities!")
elif weather == "cloudy":
    print("Good day for a walk in the park.")
elif weather == "rainy":
    print("Stay indoors and read a book.")
elif weather == "snowy":
    print("Build a snowman or go skiing!")
else:
    print("Weather condition not recognized.")

# Traffic light system
light_color = "green"
print(f"\nTraffic light: {light_color}")

if light_color == "red":
    action = "Stop"
elif light_color == "yellow":
    action = "Caution"
elif light_color == "green":
    action = "Go"
else:
    action = "Unknown signal"

print(f"Action: {action}")

# =============================================================================
# NESTED IF STATEMENTS
# =============================================================================
print("\n4. NESTED IF STATEMENTS")
print("-" * 26)

# Login system with multiple checks
username = "admin"
password = "password123"
is_active = True

print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")
print(f"Account active: {is_active}")

if username == "admin":
    if password == "password123":
        if is_active:
            print("Welcome, Admin! Full access granted.")
        else:
            print("Account is deactivated. Contact support.")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")

# Age and license verification
person_age = 20
has_license = True
has_car = False

print(f"\nAge: {person_age}, License: {has_license}, Car: {has_car}")

if person_age >= 18:
    print("Age requirement met.")
    if has_license:
        print("Has valid license.")
        if has_car:
            print("Can drive immediately!")
        else:
            print("Need to get a car first.")
    else:
        print("Need to get a license first.")
else:
    print("Too young to drive.")

# =============================================================================
# COMPLEX CONDITIONS
# =============================================================================
print("\n5. COMPLEX CONDITIONS")
print("-" * 24)

# Multiple conditions with logical operators
temperature = 25
humidity = 60
is_sunny = True

print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Sunny: {is_sunny}")

if temperature >= 20 and temperature <= 30 and humidity < 70:
    if is_sunny:
        print("Perfect weather for outdoor activities!")
    else:
        print("Good weather, but a bit cloudy.")
elif temperature > 30 or humidity >= 70:
    print("Too hot or humid for outdoor activities.")
else:
    print("Too cold for outdoor activities.")

# Student discount eligibility
age = 22
is_student = True
has_student_id = True
gpa = 3.5

print(f"\nAge: {age}, Student: {is_student}, Has ID: {has_student_id}, GPA: {gpa}")

if is_student and has_student_id:
    if age <= 25 and gpa >= 3.0:
        discount = 20
        print(f"Eligible for {discount}% student discount!")
    elif age <= 25:
        discount = 10
        print(f"Eligible for {discount}% discount (improve GPA for more)!")
    else:
        print("Student discount not available (age limit exceeded).")
else:
    print("Not eligible for student discount.")

# =============================================================================
# CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)
# =============================================================================
print("\n6. CONDITIONAL EXPRESSIONS (TERNARY)")
print("-" * 38)

# Basic ternary operator
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age: {age} -> Status: {status}")

# Number comparison
a = 15
b = 10
max_value = a if a > b else b
print(f"Max of {a} and {b}: {max_value}")

# Grade status
score = 75
pass_status = "Pass" if score >= 60 else "Fail"
print(f"Score: {score} -> {pass_status}")

# Even/odd check
number = 17
parity = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {parity}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n7. PRACTICAL EXAMPLES")
print("-" * 25)

# ATM withdrawal system
account_balance = 1000
withdrawal_amount = 250
daily_limit = 500
withdrawals_today = 200

print(f"Balance: ${account_balance}")
print(f"Withdrawal request: ${withdrawal_amount}")
print(f"Daily limit: ${daily_limit}")
print(f"Already withdrawn today: ${withdrawals_today}")

if withdrawal_amount <= 0:
    print("Invalid withdrawal amount.")
elif account_balance < withdrawal_amount:
    print("Insufficient funds.")
elif (withdrawals_today + withdrawal_amount) > daily_limit:
    remaining_limit = daily_limit - withdrawals_today
    print(f"Daily limit exceeded. You can withdraw up to ${remaining_limit} more today.")
else:
    new_balance = account_balance - withdrawal_amount
    print(f"Transaction successful!")
    print(f"Withdrawn: ${withdrawal_amount}")
    print(f"New balance: ${new_balance}")

# Online shopping cart
item_price = 50
quantity = 3
user_type = "premium"
is_weekend = True
coupon_code = "SAVE10"

subtotal = item_price * quantity
print(f"\nItem price: ${item_price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal}")
print(f"User type: {user_type}")
print(f"Weekend: {is_weekend}")
print(f"Coupon: {coupon_code}")

# Calculate discount
discount = 0
if user_type == "premium":
    discount += 10  # 10% premium discount
    
if is_weekend:
    discount += 5   # 5% weekend discount
    
if coupon_code == "SAVE10":
    discount += 10  # 10% coupon discount

# Apply maximum discount limit
if discount > 20:
    discount = 20
    print("Maximum discount of 20% applied.")

discount_amount = subtotal * (discount / 100)
final_total = subtotal - discount_amount

print(f"Total discount: {discount}%")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"Final total: ${final_total:.2f}")

# =============================================================================
# MENU SYSTEM EXAMPLE
# =============================================================================
print("\n8. MENU SYSTEM EXAMPLE")
print("-" * 26)

print("=== Restaurant Menu ===")
print("1. Pizza - $12")
print("2. Burger - $8")
print("3. Salad - $6")
print("4. Drink - $2")

# Simulate user choice
choice = "2"  # Normally this would be input()
print(f"Selected option: {choice}")

if choice == "1":
    item = "Pizza"
    price = 12
elif choice == "2":
    item = "Burger"
    price = 8
elif choice == "3":
    item = "Salad"
    price = 6
elif choice == "4":
    item = "Drink"
    price = 2
else:
    item = "Invalid selection"
    price = 0

if price > 0:
    print(f"You ordered: {item}")
    print(f"Price: ${price}")
    
    # Apply tax
    tax_rate = 0.08
    tax_amount = price * tax_rate
    total = price + tax_amount
    
    print(f"Tax (8%): ${tax_amount:.2f}")
    print(f"Total: ${total:.2f}")
else:
    print("Please make a valid selection.")

print("\n" + "=" * 50)
print("    END OF CONDITIONAL STATEMENTS PRACTICE")
print("=" * 50)