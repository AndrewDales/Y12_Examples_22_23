""" A Bank Account Class"""

# Press Shift+F10 to execute
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from hashlib import sha224
import pyinputplus as pyip


class BankAccount:
    def __init__(self, account_number, password, balance=0):
        self.balance = balance
        self.account_number = account_number
        self.password_encoded = sha224(password.encode())

    def __str__(self):
        return f'BankAccount({self.account_number})'

    def _credit(self, value):
        self.balance += value

    def _debit(self, value):
        self.balance -= value

    def show_balance(self):
        return self.balance

    def transfer(self, account, value):
        password_check = False
        while not password_check:
            print(f'Attempting to transfer £{value:.2f} to {account}')
            if self.check_password(pyip.inputStr("Enter your password to validate this transaction: \n")):
                password_check = True
            else:
                print("Password not correct")
        account._credit(value)
        self._debit(value)
        return f'Confirmation:\nPaid £{value:.2f} from {self} to {account}'

    def check_password(self, password):
        return self.password_encoded.digest() == sha224(password.encode()).digest()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    account_1 = BankAccount('0324390', "password", 500)
    account_2 = BankAccount('0969990', "monday", 1000)
    log = account_1.transfer(account_2, 50)
    print(log)
