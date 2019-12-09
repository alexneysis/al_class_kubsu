import numpy as np
import matplotlib.pyplot as plt
from . import config

X = config.x_public
y = config.y_public

for d, sample in enumerate(X):
    # Plot the negative samples
    if d < 2:
        plt.scatter(sample[0], sample[1], s=120, marker='_', linewidths=2)
    # Plot the positive samples
    else:
        plt.scatter(sample[0], sample[1], s=120, marker='+', linewidths=2)

# Print a possible hyperplane, that is seperating the two classes.
# From site
# plt.plot([-2, 6], [6, 0.5])

# Private
plt.plot([0, 7], [0, 7])
plt.show()
