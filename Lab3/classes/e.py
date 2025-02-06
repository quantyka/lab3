class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Withdrawal of ${amount} failed. Available balance: ${self.balance}")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")

    def __str__(self):
        return f"BankAccount(owner='{self.owner}', balance=${self.balance})"


account = BankAccount("John Doe", 1000)  
print(account)


account.deposit(500)    
account.deposit(200)    


account.withdraw(300)   
account.withdraw(1500)  
account.withdraw(200)   


print(account)