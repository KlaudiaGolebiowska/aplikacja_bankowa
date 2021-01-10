import random


class Account:

    def __init__(self, amount, owner):
        self._balance = amount
        self._owner = owner
        self._number = random.randint(1, 10000)

    def transfer(self, amount):
        balance = self._balance
        balance += amount
        if balance < 0:
            pass
        else:
            self._balance = balance

    def __repr__(self):
        return f"{self._number}2"

    def get_balance(self):
        return self._balance

    def get_number(self):
        return self._number

    def get_owner(self):
        return self._owner