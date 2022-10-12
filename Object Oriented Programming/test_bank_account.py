import pytest
from bank_account import Bank, BankAccount


class TestBankAccount:
    @pytest.fixture
    def bank_accounts(self):
        accounts = [BankAccount(10001, "qwerty", 5000), BankAccount(10002, "password", 3000)]
        return accounts

    def test_credit(self, bank_accounts):
        acc_1 = bank_accounts[0]
        acc_1.credit(500)
        assert acc_1.get_balance() == 5500

    def test_debit(self, bank_accounts):
        acc_1 = bank_accounts[0]
        acc_1.debit(4000)
        assert acc_1.get_balance() == 1000

    def test_get_balance(self, bank_accounts):
        assert bank_accounts[1].get_balance() == 3000

    def test_transfer(self, bank_accounts):
        acc_1, acc_2 = bank_accounts
        acc_1.transfer(acc_2, 700)
        assert acc_1.get_balance() == 4300
        assert acc_2.get_balance() == 3700

    def test_check_password(self, bank_accounts):
        assert bank_accounts[0].check_password("qwerty")
        assert not bank_accounts[1].check_password("qwerty")
