

from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):

    def test_add_number(self):

        res = calc.add(5, 7)
        self.assertEquals(res, 12)


    def test_multiply_number(self):

        res = calc.multiply(5, 2)
        self.assertEquals(res, 10)