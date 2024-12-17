from user import User

class Admin:
    totalBankBalance = 0
    totalLoanAmount = 0
    loanFeature = True

    @staticmethod
    def createAccount(name, email, address, accountType):
        return User(name, email, address, accountType)
    
    @staticmethod
    def delAccount(accountNumber):
        user = None
        for i in User.userAccounts:
            if i.accountNumber == accountNumber:
                user = i
                break
        if user:
            User.userAccounts.remove(user)
            print(f"{user.name}'s Account Deleted!")
        else:
            print("Account Not Found!")
    
    @staticmethod
    def viewAllAccounts():
        print("All user accounts: ")
        for i in User.userAccounts:
            print(f"Name: {i.name}, Account Number: {i.accountNumber}, Balance: {i.balance}")
    
    @staticmethod
    def totalAvailableBalance():
        totalBalance = 0
        for i in User.userAccounts:
            totalBalance += i.balance
        Admin.totalBankBalance = totalBalance
    
    @staticmethod
    def totalLoanAmount():
        t_loanAmount = 0
        for i in User.userAccounts:
            t_loanAmount += i.loansTaken * 10000
        Admin.totalLoanAmount = t_loanAmount
    
    @staticmethod
    def changeLoanFeature():
        if Admin.loanFeature == True:
            Admin.loanFeature = False
            print("Loan feature turned OFF")
        else:
            Admin.loanFeature = True
            print("Loan feature turned ON")


        