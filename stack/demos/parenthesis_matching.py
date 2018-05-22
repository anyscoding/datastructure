import unittest
from stack.stack import Stack


class ParenthesisMatching(object):
    def __init__(self, parenthesis):
        self.parenthesis = parenthesis
        self.stack = Stack()

    def is_match(self):
        maps = {")": "(", "]": "[", "}": "{"}
        for p in self.parenthesis:
            if p in "([{":
                self.stack.push(p)
            elif p in ")]}":
                if self.stack.is_empty():
                    return False
                else:
                    top = self.stack.pop()
                    if maps[p] != top:
                        return False
        return True


class TestParenthesisMatching(unittest.TestCase):
    def test_is_match(self):
        tcs = {
            "{ [ [ ] ] }": True,
            "{ { { } } } [ ( [ [ ] ] ) ]": True,
            "{ { ( [ ] [ ] ) } ( ) }": True,
            "[ [ { { ( ( ) ) } } ] ]": True,
            "[ ] [ ] [ ] ( ) { }": True,
            "self.assertEqual(p.is_match(), v)": True,
            "( [ ) ]": False,
            "( ( ( ) ] ) )": False,
            "[ { ( ) ]": False,
            "{ } { { } } { { [ ( ) } } }": False
        }
        for k, v in tcs.items():
            p = ParenthesisMatching(k)
            self.assertEqual(p.is_match(), v)


if __name__ == '__main__':
    unittest.main()
