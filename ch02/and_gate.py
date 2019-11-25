#!/usr/bin/env python
from itertools import product
import sys, os
sys.path.append(os.pardir)
from common.gates import AND

if __name__ == '__main__':
    for x in product((0, 1), (0, 1)):
        print(f"{x} -> {AND(*x)}")
