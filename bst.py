import sys
import unittest
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10**9)


BST = Optional["BSTNode"]


@dataclass
class BSTNode:
    value: Any
    left: BST = None
    right: BST = None


@dataclass(frozen=True)
class BSTWithComesBefore:
    comes_before: Callable[[Any, Any], bool]
    t: BST


# Return True if value is in the tree.
def lookup(tree_with_cb: BSTWithComesBefore, value: Any) -> bool:
    return lookup_bst(
        tree_with_cb.comes_before,
        tree_with_cb.t,
        value
    )


# Recursively search a BST for a value.
def lookup_bst(
    comes_before: Callable[[Any, Any], bool],
    t: BST,
    value: Any
) -> bool:
    if t is None:
        return False

    if (
        not comes_before(value, t.value)
        and not comes_before(t.value, value)
    ):
        return True

    if comes_before(value, t.value):
        return lookup_bst(comes_before, t.left, value)

    return lookup_bst(comes_before, t.right, value)


# Return a new BSTWithComesBefore with value inserted.
def insert(tree_with_cb: BSTWithComesBefore, value: Any) -> BSTWithComesBefore:
    new_tree = insert_bst(
        tree_with_cb.comes_before,
        tree_with_cb.t,
        value
    )

    return BSTWithComesBefore(
        tree_with_cb.comes_before,
        new_tree
    )


# Recursively insert a value into a BST.
def insert_bst(
    comes_before: Callable[[Any, Any], bool],
    t: BST,
    value: Any
) -> BST:
    if t is None:
        return BSTNode(value)

    if (
        not comes_before(value, t.value)
        and not comes_before(t.value, value)
    ):
        return t

    if comes_before(value, t.value):
        t.left = insert_bst(comes_before, t.left, value)
        return t

    t.right = insert_bst(comes_before, t.right, value)
    return t


# Return a new BSTWithComesBefore with value deleted.
def delete(tree_with_cb: BSTWithComesBefore, value: Any) -> BSTWithComesBefore:
    new_tree = delete_bst(
        tree_with_cb.comes_before,
        tree_with_cb.t,
        value
    )

    return BSTWithComesBefore(
        tree_with_cb.comes_before,
        new_tree
    )


# Recursively delete a value from a BST.
def delete_bst(
    comes_before: Callable[[Any, Any], bool],
    t: BST,
    value: Any
) -> BST:
    if t is None:
        return None

    if comes_before(value, t.value):
        t.left = delete_bst(comes_before, t.left, value)
        return t

    if comes_before(t.value, value):
        t.right = delete_bst(comes_before, t.right, value)
        return t

    if t.left is None:
        return t.right

    if t.right is None:
        return t.left

    replacement = t.right

    while replacement.left is not None:
        replacement = replacement.left

    t.value = replacement.value

    t.right = delete_bst(
        comes_before,
        t.right,
        replacement.value
    )

    return t


# lookup checks whether a value is in the BST.
# lookup_bst recursively searches the actual tree.
# insert adds a value to a BSTWithComesBefore.
# insert_bst recursively inserts into the actual tree and skips duplicates.
# delete removes a value from a BSTWithComesBefore.
# delete_bst recursively removes from the actual tree and reconnects the tree correctly.
