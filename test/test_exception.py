import unittest


class MyException(Exception):
    pass


class BrokenClass:

    def __init__(self):
        raise MyException("This class is broken")

class TestClass(unittest.TestCase):

    def test_is_class_broken(self):
        with self.assertRaises(MyException):
            broken_class = BrokenClass()
