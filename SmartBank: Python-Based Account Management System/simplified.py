class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Amount {amount} deposited. Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Amount {amount} withdrawn. Current balance: {self.balance}"
        else:
            return "Insufficient funds"

    def get_balance(self):
        return f"Current balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance=0.0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, account_holder, initial_balance)
            return f"Account created for {account_holder}"
        else:
            return "Account with this account number already exists"

    def perform_transaction(self, account_number, transaction_type, amount=0.0):
        account = self.accounts.get(account_number)
        if account:
            if transaction_type == "deposit":
                return account.deposit(amount)
            elif transaction_type == "withdraw":
                return account.withdraw(amount)
            elif transaction_type == "balance":
                return account.get_balance()
            else:
                return "Invalid transaction type"
        else:
            return "Account not found"


def main():
    bank = Bank()

    while True:
        print("\nSmartBank System")
        print("1. Create Account")
        print("2. Perform Transaction")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            print(bank.create_account(account_number, account_holder, initial_balance))

        elif choice == '2':
            account_number = input("Enter account number: ")
            transaction_type = input("Enter transaction type (deposit/withdraw/balance): ").lower()
            if transaction_type in ['deposit', 'withdraw']:
                amount = float(input("Enter amount: "))
            else:
                amount = 0.0
            print(bank.perform_transaction(account_number, transaction_type, amount))

        elif choice == '3':
            print("Exiting SmartBank System...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
