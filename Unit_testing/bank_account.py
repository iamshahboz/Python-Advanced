
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount 

    def withdraw(self, amount):
        if amount >= self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount 


# The problem: If you create a fresh bank account, inside every single test method, you are repeating yourself. SetUp resolve it.
# It runs before every test method
