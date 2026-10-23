

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner 
        self.__balance = balance ## Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount 

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount 

    def get_balance(self):
        return self.__balance # Controlled access

# usage 

account = BankAccount('Alice', 100)
print(account.get_balance())

# trying to access private attribute directly

print(account.__balance) # Rises attribute error


