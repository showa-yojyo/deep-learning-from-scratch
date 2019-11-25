# gates.py

import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    return 1 if np.sum(w*x) + b > 0 else 0

def AND(a, b):
    return NAND(NAND(a, b), NAND(a, b))

def OR(a, b):
    return NAND(NAND(a, a), NAND(b, b))

def XOR(x1, x2):
    return AND(NAND(x1, x2), OR(x1, x2))
