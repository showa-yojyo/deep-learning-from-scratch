#!/usr/bin/env python
from itertools import product
from nand_gate import NAND

def OR(a, b):
    return NAND(NAND(a, a), NAND(b, b))

if __name__ == '__main__':
    for x in product((0, 1), (0, 1)):
        print(f"{x} -> {OR(*x)}")
