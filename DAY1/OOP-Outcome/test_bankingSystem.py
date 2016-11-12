import unittest

from bankingSystem import BankAccount, CurrentAccount, SavingsAccount

class CurrentAccountTestCases(unittest.TestCase):
    """Class for all possible test cases in the main BankAccount class"""

    def setUp(self):
        """creating an instance of CurrentAccount"""
        self.CA = CurrentAccount()
    
    def tearDown(self):
        """destroying an instance of SavingsAccount"""
        del self.CA

    def test_current_account_is_instance_of_bank_account(self):
        self.assertTrue(isinstance(self.CA, BankAccount), msg='CurrentAccount is not a subclass of BankAccount')
  
    def test_current_account_can_deposit_valid_amounts(self):
        balance = self.CA.deposit(1500)
        self.assertEquals(balance, 1500)
  
    def test_current_account_cannot_withdraw_more_than_current_balance(self):
        message = self.CA.withdraw(1500)
        self.assertEquals(message, 'Cannot withdraw beyond the current account balance', msg='No overdrafts')
  
    def test_current_account_can_withdraw_valid_cash_amounts(self):
        self.CA.deposit(23001)
        self.CA.withdraw(437)
        self.assertEquals(self.CA.balance, 22564, msg='Incorrect balance after withdrawal')
    
class SavingsAccountTestCases(unittest.TestCase):
    def setUp(self):
        """creating an instance of SavingsAccount"""
        self.SA = SavingsAccount()
    
    def tearDown(self):
        """destroying an instance of SavingsAccount"""
        del self.SA
  
    def test_savings_account_is_instance_of_bank_account(self):
        self.assertTrue(isinstance(self.SA, BankAccount), msg='SavingsAccount is not a subclass of BankAccount')

    def test_savings_account_can_deposit_valid_amounts(self):
        init_balance = self.SA.balance
        balance = self.SA.deposit(1500)
        self.assertEquals(balance, (1500 + init_balance), msg='Balance does not match deposit')

    def test_savings_account_cannot_withdraw_more_than_current_balance(self):
        message = self.SA.withdraw(1500)
        self.assertEquals(message, 'Cannot withdraw beyond the current account balance', msg='No overdrafts')

    def test_savings_account_can_withdraw_valid_amounts_successfully(self):
        self.SA.deposit(2300)
        self.SA.withdraw(543)
        self.assertEquals(2257, self.SA.balance, msg="Incorrect balance after withdrawal")

if __name__ == '__main__':
  unittest.main()