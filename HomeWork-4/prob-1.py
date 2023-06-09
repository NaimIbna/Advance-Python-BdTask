# Using abstract class show bank statement of money withdrawn, deposited and available balance at the end of the month 

from abc import ABC, abstractmethod

class BankStatement(ABC):
    def __init__(self):
        self.balance = 0

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    def display(self):
        print("Available Balance: ", self.balance)

class MyAccount(BankStatement):
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

def final_show(statement):
    deposit_amount = float(input("Enter deposit amount: "))
    statement.deposit(deposit_amount)

    withdrawal_amount = float(input("Enter withdrawal amount: "))
    statement.withdraw(withdrawal_amount)

    statement.display()

amount = MyAccount()
final_show(amount)