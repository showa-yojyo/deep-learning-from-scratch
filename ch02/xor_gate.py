#!/usr/bin/env python
from itertools import product
from and_gate import AND
from or_gate import OR
from nand_gate import NAND

def XOR(x1, x2):
    return AND(NAND(x1, x2), OR(x1, x2))

if __name__ == '__main__':
    for x in product((0, 1), (0, 1)):
        print(f"{x} -> {XOR(*x)}")
