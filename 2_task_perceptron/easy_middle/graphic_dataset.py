import numpy as np
import matplotlib.pyplot as plt

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

# for d, sample in enumerate(x_private):
for d, sample in enumerate(x_public):
    # Plot the negative samples
    if d < 2:
        plt.scatter(sample[0], sample[1], s=120, marker='_', linewidths=2)
    # Plot the positive samples
    else:
        plt.scatter(sample[0], sample[1], s=120, marker='+', linewidths=2)

# Print a possible hyperplane, that is seperating the two classes.
# From site
plt.plot([-2, 6], [6, 0.5])

# Private
# plt.plot([0, 7], [0, 7])
plt.show()
