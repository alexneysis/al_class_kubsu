import numpy as np
from . import config

X = config.x_public
y = config.y_public

def perceptron_sgd(X, Y):
    w = np.zeros(len(X[0]))
    eta = 1
    epochs = 10

    for t in range(epochs):
        for i, x in enumerate(X):
            if (np.dot(X[i], w) * Y[i]) <= 0:
                w = w + eta * X[i] * Y[i]

    return w


w = perceptron_sgd(X, y)
print(w)
