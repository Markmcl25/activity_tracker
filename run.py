import os
import gspread
from google.oauth2.service_account import Credentials

# Define the scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from the JSON key file
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Authorize the client
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the Google Sheet by name
SHEET = GSPREAD_CLIENT.open('info_log')

# Access the first worksheet (sheet 1)
worksheet = SHEET.get_worksheet(0)

# Function to add data to the sheet
def add_data_to_sheet(name, email, message, amount=None, date=None, type=None, total_amount_owed=None):
    """
    Appends a row with the given name, email, message, amount, date, type, total_amount_owed to the Google Sheet.

    Parameters:
    name (str): The name to add.
    email (str): The email to add.
    message (str): The message to add.
    amount (float): The amount to add (optional).
    date (str): The date to add (optional).
    type (str): The type to add (optional).
    total_amount_owed (float): The total amount owed to add (optional).
    """
    worksheet.append_row([name, email, message, amount, date, type, total_amount_owed])

# Function to view data
def view_data():
    rows = worksheet.get_all_records()
    for row in rows:
        print(row)

# Function to add numbers
def add_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Sum:", num1 + num2)
    except ValueError:
        print("Please enter valid numbers.")

# Main function to handle user input
def main():
    while True:
        print("Options: add, view, add_numbers, quit")  # Include add_numbers in options
        choice = input("Enter your choice: ").strip().lower()
        if choice == 'add':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            message = input("Enter your message: ")
            amount = float(input("Enter the amount: "))  # Prompt for amount
            date = input("Enter the date: ")  # Prompt for date
            type = input("Enter the type: ")  # Prompt for type
            total_amount_owed = float(input("Enter the total amount owed: "))  # Prompt for total amount owed
            add_data_to_sheet(name, email, message, amount, date, type, total_amount_owed)
        elif choice == 'view':
            view_data()
        elif choice == 'add_numbers':  # Call add_numbers if user chooses this option
            add_numbers()
        elif choice == 'quit':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
