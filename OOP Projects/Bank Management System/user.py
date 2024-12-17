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
    
    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            self.transactionHistory.append(f"Deposited: {amount}")
            print(f"Deposit Successful. New balance: {self.balance}")
        else:
            print("Deposit Failed!")
    
    def withdraw(self, amount):
        if amount>self.balance:
            print("Withdrawal amount exceeded!")
        elif amount<=0:
            print("Withdrawal amount must be positive!")
        else:
            self.balance -= amount
            self.transactionHistory.append(f"Withdrawn: {amount}")
            print(f"Withdrawal successful. New balance: {self.balance}")
    
    def checkBalance(self):
        print(f"Available balance: {self.balance}")
    
    def viewTransactionHistory(self):
        print("Transaction History: ")
        for i in self.transactionHistory:
            print(i)
    
    def takeLoan(self, amount):
        if self.loansTaken<2:
            self.balance += amount
            self.loansTaken += 1
            self.transactionHistory.append(f"Loan taken: {amount}")
            print(f"Loan approved. New balance: {self.balance}")
        else:
            print("Loan limit exceeded. You can only take two loans!")
    
    def transferMoney(self, recipientAccountNumber, amount):
        # recipient = next((
        #     user for user in User.userAccounts
        #     if user.accountNumber == recipientAccountNumber
        # ), None)
        recipient = None
        for user in User.userAccounts:
            if user.accountNumber == recipientAccountNumber:
                recipient = user
                break

        if recipient is None:
            print("Account does not exist!")
        elif amount>self.balance:
            print("Transfer amount exceeded your current balance!")
        elif amount<=0:
            print("Transfer amount must be positive!")
        else:
            self.balance -= amount
            recipient.balance +=amount
            self.transactionHistory.append(f"Money Transferred: {amount} to {recipientAccountNumber}")
            recipient.transactionHistory.append(f"Money Received: {amount} from {self.accountNumber}")
            print(f"Transfer successful. Your new balance: {self.balance}")





        