import unittest
from bank_account import BankAccount  # Assuming the BankAccount class is in a file named bank_account.py

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(1000)  # Create a new account with 1000 balance for each test

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit(self):
        self.assertTrue(self.account.deposit(500))
        self.assertEqual(self.account.get_balance(), 1500)

    def test_deposit_negative_amount(self):
        self.assertFalse(self.account.deposit(-100))
        self.assertEqual(self.account.get_balance(), 1000)

    def test_withdraw(self):
        self.assertTrue(self.account.withdraw(300))
        self.assertEqual(self.account.get_balance(), 700)

    def test_withdraw_insufficient_funds(self):
        self.assertFalse(self.account.withdraw(1500))
        self.assertEqual(self.account.get_balance(), 1000)

    def test_withdraw_negative_amount(self):
        self.assertFalse(self.account.withdraw(-100))
        self.assertEqual(self.account.get_balance(), 1000)

    def test_multiple_operations(self):
        self.account.deposit(500)  # Balance: 1500
        self.account.withdraw(200)  # Balance: 1300
        self.account.deposit(100)  # Balance: 1400
        self.assertEqual(self.account.get_balance(), 1400)

if __name__ == '__main__':
    unittest.main()