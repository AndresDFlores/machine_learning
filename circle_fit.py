# import numpy as np
# import matplotlib.pyplot as plt

# #  https://stackoverflow.com/questions/73362793/how-to-scatter-plot-two-concentric-circles-with-numpy-and-matplotlib

# r = [5, 10]
# angle = np.linspace(0, 2 * np.pi, 100)

# X = [
#     r[0] * np.cos(angle)
#     ]

# Y = [
#     r[0] * np.sin(angle)
#     ]


# plt.axis('equal');
# plt.scatter(X[0], Y[0], c='purple')

# avg_x = np.mean(X)
# avg_y = np.mean(Y)

# plt.plot(avg_x, avg_y, 'ro')
# plt.show()


import numpy as np
import matplotlib.pyplot as plt


def get_linear_training_matrices(x, y):

    X_ = [[1, val] for val in x]
    Y_ = [[val] for val in y]

    return X_, Y_



def get_parameters(X_,Y_):

    #  calculate the model parameters
    A1 = np.linalg.inv(np.transpose(X_)@X_)
    A2 = np.transpose(X_)@Y_
    A = A1@A2  # in linear regression, A = [[b], [m]]

    return A



def get_regression(X_, Y_, A):

    Y_Calc = X_@A

    return Y_Calc



def get_cost_function(Y_, Y_Calc):
    errors = Y_Calc-Y_

    squared_errors = [err**2 for err in errors]
    sum_squared_errors = sum(squared_errors)
    J = (1/len(Y_))*sum_squared_errors

    return J



def plot_regression(x, y, Y_Calc, r2=None):
    #  this produces a 2-D plot of the train data and test data
    plot, ax = plt.subplots()

    ax.plot(x, y, 'bo')
    ax.plot(x, Y_Calc, 'r')
    ax.grid(True)

    if r2:
        ax.set_title(f'R2: {r2}')

    plt.show()



def main(x_data, y_data):

    X_, Y_ = get_linear_training_matrices(x_data, y_data)
    A = get_parameters(X_, Y_)
    Y_Calc = get_regression(X_, Y_, A)
    J = get_cost_function(Y_, Y_Calc)

    plot_regression(x_data, y_data, Y_Calc, J)



r = [5, 10]
angle = np.linspace(0, 2 * np.pi, 100)

x_data = [r[0] * np.cos(angle)]
y_data = [r[0] * np.sin(angle)]

main(*x_data, *y_data)

