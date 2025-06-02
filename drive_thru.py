def welcome():
    """Display the menu."""
    print("Welcome to Fast Food Drive-Thru!")
    print("Here is our menu:")
    print("1. 🍔 Cheeseburger")
    print("2. 🍟 Fries")
    print("3. 🥤 Soda")
    print("4. 🍦 Ice Cream")
    print("5. 🍪 Cookie")
    print("Please enter the number of the item you'd like to order.")

def get_item(item_number):
    """Return the name of the item based on the number."""
    menu_items = [
        "🍔 Cheeseburger",
        "🍟 Fries",
        "🥤 Soda",
        "🍦 Ice Cream",
        "🍪 Cookie"
    ]
    # Adjust item_number to be 0-indexed for list access
    index = item_number - 1
    if 0 <= index < len(menu_items):
        return menu_items[index]
    else:
        return "❌ Invalid item number. Please try again."

def main():
    """Main program to take user input and display the order."""
    welcome()
    try:
        item_number = int(input("Enter the item number: "))
        print(f"You ordered: {get_item(item_number)}")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

# Run the program
if __name__ == "__main__":
    main()
