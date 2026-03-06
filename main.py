import json
import os

DB_file = 'database.json'

def load_data():
    if not os.path.exists(DB_file):
        return{"users":{}}
    with open(DB_file,'r') as file:
        try:
            data = json.load(file)
            if "users" not in data:
                data["users"] = {}
            return data
        except json.JSONDecodeError:
            return {"users": {}}

def save_data(data):
    with open(DB_file,'w') as file:
        json.dump(data, file, indent=4)
    print("Data updated successfully")

def sign_up():
    data = load_data()
    username = input("Enter Username: ")
    if username in data["users"]:
        print("Username already exists!")
        return
    password = input("Enter Password: ")
    try:
        balance = float(input("Enter Initial Balance: "))
    except ValueError:
        print("Invalid balance! Please enter a number.")
        return
    data["users"][username] = {
        "password": password,
        "balance": balance
    }
    save_data(data)
    print(f"Account created successfully for {username}!")


def log_in():
    data = load_data()
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in data["users"]:
        if data["users"][username]["password"] == password:
            user_dashboard(username)
        else:
            print("Error: Wrong password!")
    else:
        print("Error: Username not found!")


def deposit(username):
    data = load_data()
    try:
        amount = float(input("Enter the deposit amount: "))
        if amount <= 0:
            print("Wrong!Please enter a positive number.")
            return

        data["users"][username]["balance"] += amount
        save_data(data)
        print(f"The deposit was successful! and your current balance:{data['users'][username]['balance']}")
    except ValueError:
        print("Wrong! Please enter a number.")


def withdraw(username):
    data = load_data()
    try:
        amount = float(input("Enter the withdraw amount: "))
        current_balance = data["users"][username]["balance"]

        if amount > current_balance:
            print(f"Your balance is insufficient, your current balance: {current_balance}")
        elif amount <= 0:
            print("Wrong!Please enter a positive number.")
        else:
            data["users"][username]["balance"] -= amount
            save_data(data)
            print(f"The withdrawal was successful! you current balance: {data['users'][username]['balance']}")
    except ValueError:
        print("Wrong! Please enter a number.")


def transfer(sender_username):
    data = load_data()
    receiver_username = input("Enter receiver username: ")

    if receiver_username not in data["users"]:
        print("Username not found!")
        return
    if receiver_username == sender_username:
        print("You cannot transfer to yourself!")
        return

    try:
        amount = float(input(f"Enter the amount you want to transfer to {receiver_username}: "))
        sender_balance = data["users"][sender_username]["balance"]

        if amount > sender_balance:
            print("Your balance is insufficient.")
        elif amount <= 0:
            print("Wrong!Please enter a positive number.")
        else:

            data["users"][sender_username]["balance"] -= amount
            data["users"][receiver_username]["balance"] += amount

            save_data(data)
            print(f"The transfer was successful! your current balance: {data['users'][sender_username]['balance']}")
    except ValueError:
        print("Wrong! Please enter a number.")

def user_dashboard(username):
    while True:

        data = load_data()
        user_info = data["users"][username]

        print(f"\n--- {username}'s Dashboard ---")
        print(f"Current Balance: ${user_info['balance']}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Log Out")

        choice = input("Select an option: ")

        if choice == '1':
            deposit(username)
        elif choice == '2':
            withdraw(username)
        elif choice == '3':
            transfer(username)
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid choice!")



def main():
    print("Welcome to Digital Wallet System")
    while True:
        print("1.Create new account")
        print("2.Login")
        print("3.Exit")

        choice = input("Select an option: ")
        if choice == "1":
            sign_up()
        elif choice == '2':
            log_in()
        elif choice == "3":
            print("Thank you for using our System")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
