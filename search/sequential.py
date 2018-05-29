import unittest


def sequential_search(alist, item):
    for i in alist:
        if i == item:
            return True
    return False


class TestSequentialSearch(unittest.TestCase):
    def test_sequential(self):
        tcs = [
            (False, [1, 2, 32, 8, 17, 19, 42, 13, 0], 3),
            (True, [1, 2, 32, 8, 17, 19, 42, 13, 0], 17)
        ]
        for tc in tcs:
            self.assertEqual(tc[0], sequential_search(*tc[1:]))