class User:
    userAccounts = []
    accountCounter = 1000

    def __init__(self, name, email, address, accountType):
        self.name = name
        self.email = email
        self.address = address
        self.accountType = accountType
        self.accountNumber = User.accountCounter
        self.balance = 0
        self.transactionHistory = []
        self.loansTaken = 0

        User.accountCounter +=1
        User.userAccounts.append(self)
    




        