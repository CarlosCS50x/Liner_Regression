import numpy as np
import matplotlib.pyplot as plt

# Function to compute error for a line given points
def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))

# Function to perform a single gradient descent step
def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return new_b, new_m

# Function to run gradient descent
def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for _ in range(num_iterations):
        b, m = step_gradient(b, m, np.array(points), learning_rate)
    return b, m

# Main function to run the regression
def run():
    points = np.genfromtxt("data.csv", delimiter=",")
    learning_rate = 0.0001
    initial_b = 0  # initial y-intercept guess
    initial_m = 0  # initial slope guess
    num_iterations = 4000
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))
    print("Running...")
    b, m = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points)))
    
    # Plotting the results
    x = points[:, 0]
    y = points[:, 1]
    plt.scatter(x, y, color='blue', label='Data Points')
    plt.plot(x, m * x + b, color='red', label='Best Fit Line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression Fit')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    run()
