from app.account import Account


class Card:

    def __init__(self, account: Account, pin):
        self._account = account
        self._pin = pin

    def __repr__(self):
        return self._account.get_owner()

    def get_account(self):
        return self._account

    def check_pin(self, pin) -> bool:
        if self._pin == pin:
            return True
        else:
            return False

    def owner(self):
        return self._account.get_owner()
