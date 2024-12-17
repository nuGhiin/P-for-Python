from user import User
from admin import Admin
from replica import userMenu, adminMenu


alice = User("Tonmoy", "tonmoy@email.com", "123 Sylhet Road", "Savings")
bob = User("Chinmoy", "chinmoy@hotmail.com", "3258 Dhaka Road", "Current")
charlie = User("Mrinmoy", "mrinmoy@yahoo.com", "1204 Rangpur Road", "Savings")


alice.deposit(5000)
bob.deposit(10000)
charlie.deposit(7000)

# Replica System
print("=== Welcome to the Bank Management System ===")

while True:
    print("\nMain Menu:")
    print("1. User Login")
    print("2. Admin Login")
    print("3. Exit")


    choice = int(input("Enter your choice: "))
    if choice == 1:
    #user
        account_number = int(input("Enter your account number: "))
        user = next((u for u in User.userAccounts if u.accountNumber == account_number), None)
        if user:
            print(f"\nWelcome, {user.name}!")
            userMenu(user)
        else:
            print("Account not found. Please try again.")
    elif choice == 2:
    #admin
        print("\nWelcome, Admin!")
        adminMenu()
    elif choice == 3:
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    
