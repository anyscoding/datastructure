import unittest

from dequeue.dequeue import Dequeue


def palindrome_check(astring):
    dq = Dequeue()

    for i in astring:
        dq.add_real(i)

    while dq.size() > 1:
        if dq.remove_front() != dq.remove_real():
            return False
    return True


class TestPalindrome(unittest.TestCase):
    def test_check(self):
        tcs = {
            "abccba": True,
            "abcba": True,
            "fghjkllk": False,
            "fthjkaknknnabjhac": False
        }
        for k, v in tcs.items():
            self.assertEqual(palindrome_check(k), v)