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


# Example Usage
bank = Bank()

print(bank.create_account("123", "Alice"))
print(bank.create_account("456", "Bob", 1000.0))

print(bank.perform_transaction("123", "deposit", 500.0))
print(bank.perform_transaction("456", "withdraw", 200.0))
print(bank.perform_transaction("789", "balance"))  # Non-existing account

print(bank.accounts["123"].get_balance())
