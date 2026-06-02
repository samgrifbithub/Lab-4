from bst import *
import sys
import unittest
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10**9)


@dataclass(frozen=True)
class Point2D:
    x: float
    y: float


class BSTTests(unittest.TestCase):

    def test_strings(self):
        def comes_before(a: Any, b: Any) -> bool:
            return a < b

        tree = BSTWithComesBefore(comes_before, None)

        tree = insert(tree, "hi")
        tree = insert(tree, "hello")
        tree = insert(tree, "good afternoon")

        self.assertTrue(lookup(tree, "hi"))
        self.assertTrue(lookup(tree, "hello"))
        self.assertTrue(lookup(tree, "good afternoon"))
        self.assertFalse(lookup(tree, "bye"))

        tree = delete(tree, "hi")

        self.assertFalse(lookup(tree, "hi"))
        self.assertTrue(lookup(tree, "hello"))
        self.assertTrue(lookup(tree, "good afternoon"))

    def test_points(self):
        def comes_before(a: Any, b: Any) -> bool:
            return (a.x * a.x + a.y * a.y) < (b.x * b.x + b.y * b.y)

        p1 = Point2D(1, 0)
        p2 = Point2D(2, 0)
        p3 = Point2D(3, 0)

        t = BSTWithComesBefore(comes_before, None)

        t = insert(t, p2)
        t = insert(t, p1)

        self.assertTrue(lookup(t, p1))
        self.assertTrue(lookup(t, p2))
        self.assertFalse(lookup(t, p3))

        t = delete(t, p2)

        self.assertFalse(lookup(t, p2))

    def test_reverse_numbers(self):
        def comes_before(a: Any, b: Any) -> bool:
            return a > b

        t = BSTWithComesBefore(comes_before, None)

        t = insert(t, 10)
        t = insert(t, 9)

        self.assertTrue(lookup(t, 10))
        self.assertTrue(lookup(t, 9))
        self.assertFalse(lookup(t, 8))

        t = delete(t, 10)

        self.assertFalse(lookup(t, 10))


if __name__ == '__main__':
    unittest.main()

# test_strings checks that string values can be inserted, found, and deleted alphabetically.
# test_points checks that Point2D values are ordered by distance from the origin.
# test_reverse_numbers checks that integers work when the order is reversed.
