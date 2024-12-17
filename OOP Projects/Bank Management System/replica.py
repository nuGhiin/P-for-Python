from user import User
from admin import Admin

def userMenu(user):
    while True:
        print("\nUser Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            user.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            user.withdraw(amount)
        elif choice == 3:
            user.checkBalance()
        elif choice == 4:
            user.viewTransactionHistory()
        elif choice == 5:
            amount = float(input("Enter loan amount: "))
            user.takeLoan(amount)
        elif choice == 6:
            recipientAccountNumber = int(input("Enter recipient account number: "))
            amount = float(input("Enter amount to transfer: "))
            user.transferMoney(recipientAccountNumber, amount)
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")


def adminMenu():
    while True:
        print("\nAdmin Menu:")
        print("1. View All Accounts")
        print("2. Check Total Available Balance")
        print("3. Check Total Loan Amount")
        print("4. Toggle Loan Feature")
        print("5. Delete Account")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            Admin.viewAllAccounts()
        elif choice == 2:
            Admin.totalAvailableBalance()
        elif choice == 3:
            Admin.totalLoanAmount()
        elif choice == 4:
            Admin.changeLoanFeature()
        elif choice == 5:
            accountNumber = int(input("Enter account number to delete: "))
            Admin.delAccount(accountNumber)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")
    


def main():
    print("Welcome to the Bank Management System")
    while True:
        print("\nMain Menu:")
        print("1. User Login")
        print("2. Admin Login")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            accountNumber = int(input("Enter your account number: "))
            user = next((u for u in User.userAccounts if u.accountNumber == accountNumber), None)
            if user:
                userMenu(user)
            else:
                print("Account not found.")
        elif choice == 2:
            adminMenu()
        elif choice == 3:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")