import unittest


def binary_search(alist, item):
    if alist:
        middle = len(alist) // 2
        if alist[middle] == item:
            return True
        elif alist[middle] < item:
            return binary_search(alist[middle+1:], item)
        else:
            return binary_search(alist[:middle], item)
    else:
        return False


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        tcs = [
            (True, [0, 1, 2, 8, 13, 17, 19, 32, 42], 8),
            (True, [0, 1, 2, 8, 13, 17, 19, 32, 42], 42),
            (True, [0, 1, 2, 8, 13, 17, 19, 32, 42], 0),
            (False, [0, 1, 2, 8, 13, 17, 19, 32, 42], 7),
            (False, [0, 1, 2, 8, 13, 17, 19, 32, 42], 50),
        ]
        for tc in tcs:
            self.assertEqual(tc[0], binary_search(*tc[1:]))