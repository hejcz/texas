import unittest
from unittest.mock import MagicMock

from game import Game


class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.send_to_single = MagicMock()
        self.send_to_all = MagicMock()
        self.game = Game(self.send_to_all, self.send_to_single)

    def test_raise(self):
        self.game.raise_money(2, 20)
        self.send_to_single.assert_called_with(2, "ok")

    def test_raise_2(self):
        self.game.raise_money(2, 20)
        self.send_to_single.assert_called_with(1, "ok")


if __name__ == '__main__':
    unittest.main()
