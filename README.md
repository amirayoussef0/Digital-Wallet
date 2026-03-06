# Python Digital Wallet

A simple Digital Wallet system built with Python.  
Users can create accounts, log in, and perform financial operations (deposit, withdraw, transfer) with real-time updates stored in a JSON file.

---

## Features

### Authentication
- Sign Up: create account with username, password, and initial balance.
- Log In: verify username and password.

### JSON Database
- All data stored in `database.json`.
- Updates automatically with every transaction.

### Financial Operations
- **Deposit:** add money to wallet.
- **Withdraw:** remove money if balance allows.
- **Transfer:** send money to another user by username.

### Dashboard
- View username, current balance, and available operations.

---

## Project Structure

project-folder  
│  
├── main.py  
├── wallet.py  
├── database.json  
└── README.md

---

## Example Usage

- Create account → Log in → Deposit → Withdraw → Transfer → Check balance

---

## Error Handling

- Invalid username/password
- Withdraw more than balance
- Transfer to non-existing user

---

## Author

Amira Abdellatif Mohamed Youssef
