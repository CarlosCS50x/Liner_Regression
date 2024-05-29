Linear Regression with Gradient Descent
This project implements a linear regression algorithm using gradient descent to find the best-fit line for a given set of data points. The algorithm is visualized with an animated plot showing how the line evolves over iterations.

Description
The script performs linear regression using gradient descent to minimize the mean squared error (MSE) between the predicted and actual values of the data points. The resulting best-fit line is animated to show the progression of the line through the iterations of gradient descent.

Files
gradient_descent.py: Main script that performs linear regression, computes errors, updates parameters using gradient descent, and animates the best-fit line.
data.csv: CSV file containing the data points (x, y) used for linear regression.
Dependencies
Python 3.x
numpy: For numerical operations
matplotlib: For plotting and animation
Install the dependencies using pip:

sh
Copiar código
pip install numpy matplotlib
Usage
Place your data points in a file named data.csv in the same directory as the script. The CSV file should have two columns without headers, representing the x and y values of the data points.

Run the script:

sh
Copiar código
python gradient_descent.py
The script will perform gradient descent and display an animated plot showing the evolution of the best-fit line over the iterations.

Function Descriptions
compute_error_for_line_given_points(b, m, points)
Calculates the mean squared error for a given line defined by y = mx + b.

Parameters:

b (float): y-intercept of the line.
m (float): Slope of the line.
points (ndarray): Array of data points.
Returns:

(float): Mean squared error.
step_gradient(b_current, m_current, points, learningRate)
Performs a single step of gradient descent to update the parameters b and m.

Parameters:

b_current (float): Current y-intercept.
m_current (float): Current slope.
points (ndarray): Array of data points.
learningRate (float): Learning rate for gradient descent.
Returns:

(float, float): Updated values of b and m.
gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations)
Runs the gradient descent algorithm for a specified number of iterations.

Parameters:

points (ndarray): Array of data points.
starting_b (float): Initial y-intercept.
starting_m (float): Initial slope.
learning_rate (float): Learning rate for gradient descent.
num_iterations (int): Number of iterations to run gradient descent.
Returns:

(float, float, list, list): Final values of b and m, and histories of b and m values.
run()
Main function to execute the linear regression and animate the results.

Loads data from data.csv.
Initializes parameters and runs gradient descent.
Animates the evolution of the best-fit line.
Important Comments on the Code
Ensure data.csv is present in the same directory as the script or adjust the file path accordingly.
The learning rate and number of iterations can be adjusted to optimize the gradient descent performance for different datasets.
The animated plot helps visualize the convergence process, making it easier to understand how gradient descent works.
Example
An example data.csv:

Copiar código
1.0, 2.0
2.0, 2.8
3.0, 3.6
4.0, 4.5
5.0, 5.1
Running the script will show the best-fit line gradually approaching the optimal solution through each iteration of gradient descent.
