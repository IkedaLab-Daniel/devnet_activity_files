import os

def authenticate_user():
    """
    Authenticate user by checking credentials against users.txt file
    Returns username if successful, None if failed
    """
    users_file = "users.txt"
    
    # Check if users file exists
    if not os.path.exists(users_file):
        print("Error: users.txt file not found!")
        return None
    
    while True:
        print("\n=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if not username or not password:
            print("Username and password cannot be empty!")
            continue
        
        # Read and check credentials
        try:
            with open(users_file, 'r') as file:
                users_data = file.read().strip()
                
            # Parse user credentials (format: username1,password1 username2,password2)
            user_pairs = users_data.split()
            valid_users = {}
            
            for pair in user_pairs:
                if ',' in pair:
                    user, pwd = pair.split(',', 1)
                    valid_users[user] = pwd
            
            # Check credentials
            if username in valid_users and valid_users[username] == password:
                print(f"Welcome, {username}!")
                return username
            else:
                print("Invalid credentials! Please try again or type 'exit' to quit.")
                choice = input("Continue? (press Enter) or type 'exit': ").strip().lower()
                if choice == 'exit':
                    return None
                    
        except Exception as e:
            print(f"Error reading users file: {e}")
            return None

def view_cart(username):
    """Display all items in the user's cart"""
    cart_file = f"cart_{username}.txt"
    
    print(f"\n=== {username.upper()}'S CART ===")
    
    if not os.path.exists(cart_file):
        print("Your cart is empty!")
        return
    
    try:
        with open(cart_file, 'r') as file:
            items = file.read().strip().split('\n')
            
        if not items or items == ['']:
            print("Your cart is empty!")
        else:
            print("Items in your cart:")
            for i, item in enumerate(items, 1):
                if item.strip():
                    print(f"{i}. {item.strip()}")
                    
    except Exception as e:
        print(f"Error reading cart file: {e}")

def add_item_to_cart(username):
    """Add an item to the user's cart"""
    cart_file = f"cart_{username}.txt"
    
    item = input("Enter item to add: ").strip()
    
    if not item:
        print("Item name cannot be empty!")
        return
    
    try:
        with open(cart_file, 'a') as file:
            file.write(item + '\n')
        print(f"'{item}' has been added to your cart!")
        
    except Exception as e:
        print(f"Error adding item to cart: {e}")

def remove_item_from_cart(username):
    """Remove an item from the user's cart"""
    cart_file = f"cart_{username}.txt"
    
    if not os.path.exists(cart_file):
        print("Your cart is empty!")
        return
    
    try:
        with open(cart_file, 'r') as file:
            items = file.read().strip().split('\n')
            
        # Filter out empty items
        items = [item.strip() for item in items if item.strip()]
        
        if not items:
            print("Your cart is empty!")
            return
        
        print("\nItems in your cart:")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")
        
        try:
            choice = int(input("Enter item number to remove: "))
            if 1 <= choice <= len(items):
                removed_item = items.pop(choice - 1)
                
                # Write remaining items back to file
                with open(cart_file, 'w') as file:
                    for item in items:
                        file.write(item + '\n')
                
                print(f"'{removed_item}' has been removed from your cart!")
            else:
                print("Invalid item number!")
                
        except ValueError:
            print("Please enter a valid number!")
            
    except Exception as e:
        print(f"Error removing item from cart: {e}")

def main():
    """Main program loop"""
    print("=== CART TRACKER SYSTEM ===")
    
    # User authentication
    username = authenticate_user()
    if not username:
        print("Goodbye!")
        return
    
    # Main menu loop
    while True:
        print(f"\n=== CART MENU ({username}) ===")
        print("1. View Cart")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            view_cart(username)
        elif choice == '2':
            add_item_to_cart(username)
        elif choice == '3':
            remove_item_from_cart(username)
        elif choice == '4':
            print("Thank you for using Cart Tracker System!")
            break
        else:
            print("Invalid option! Please select 1-4.")

if __name__ == "__main__":
    main()