import unittest

from my_queue.queue import Queue


def hostPotato(nlist, num):
    q = Queue()
    for n in nlist:
        q.enqueue(n)
    while q.size() > 1:
        for i in range(1, num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()


class TestHotPotato(unittest.TestCase):
    def test_hot_potato(self):
        tcs = [
            ("Kent", ["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7),
            ("Bill", ["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 3),
            ("Bill", ["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 5)
        ]

        for i in tcs:
            self.assertEqual(i[0], hostPotato(*i[1:]))
