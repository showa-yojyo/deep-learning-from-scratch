# test_mnist.py

from unittest import TestCase

import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import (
    load_mnist, train_num, test_num, img_dim, img_size)

class MnistTestCase(TestCase):

    ndigits = 10
    ntrain = train_num
    ntest = test_num
    unflatten_size = img_dim
    flatten_size = img_size

    def test_load_mnist_flaten(self):
        train, test = load_mnist(flatten=True)
        self.assertEqual(train[0].shape, (self.ntrain, self.flatten_size))
        self.assertEqual(test[0].shape, (self.ntest, self.flatten_size))

        train, test = load_mnist(flatten=False)
        self.assertEqual(train[0].shape, (self.ntrain, *self.unflatten_size))
        self.assertEqual(test[0].shape, (self.ntest, *self.unflatten_size))

    def test_load_mnist_normalize(self):
        traint, testt = load_mnist(normalize=True)
        for i in (traint[0], testt[0]):
            self.assertEqual(i.dtype, np.float32)
            self.assertTrue(((0 <= i) & (i <= 1.0)).all())

        trainf, testf = load_mnist(normalize=False)
        for i in (trainf[0], testf[0]):
            self.assertEqual(i.dtype, np.uint8)

    def test_load_mnist_one_hot_label(self):
        traint, testt = load_mnist(one_hot_label=True)
        self.assertEqual(traint[1].shape, (self.ntrain, self.ndigits))
        self.assertEqual(testt[1].shape, (self.ntest, self.ndigits))
        for i in (traint[1], testt[1]):
            self.assertEqual(i.dtype, np.bool)
            self.assertTrue(((i == 0) | (i == 1)).all())

        trainf, testf = load_mnist(one_hot_label=False)
        self.assertEqual(trainf[1].shape, (self.ntrain,))
        self.assertEqual(testf[1].shape, (self.ntest,))
        for i in (trainf[1], testf[1]):
            self.assertEqual(i.dtype, np.uint8)
            self.assertTrue(((i != 0) & (i != 1)).any())
