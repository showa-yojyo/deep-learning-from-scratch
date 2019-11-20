#!/usr/bin/env python
from itertools import product
from nand_gate import NAND

def AND(a, b):
    return NAND(NAND(a, b), NAND(a, b))

if __name__ == '__main__':
    for x in product((0, 1), (0, 1)):
        print(f"{x} -> {AND(*x)}")
