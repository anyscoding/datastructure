import unittest


def gap_insert_sort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        cur = alist[i]
        index = i
        while index >= gap and alist[index-gap] > cur:
            alist[index] = alist[index-gap]
            index -= gap
        alist[index] = cur


def shell_sort(alist):
    sub_count = len(alist)//2
    while sub_count > 0:
        for start in range(sub_count):
            gap_insert_sort(alist, start, sub_count)
        sub_count = sub_count // 2

    return alist


class TestShellSort(unittest.TestCase):
    def test_shell_sort(self):
        tcs = [
            ([54, 26, 93, 17, 77, 31, 44, 55, 20], [17, 20, 26, 31, 44, 54, 55, 77, 93]),
            ([99, 98, 97, 96, 95, 94, 93, 92, 91], [91, 92, 93, 94, 95, 96, 97, 98, 99]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
        ]
        for tc in tcs:
            self.assertEqual(tc[1], shell_sort(tc[0]))