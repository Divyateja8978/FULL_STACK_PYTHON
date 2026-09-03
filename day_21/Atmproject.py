balance = 5000
pin = 1234

def check_balance():
    print("Current Balance:", balance)

def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    balance += amount
    print("Amount deposited successfully")
    print("New Balance:", balance)

def withdraw():
    global balance
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance -= amount
        print("Please collect your cash")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient balance")


entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()

        elif choice == 2:
            deposit()

        elif choice == 3:
            withdraw()

        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Incorrect PIN")