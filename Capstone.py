
# ATM clone:

import datetime

# Class Account:


class Account:

    dateCreated = datetime.datetime.now()

    def __init__(self, id, balance, annualInterestRate):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getBalance(self):
        return self.balance

    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12

    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: ")

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return "\nAccount ID: {0.id} \nAccount Balance: {0.balance} \nAnnual Interest Rate: {0.annualInterestRate} % \nAccount Created: {0.dateCreated}".format(self)


# User Accounts:

accounts = [
    Account(0, 100, 6),
    Account(1, 100, 6),
    Account(2, 100, 6),
    Account(3, 100, 6),
    Account(4, 100, 6),
    Account(5, 100, 6),
    Account(6, 100, 6),
    Account(7, 100, 6),
    Account(8, 100, 6),
    Account(9, 100, 6)
]


# User Prompts

while True:

    id_check = int(input("\nPlease enter Account ID:\n"))
    print(accounts[id_check])

    current_acc = accounts[id_check]

    while True:

        print("""
            1)  Balance
            2)  Withdraw
            3)  Deposit
            4)  Exit

            """)

        option = int(input("Enter Option: "))

        if option == 1:
            print("Current Balance:",  current_acc.getBalance())

        if option == 2:
            print("Your current balance:", current_acc.getBalance())

            withdraw_amount = float(input("Enter withdraw amount: "))
            current_acc.withdraw(withdraw_amount)
            print(current_acc.getBalance())

        if option == 3:
            print("Your current balance:", current_acc.getBalance())
            deposit_amount = float(input("Enter deposit amount: "))

            if deposit_amount > 0:
                current_acc.deposit(deposit_amount)
                print("Your new balance:", current_acc.getBalance())
            else:
                print("No deposit made")

        if option == 4:
            break
