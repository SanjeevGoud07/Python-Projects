from bank import Bank

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
