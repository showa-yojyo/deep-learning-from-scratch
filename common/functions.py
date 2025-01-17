#!/usr/bin/env python
import numpy as np


def identity_function(x):
    return x


def step_function(x):
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_grad(x):
    sigx = sigmoid(x)
    return (1.0 - sigx) * sigx


def relu(x):
    return np.maximum(0, x)


def relu_grad(x):
    grad = np.zeros(x)
    grad[x>=0] = 1
    return grad


def softmax(x):
    x = np.asarray(x)
    if x.ndim == 2:
        x = x.T
        x -= np.max(x, axis=0)
        expx = np.exp(x)
        y = expx / np.sum(expx, axis=0)
        return y.T

    x -= np.max(x) # オーバーフロー対策
    expx = np.exp(x)
    return expx / np.sum(expx)


def sum_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)


def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # 教師データがone-hot-vectorの場合、正解ラベルのインデックスに変換
    if t.size == y.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


def softmax_loss(X, t):
    return cross_entropy_error(softmax(X), t)
