#!/usr/bin/env python
import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        return cross_entropy_error(softmax(self.predict(x)), t)

if __name__ == "__main__":
    x = np.array([0.6, 0.9])
    t = np.array([0, 0, 1])
    net = simpleNet()

    f = lambda w: net.loss(x, t)
    print(numerical_gradient(f, net.W))
