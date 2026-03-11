# Inventory

## Description
The program allows the user to add items to an inventory and calculate the total value of all products.

## How it works
- A dictionary is used to store the inventory.
- The dictionary contains the following keys:
  - `items_name`
  - `prices_by_1`
  - `quantitys`
  - `total_price`

Each key contains a list where the program stores the values entered by the user.

## Project Structure
The project uses multiple Python files:

- **main.py** → Main program execution.
- **verify_numbers.py** → Functions to validate that price and quantity are numbers greater than 0.
- **functions.py** → Functions to:
  - Add items
  - Show inventory
  - Show total inventory value

## Features
- Add items to the inventory
- Validate numeric inputs
- Display stored items
- Calculate the total inventory value
