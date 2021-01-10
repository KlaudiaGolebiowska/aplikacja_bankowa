class CashMachine:

    def __init__(self, *args, **kwargs):
        self._is_working = True
        self._card = None
        self._cash_level = kwargs['start_cash'] if 'start_cash' in kwargs.keys() else 0
        if not isinstance(self._cash_level, int):
            raise ValueError("Start cash should be integer")

    def is_working(self) -> bool:
        return self._is_working

    def insert_card(self, card):
        self._card = card

    def card_inside(self):
        return self._card

    def check_level_of_cash(self) -> int:
        return self._cash_level

    def fill_cash(self, inserted_cash):
        if inserted_cash > 0:
            self._cash_level += inserted_cash

    def withdraw(self, wanted_cash):
        self._cash_level -= wanted_cash
        return wanted_cash
