# MC-Donald-s-drive-thru-Order
This Python script simulates a Fast Food Drive-Thru ordering system. It displays a menu with items like cheeseburgers, fries, soda, ice cream, and cookies. Users input the item number to place an order. The program validates the input, retrieves the corresponding item, and handles invalid entries gracefully with error messages.
# Fast Food Drive-Thru Simulator

This Python script simulates a simple Fast Food Drive-Thru ordering system.

## Description

The script presents a menu of fast food items to the user:
- 🍔 Cheeseburger
- 🍟 Fries
- 🥤 Soda
- 🍦 Ice Cream
- 🍪 Cookie

Users can then input the number corresponding to the item they wish to order. The program will confirm the ordered item or display an error message if the input is invalid (e.g., not a number, or a number not on the menu).

## How to Run

1.  Ensure you have Python installed on your system.
2.  Save the script as `drive_thru.py`.
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the script using the command:
    ```bash
    python drive_thru.py
    ```

## Example Usage

```
Welcome to Fast Food Drive-Thru!
Here is our menu:
1. 🍔 Cheeseburger
2. 🍟 Fries
3. 🥤 Soda
4. 🍦 Ice Cream
5. 🍪 Cookie
Please enter the number of the item you'd like to order.
Enter the item number: 1
You ordered: 🍔 Cheeseburger
```

```
Welcome to Fast Food Drive-Thru!
Here is our menu:
1. 🍔 Cheeseburger
2. 🍟 Fries
3. 🥤 Soda
4. 🍦 Ice Cream
5. 🍪 Cookie
Please enter the number of the item you'd like to order.
Enter the item number: 7
You ordered: ❌ Invalid item number. Please try again.
```

```
Welcome to Fast Food Drive-Thru!
Here is our menu:
1. 🍔 Cheeseburger
2. 🍟 Fries
3. 🥤 Soda
4. 🍦 Ice Cream
5. 🍪 Cookie
Please enter the number of the item you'd like to order.
Enter the item number: abc
❌ Invalid input. Please enter a number.
```
