import numpy as np
import matplotlib.pyplot as plt

#  https://stackoverflow.com/questions/73362793/how-to-scatter-plot-two-concentric-circles-with-numpy-and-matplotlib

r = [5, 10]
angle = np.linspace(0, 2 * np.pi, 100)

X = [r[0] * np.cos(angle), r[1] * np.cos(angle)]
Y = [r[0] * np.sin(angle), r[1] * np.sin(angle)]

plt.axis('equal');
plt.scatter(X[0], Y[0], c='purple')
# plt.scatter(X[1], Y[1], c='yellow')



avg_x = np.mean(X)
avg_y = np.mean(Y)

# min_x = min(X)
# max_x = max(X)
# x_diam = max_x-min_x

# min_y = min(Y)
# max_y = max(Y)
# y_diam = max_y-min_y



plt.plot(avg_x, avg_y, 'ro')
plt.show()