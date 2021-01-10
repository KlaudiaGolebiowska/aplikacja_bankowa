import unittest

from mock import MagicMock

from app.card import Card

from app.account import Account


class TestCard(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._account_amount = 100
        cls._account_owner = "Klaudia Golebiowska"
        cls.account = Account(cls._account_amount, cls._account_owner)
        cls.account.get_balance = MagicMock(return_value=200)
        cls.account.get_owner = MagicMock(return_value="Klaudia Golebiowska")

    def setUp(self) -> None:
        # Given
        self.pin = 1234
        self.card = Card(account=self.account, pin=self.pin)

    # Metoda Card.check_pin powinna sprawdzić czy pin jest poprawny.
    def test_whenValidPinIsChecked_thenTrueIsReturned(self):
        # When
        is_pin_valid = self.card.check_pin(pin=self.pin)

        # Then
        self.assertTrue(is_pin_valid)

    # Metoda Card.check_pin powinna sprawdzić czy pin jest poprawny.
    def test_whenInvalidPinIsChecked_thenFalseIsReturned(self):
        # Given
        invalid_pin = 0000

        # When
        is_pin_valid = self.card.check_pin(pin=invalid_pin)

        # Then
        self.assertFalse(is_pin_valid)

    # Odwołanie się do Card.owner powinno zwracać imie i nazwisko właściciela konta.
    def test_whenCardOwnerIsCalled_AccountOwnerIsReturned(self):
        # When
        found_owner = self.card.owner()

        # Then
        self.assertEqual(self._account_owner, found_owner)

    # Metoda Card.get_account powinna zwrócić konto do którego karta jest „podpięta”
    def test_whenAccountIsCalledFromCard_properAccountIsReturned(self):
        # When
        found_account = self.card.get_account()

        # Then
        self.assertEqual(self.account, found_account)
        self.assertEqual(self.account, found_account)