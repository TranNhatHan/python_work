import numpy as np
from scipy.optimize import minimize

# Define the area function to minimize (we use negative for maximization)
def area(W):
    return - (200 * W[0] - 2 * W[0]**2)

# Initial guess for the width (W)
initial_simplex = np.array([[0], [2], [3]])  # Three points in the initial simplex

# Perform optimization using Nelder-Mead method
result = minimize(area, initial_simplex[0], method='Nelder-Mead')

# Get the optimal width
optimal_width = result.x[0]
optimal_length = 200 - 2 * optimal_width
max_area = -result.fun  # Convert back to positive

print("Results using Nelder-Mead Method:")
print(f"Optimal Width: {optimal_width:.2f} m")
print(f"Optimal Length: {optimal_length:.2f} m")
print(f"Maximum Area: {max_area:.2f} m²")
