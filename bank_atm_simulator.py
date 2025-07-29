balance = 1000
PIN = '1234'

def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposited successfully. New balance: ₹{balance}")
    except:
        print("Invalid input!")

def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"Withdrawal successful. New balance: ₹{balance}")
    except:
        print("Invalid input!")

def atm():
    pin = input("Enter PIN: ")
    if pin != PIN:
        print("Incorrect PIN.")
        return
    while True:
        print("\n--- ATM Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            deposit()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            print(f"Your balance is ₹{balance}")
        elif choice == '4':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice.")

atm()
