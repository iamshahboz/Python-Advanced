import unittest 
from bank_account import BankAccount 

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # Runs before every test method 
        self.account = BankAccount(balance=100)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)

    def test_deposit_increases_balance(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_withdraw_decreases_balance(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

    def test_withdraw_more_than_balance_raises_error(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1000)

    def tearDown(self):
        # Runs after EVERY test method — cleanup (closing files, connections, etc.)
        del self.account


if __name__ == "__main__":
    unittest.main()
