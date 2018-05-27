import unittest

from stack.stack import Stack


def infix2postfix(infix):
    s = Stack()
    l = []

    linfix = infix.split()
    priority = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    for i in linfix:
        if i == "(":
            s.push(i)
        elif i == ")":
            t = s.pop()
            while not s.is_empty() and t != "(":
                l.append(t)
                t = s.pop()
        elif i in "+-*/":
            while not s.is_empty() and priority[s.peek()] >= priority[i]:
                l.append(s.pop())
            s.push(i)
        else:
            l.append(i)
    while not s.is_empty():
        l.append(s.pop())

    return " ".join(l)


class TestInfix2Postfix(unittest.TestCase):
    def test_infix2postfix(self):
        tcs = {
            "A * B + C * D": "A B * C D * +",
            "( A + B ) * C": "A B + C *",
            "A + B * C": "A B C * +"
        }
        for k, v in tcs.items():
            self.assertEqual(infix2postfix(k), v)