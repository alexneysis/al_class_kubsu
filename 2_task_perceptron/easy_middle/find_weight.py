import numpy as np

x_public = np.array([
    [-2, 4, -1],
    [4, 1, -1],
    [1, 6, -1],
    [2, 4, -1],
    [6, 2, -1],

])
y_public = np.array([-1, -1, 1, 1, 1])
eta_public = 1

# Private dataset
x_private = np.array([
    [4, 3, -1],
    [7, 3, -1],
    [1, 6.5, -1],
    [2.6, 4.5, -1],
    [2.4, 6.5, -1],
    [4, 6.5, -1],
    [2.5, 8.5, -1],

])
y_private = np.array([-1, -1, 1, 1, 1, 1, 1])

eta_private = 0.1

def perceptron_sgd(X, Y):
    w = np.zeros(len(X[0]))
    eta = 1
    epochs = 10

    for t in range(epochs):
        for i, x in enumerate(X):
            if (np.dot(X[i], w) * Y[i]) <= 0:
                w = w + eta * X[i] * Y[i]

    return w


w = perceptron_sgd(x_public, y_public)
# w = perceptron_sgd(x_private, y_private)
print(w)
