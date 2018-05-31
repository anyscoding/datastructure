import unittest


def bubble_sort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(0, i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        tcs = [
            ([54, 26, 93, 17, 77, 31, 44, 55, 20], [17, 20, 26, 31, 44, 54, 55, 77, 93]),
            ([99, 98, 97, 96, 95, 94, 93, 92, 91], [91, 92, 93, 94, 95, 96, 97, 98, 99]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
        ]
        for tc in tcs:
            self.assertEqual(tc[1], bubble_sort(tc[0]))