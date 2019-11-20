#!/usr/bin/env python
from itertools import product
import numpy as np


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    return 1 if np.sum(w*x) + b > 0 else 0

if __name__ == '__main__':
    for x in product((0, 1), (0, 1)):
        print(f"{x} -> {NAND(*x)}")
