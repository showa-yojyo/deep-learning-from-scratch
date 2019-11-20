#!/usr/bin/env python
import numpy as np
import matplotlib.pylab as plt
from sigmoid import sigmoid
from step_function import step_function

if __name__ == "__main__":
    x = np.arange(-5.0, 5.0, 0.1)
    y1 = sigmoid(x)
    y2 = step_function(x)

    plt.plot(x, y1)
    plt.plot(x, y2, 'k--')
    plt.ylim(-0.1, 1.1) #図で描画するy軸の範囲を指定
    plt.show()
