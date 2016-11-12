class BankAccount(object):
    """The BankAccount class with 
    no implementation of withdraw and deposit methods
    """
    def __init__(self):
        pass

    def withdraw():
        pass
        
    def deposit():
        pass

class SavingsAccount(BankAccount):
    """The SavingsAccount class, inheriting the BankAccount parent class,
     for instanciating SavingsAccount objects"""

    def __init__(self):
        self.balance = 500

    def deposit(self, amount):
        """method for depositing the amount to SavingsAccount"""
        if (amount < 0):
            return "Invalid deposit amount"
        else:
            self.balance += amount
            return self.balance

    def withdraw(self, amount):
        """method for withdrawing amount from the SavingsAccount"""
        
        # Ensure minimum balance is always 500
        if ((self.balance - amount) > 0) and ((self.balance - amount) < 500):
            return "Cannot withdraw beyond the minimum account balance"
        elif (self.balance - amount) < 0:
            return "Cannot withdraw beyond the current account balance"
        elif amount < 0:
            return "Invalid withdraw amount"
        else:
            self.balance -= amount
            return self.balance

class CurrentAccount(BankAccount):
    """The CurrentAccount class, inheriting the BankAccount parent class,
     for instanciating CurrentAccount objects"""

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        """method for depositng amount passed to the CurrentAccount"""

        if amount < 0:
            return "Invalid deposit amount"
        else:
            self.balance += amount
            return self.balance

    def withdraw(self, amount):
        """method for withdrawing the passed amount from the CurrentAccount"""

        if amount < 0:
            return "Invalid withdraw amount"
        elif self.balance< amount:
            return "Cannot withdraw beyond the current account balance"
        else:
            self.balance -= amount
            return self.balance