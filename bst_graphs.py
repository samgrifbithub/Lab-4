from bst import *
import sys
import unittest
from typing import *
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt
import numpy as np
import random
import time

sys.setrecursionlimit(10**9)


TREES_PER_RUN: int = int(1e4)


# Create a random BST with n random float values.
def random_tree(n: int) -> BSTWithComesBefore:
    def comes_before(a: Any, b: Any) -> bool:
        return a < b

    t = BSTWithComesBefore(comes_before, None)

    for i in range(n):
        t = insert(t, random.random())

    return t


# Find the height of a BST.
def height(t: BST) -> int:
    if t is None:
        return 0

    left_height = height(t.left)
    right_height = height(t.right)

    if left_height > right_height:
        return 1 + left_height

    return 1 + right_height


# if its slow change
n_max_height = 20
n_max_insert = 20

# Graph #1: Height of random BST as N increases.
x_values = np.linspace(1, n_max_height, 50)
x_values = [int(x) for x in x_values]

y_values = []

for n in x_values:
    total_height = 0

    for i in range(TREES_PER_RUN):
        t = random_tree(n)
        total_height += height(t.t)

    average_height = total_height / TREES_PER_RUN
    y_values.append(average_height)

plt.plot(x_values, y_values, label="Average Height")
plt.xlabel("N")
plt.ylabel("Average Height")
plt.title("Height of Random BST as N Increases")
plt.grid(True)
plt.legend()
plt.show()


# Graph #2: Insert time as N increases.
x_values = np.linspace(1, n_max_insert, 50)
x_values = [int(x) for x in x_values]

y_values = []

for n in x_values:
    total_time = 0.0

    for i in range(TREES_PER_RUN):
        t = random_tree(n)

        start = time.perf_counter()
        insert(t, random.random())
        end = time.perf_counter()

        total_time += end - start

    average_time = total_time / TREES_PER_RUN
    y_values.append(average_time)

plt.plot(x_values, y_values, label="Average Insert Time")
plt.xlabel("N")
plt.ylabel("Average Insert Time")
plt.title("Insert Time as N Increases")
plt.grid(True)
plt.legend()
plt.show()
