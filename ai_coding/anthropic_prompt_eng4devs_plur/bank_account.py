class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            return True
        return False

    def get_balance(self):
        return self._balance