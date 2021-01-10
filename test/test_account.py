import unittest

from app.account import Account


class TestAccount(unittest.TestCase):

    def setUp(self) -> None:
        self.owner = "Klaudia Gołębiowska"
        self.balance = 100
        self.account = Account(amount=self.balance, owner=self.owner)

    # Metoda Account.get_owner powinna zwracać Imię  i nazwisko właściciela.
    def test_whenAccountOwnerCalled_thenOwnerIsReturned(self):
        # When
        owner_received = self.account.get_owner()

        # Then
        self.assertEqual(self.owner, owner_received)

    # Metoda Account.get_balance powinna zwracać aktualny stan konta.
    def test_whenAccountBalanceCalled_thenActualBalanceReturned(self):
        # When
        balance_received = self.account.get_balance()

        # Then
        self.assertEqual(self.balance, balance_received)

    # Metoda Account.get_number powinna zwracać numer konta. Numer konta powinien być nadawny przez system.
    def test_whenAccountNumberIsCalled_thenAccountNumberIsReturned(self):
        # Given
        account2 = Account(amount=0, owner="X")

        # When

        number_received_1 = self.account.get_number()
        number_received_2 = account2.get_number()

        # Then
        self.assertIsInstance(number_received_1, int)
        self.assertNotEqual(number_received_1, number_received_2)

    # Metoda Account.transfer powinna zmieniać stan konta o podaną kwotę
    def test_whenTransferIsMade_thenBalanceIsChanged(self):
        # Given
        money_to_transfer = 50

        # When
        self.account.transfer(money_to_transfer)

        # Then
        self.assertEqual(self.balance + money_to_transfer, self.account.get_balance())

    # Metoda Account.transfer nie powinna pozwolić zmienić balance na ujemny.
    def test_whenNegativeTransferIsMadeFromEmptyAccount_thenTransferIsNotMade(self):
        # Given
        money_to_transfer = -150

        # When
        self.account.transfer(money_to_transfer)

        # Then
        self.assertEqual(self.balance, self.account.get_balance())