#!/usr/bin/env python
"""test_gates.py
"""
from unittest import (TestCase, main)
import sys, os
sys.path.append(os.pardir)
from common.gates import (NAND, AND, OR, XOR)

class GatesTestCase(TestCase):

    def test_NAND(self):
        self.assertEqual(NAND(0, 0), 1)
        self.assertEqual(NAND(0, 1), 1)
        self.assertEqual(NAND(1, 0), 1)
        self.assertEqual(NAND(1, 1), 0)

    def test_AND(self):
        self.assertEqual(AND(0, 0), 0)
        self.assertEqual(AND(0, 1), 0)
        self.assertEqual(AND(1, 0), 0)
        self.assertEqual(AND(1, 1), 1)

    def test_OR(self):
        self.assertEqual(OR(0, 0), 0)
        self.assertEqual(OR(0, 1), 1)
        self.assertEqual(OR(1, 0), 1)
        self.assertEqual(OR(1, 1), 1)

    def test_XOR(self):
        self.assertEqual(XOR(0, 0), 0)
        self.assertEqual(XOR(0, 1), 1)
        self.assertEqual(XOR(1, 0), 1)
        self.assertEqual(XOR(1, 1), 0)

if __name__ == '__main__':
    main()
