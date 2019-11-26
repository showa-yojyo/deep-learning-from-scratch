#!/usr/bin/env python
"""test_functions.py
"""
from unittest import (TestCase, main)
import numpy as np
import sys, os
sys.path.append(os.pardir)
from common.functions import (
    sigmoid, step_function, relu, softmax)

class FunctionsTestCase(TestCase):

    epsilon = np.nextafter(0, 1)

    def test_sigmoid(self):
        # x -> 1/(1 + exp(-x))
        self.assertAlmostEqual(sigmoid(0), .5)
        self.assertAlmostEqual(sigmoid(-np.inf), 0)
        self.assertAlmostEqual(sigmoid(np.inf), 1)
        x = 42
        self.assertAlmostEqual(sigmoid(x) - .5, sigmoid(-x) + .5)

    def test_step(self):
        # step_function returns np.array(dtype=int)
        self.assertEqual(step_function(-np.inf), 0)
        self.assertEqual(step_function(0), 0)
        self.assertEqual(step_function(self.epsilon), 1)
        self.assertEqual(step_function(np.inf), 1)

    def test_relu(self):
        # x -> max(0, x)
        self.assertAlmostEqual(relu(-np.inf), 0)
        self.assertEqual(relu(-42), 0)
        self.assertEqual(relu(0), 0)
        self.assertEqual(relu(self.epsilon), self.epsilon)
        self.assertEqual(relu(42), 42)
        self.assertEqual(relu(np.inf), np.inf)

    def test_softmax(self):
        # y_i = exp(x_i)/sum_i^n(exp(x_i))

        # Use the code in p. 70
        self.assertTrue(np.allclose(
            softmax([0.3, 2.9, 4.0]), np.array(
                [0.01821127, 0.24519181, 0.73659691])))

        # softmax must not return NAN
        self.assertFalse(np.isnan(softmax([1010, 1000, 990]).any()))

if __name__ == '__main__':
    main()
