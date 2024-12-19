class ATM:
    def __init__(self):
        self.balance = 0 

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount}. Your new balance is ${self.balance}.")
        else:
            print("Invalid deposit amount. Please try again.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Successfully withdrew ${amount}. Your new balance is ${self.balance}.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount. Please try again.")

    def start(self):
        while True:
            print("\n--- Welcome to the ATM ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            
            choice = input("Select an option (1-4): ")
            
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter the amount to deposit: $"))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter the amount to withdraw: $"))
                self.withdraw(amount)
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

# Instantiate ATM object and start the interface
atm = ATM()
atm.start()
