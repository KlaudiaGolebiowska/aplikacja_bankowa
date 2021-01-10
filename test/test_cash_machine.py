"""
Bankomat:
Czy można wypłacić pieniądze.
Czy łączy się z kontem.
Czy brak pieniędzy w bankomacie jest obsługiwany
Czy brak pieniędzy na koncie jest obsługiwany.
"""
import unittest

from parameterized import parameterized

from app.account import Account
from app.card import Card
from app.cash_machine import CashMachine


class TestCashMachine(unittest.TestCase):

    def test_whenCashMachineIsCreated_itWorks(self):
        # Given
        cash_machine = CashMachine()

        # When
        status_of_cash_machine = cash_machine.is_working()

        # Then
        self.assertTrue(status_of_cash_machine)

    def test_whenCardIsInserted_thenCashMachineIsAbleToReceiveIt(self):
        # Given
        account = Account(amount=1, owner="Owner of Card")
        card = Card(account=account, pin=1234)
        cash_machine = CashMachine()

        # When
        cash_machine.insert_card(card)
        inserted_card = cash_machine.card_inside()

        # Then
        self.assertEqual(card, inserted_card)

    def test_whenLevelOfCashIsChecked_thenItIsReturned(self):
        # Given
        level_of_cash = 10000
        cash_machine = CashMachine(start_cash=level_of_cash)

        # When
        found_level_of_cash = cash_machine.check_level_of_cash()

        # Then
        self.assertEqual(level_of_cash, found_level_of_cash)

    def test_whenLevelIsLow_thenThereIsPossibilityToAddCash(self):
        # Given
        start_cash = 100
        inserted_cash = 9900
        cash_machine = CashMachine(start_cash=start_cash)

        # When
        cash_machine.fill_cash(inserted_cash)
        found_level_of_cash = cash_machine.check_level_of_cash()

        # Then
        self.assertEqual(start_cash + inserted_cash, found_level_of_cash)

    def test_whenStartCashIsNotInt_thenRaiseValueError(self):
        with self.assertRaisesRegex(ValueError, "should be integer"):
            start_cash = "10000"
            cash_machine = CashMachine(start_cash=start_cash)

    @parameterized.expand([
        ["1_zloty", 1, 100],
        ["10_zloty", 10, 100],
        ["100_zloty", 100, 1000],
        ["1000_zloty", 1000, 10000],
        ["10000_zloty", 10000, 10000]
    ])
    def test_whenWantToWithdrawCash_thenCashIsReturned(self, name, wanted_cash, start_cash):
        # Given
        cash_machine = CashMachine(start_cash=start_cash)

        # When
        withdrawn_cash = cash_machine.withdraw(wanted_cash)
        cash_level = cash_machine.check_level_of_cash()

        # Then
        self.assertEqual(wanted_cash, withdrawn_cash)
        self.assertEqual(start_cash - wanted_cash, cash_level)