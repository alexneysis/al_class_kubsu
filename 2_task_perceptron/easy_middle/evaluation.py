import matplotlib.pyplot as plt
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


def perceptron_sgd_plot(X, Y):
    '''
    train perceptron and plot the total loss in each epoch.

    :param X: data samples
    :param Y: data labels
    :return: weight vector as a numpy array
    '''
    w = np.zeros(len(X[0]))
    eta = eta_public
    n = 30
    errors = []

    for t in range(n):
        total_error = 0
        for i, x in enumerate(X):
            if (np.dot(X[i], w) * Y[i]) <= 0:
                total_error += (np.dot(X[i], w) * Y[i])
                w = w + eta * X[i] * Y[i]
        errors.append(total_error * -1)

    print(w)
    return w


for d, sample in enumerate(x_private):
    # Plot the negative samples
    if d < 2:
        plt.scatter(sample[0], sample[1], s=120, marker='_', linewidths=2, color='black')
    # Plot the positive samples
    else:
        plt.scatter(sample[0], sample[1], s=120, marker='+', linewidths=2, color='purple')

# Add our test samples
plt.scatter(5, 4, s=120, marker='+', linewidths=2, color='green')
plt.scatter(0, 1, s=120, marker='_', linewidths=2, color='blue')

# Print the hyperplane calculated by perceptron_sgd()
w = perceptron_sgd_plot(x_private, x_private)
x2 = [w[0], w[1], -w[1], w[0]]
x3 = [w[0], w[1], w[1], -w[0]]

x2x3 = np.array([x2, x3])
X, Y, U, V = zip(*x2x3)
ax = plt.gca()
ax.quiver(X, Y, U, V, scale=1, color='blue')
plt.show()
