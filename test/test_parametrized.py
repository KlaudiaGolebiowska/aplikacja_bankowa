import unittest

from app.cash_machine import CashMachine


class Test(unittest.TestCase):

    def test_one(self):
        with self.assertRaises(ValueError):
            int("XXX")

    def test_two(self):
        with self.assertRaisesRegex(ValueError, "literal"):
            int("XXX")

    def test_three(self):
        cash_machine = CashMachine()
        int(cash_machine)

import unittest

from parameterized import parameterized


class TestSequence(unittest.TestCase):
    @parameterized.expand([
        ["foo", "a", "a"],
        ["bar", "a", "b"],
        ["lee", "b", "b"],
        ["lee", "C", "b"],
    ])
    def test_sequence(self, name, a, b):
        self.assertEqual(a, b)
