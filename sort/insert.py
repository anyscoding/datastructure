import unittest


def insert_sort(alist):
    for i in range(1, len(alist)):
        cur = alist[i]
        index = i
        while index > 0 and alist[index-1] > cur:
            alist[index] = alist[index-1]
            index -= 1
        alist[index] = cur
    return alist


class TestInsertSort(unittest.TestCase):
    def test_insert_sort(self):
        tcs = [
            ([54, 26, 93, 17, 77, 31, 44, 55, 20], [17, 20, 26, 31, 44, 54, 55, 77, 93]),
            ([99, 98, 97, 96, 95, 94, 93, 92, 91], [91, 92, 93, 94, 95, 96, 97, 98, 99]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
        ]
        for tc in tcs:
            self.assertEqual(tc[1], insert_sort(tc[0]))
