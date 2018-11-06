from unittest import TestCase
from cheers import Cheers


class TestCheers(TestCase):

    def test_upper(self):
        c = Cheers()
        self.assertEqual(c.all_caps("banana"), 'BANANA')
