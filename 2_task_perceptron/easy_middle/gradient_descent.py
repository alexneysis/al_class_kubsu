import matplotlib.pyplot as plt
import numpy as np

def perceptron_sgd_plot(X, Y):
    '''
    train perceptron and plot the total loss in each epoch.

    :param X: data samples
    :param Y: data labels
    :return: weight vector as a numpy array
    '''
    w = np.zeros(len(X[0]))
    eta = 1
    n = 30
    errors = []

    for t in range(n):
        total_error = 0
        for i, x in enumerate(X):
            if (np.dot(X[i], w) * Y[i]) <= 0:
                total_error += (np.dot(X[i], w) * Y[i])
                w = w + eta * X[i] * Y[i]
        errors.append(total_error * -1)

    plt.plot(errors)
    plt.xlabel('Epoch')
    plt.ylabel('Total Loss')
    plt.show()

    return w


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

print(perceptron_sgd_plot(x_public, y_public))
# print(perceptron_sgd_plot(x_private, y_private))
