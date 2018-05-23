import random
import unittest
from stack.stack import Stack


class BitConversion(object):
    def __init__(self, dec):
        self.dec = dec
        self.stack = Stack()
        self.base = "0123456789abcdef"

    def conversion(self, bit):
        if bit not in (2, 8, 16):
            raise ValueError("bit must in (2, 8, 16)")
        while self.dec > 0:
            remainder = self.dec % bit
            self.stack.push(self.base[remainder])
            self.dec = self.dec // bit

        result = []
        while not self.stack.is_empty():
            result.append(self.stack.pop())

        return "".join(result)


class TestBitConversion(unittest.TestCase):
    def test_conversion_bit_2(self):
        test = random.randint(1, 1000000)
        bc = BitConversion(test)
        self.assertEqual(bin(test)[2:], bc.conversion(2))

    def test_conversion_bit_8(self):
        test = random.randint(1, 1000000)
        bc = BitConversion(test)
        self.assertEqual(oct(test)[2:], bc.conversion(8))

    def test_conversion_bit_16(self):
        test = random.randint(1, 1000000)
        bc = BitConversion(test)
        self.assertEqual(hex(test)[2:], bc.conversion(16))

    def test_conversion_bit_unknown(self):
        test = random.randint(1, 1000000)
        bit = random.randint(1, 100)
        while bit in (2, 8, 16):
            bit = random.randint(1, 100)
        bc = BitConversion(test)
        self.assertRaises(ValueError, bc.conversion, bit)


if __name__ == '__main__':
    unittest.main()
