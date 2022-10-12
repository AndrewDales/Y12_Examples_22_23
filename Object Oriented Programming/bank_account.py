from hashlib import sha224
from datetime import datetime
import pyinputplus as pyip


class PasswordError(Exception):
    pass


class TransactionError(Exception):
    pass


class BankAccount:
    """ A Bank Account Class"""

    def __init__(self, account_number, password, balance=0):
        self._balance = balance
        self._password_encoded = sha224(password.encode())
        self.account_number = account_number

    def __repr__(self):
        return f'BankAccount({self.account_number})'

    def credit(self, value):
        self._balance += value

    def debit(self, value):
        self._balance -= value

    def get_balance(self):
        return self._balance

    def transfer(self, account, value):
        account.credit(value)
        self.debit(value)

    def check_password(self, password):
        return self._password_encoded.digest() == sha224(password.encode()).digest()


class Bank:
    next_account_number = 10_000

    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}
        self.transactions = []

    def __repr__(self):
        return f"Bank('{self.bank_name}')"

    def add_account(self, ac_password, amount=0):
        Bank.next_account_number += 1
        self.accounts[Bank.next_account_number] = \
            BankAccount(Bank.next_account_number, ac_password, amount)
        return Bank.next_account_number

    def check_account_number(self, ac_number):
        return ac_number in self.accounts.keys()

    def transact(self, source_account, dest_account, amount, transaction_datetime=datetime.now()):
        if amount <= 0:
            raise TransactionError("Transaction must be for a positive amount")

        if source_account.get_balance() < amount:
            raise TransactionError("Insufficient funds in source account")

        source_account.transfer(dest_account, amount)
        self.transactions.append({
            "date": transaction_datetime,
            "source_acc": source_account.account_number,
            "destination_acc": dest_account.account_number,
            "amount": amount,
        })


class ATM:
    def __init__(self, the_bank):
        self.bank = the_bank
        self.current_user_account = None
        self.current_user_validated = False
        self.menu_choices = {"Show Balance": self.show_balance,
                             "Take cash from account": self.remove_cash,
                             "Deposit cash in account": self.deposit_cash,
                             "Transfer cash to another account": self.transfer_cash,
                             "Exit": self.exit}
        self.atm_menu()

    def validate_account(self):
        ac_num = 0
        while not ac_num:
            ac_num = pyip.inputInt("Enter account number\n:",
                                   min=10_000,
                                   max=Bank.next_account_number,
                                   limit=3)
            if not self.bank.check_account_number(ac_num):
                print(f'Bank Account with account number {ac_num} not found')
                ac_num = 0
        return self.bank.accounts[ac_num]

    def validate_password(self):
        self.current_user_validated = False
        while not self.current_user_validated:
            current_pass = pyip.inputStr("Enter your password\n:")
            if self.current_user_account.check_password(current_pass):
                self.current_user_validated = True
            else:
                print("Password not correct")

    def show_balance(self):
        print(f"Current Balance on {self.current_user_account}:")
        print(f"£{self.current_user_account.get_balance():.2f}\n")

    def remove_cash(self):
        cash_requested = pyip.inputInt("Enter the amount of cash that your require: ", min=0, max=400)
        if cash_requested > self.current_user_account.get_balance():
            print("You do not have sufficient funds in your account")
        else:
            input(f"Take £{cash_requested:.0f} from the slot")
            self.current_user_account.debit(cash_requested)
        print()
        self.show_balance()

    def deposit_cash(self):
        cash_deposited = pyip.inputInt("Enter the amount of cash that your wish to deposit: ", min=0, max=1000)
        input(f"Put £{cash_deposited:.0f} in the deposit area")

        self.current_user_account.credit(cash_deposited)
        print()
        self.show_balance()

    def transfer_cash(self):
        print("Enter the account that you wish to transfer money to")
        destination = self.validate_account()
        transfer_amount = pyip.inputInt("Enter the amount of money that you wish to transfer: ",
                                        min=1,
                                        max=self.current_user_account.get_balance()
                                        )
        print("Re-enter your password")
        self.validate_password()
        if self.current_user_validated:
            self.bank.transact(self.current_user_account, destination, transfer_amount)
            print(f"You transferred £{transfer_amount:.0f} to {destination}")

    def exit(self):
        self.current_user_account = None
        self.current_user_validated = False
        print("Goodbye\n")
        self.atm_menu()

    def atm_menu(self):
        print(f"Welcome to {self.bank}\n")
        self.current_user_account = self.validate_account()
        self.validate_password()

        if self.current_user_validated:
            while True:
                choice = pyip.inputMenu(list(self.menu_choices), numbered=True)
                self.menu_choices[choice]()


if __name__ == "__main__":
    my_bank = Bank("Highgate Bank")
    account_1 = my_bank.add_account("qwerty", 1000)
    account_2 = my_bank.add_account("password", 2000)
    # my_atm = ATM(my_bank)
