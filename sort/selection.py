import unittest


def selection_sort(alist):
    for i in range(len(alist)-1, 0, -1):
        max_index = 0
        for j in range(0, i+1):
            if alist[j] > alist[max_index]:
                max_index = j
        alist[i], alist[max_index] = alist[max_index], alist[i]

    return alist


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        tcs = [
            ([54, 26, 93, 17, 77, 31, 44, 55, 20], [17, 20, 26, 31, 44, 54, 55, 77, 93]),
            ([99, 98, 97, 96, 95, 94, 93, 92, 91], [91, 92, 93, 94, 95, 96, 97, 98, 99]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
        ]
        for tc in tcs:
            self.assertEqual(tc[1], selection_sort(tc[0]))
