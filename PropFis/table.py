import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress

# Sample data
data = {
    'x': [546.1e-9, 433.9e-9, 404.7e-9, 365.0e-9, 312.6e-9, 253.5e-9],
    'y': [0.455, 1.021, 1.225, 1.608, 2.149, 3.070]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate inverse of x (handling potential division by zero)
df['x_inv'] = 1 / df['x'].where(df['x'] != 0, other=float('inf'))

# Prepare data for plotting (original x and transformed x_inv)
x = df['x'].tolist()
x_inv = df['x_inv'].tolist()
y = df['y'].tolist()

slope, intercept, r_value, p_value, std_err = linregress(x_inv, y)

# Function for the fitted line
def linear_func(x):
    return slope * x + intercept

# Generate x-values for the fitted line plot 
x_fit = x_inv  # Or customize the range

# Calculate corresponding y-values
y_fit = [linear_func(x) for x in x_fit]

# Plotting
plt.plot(x, y, 'o', label='Data (y vs x)')
plt.plot(x_inv, y, 'o', label='Data (y vs 1/x)')
plt.plot(x_fit, y_fit, '--', label='Linear Fit')
# Customize the plot 
plt.xlabel('f Hz')
plt.ylabel('E (eV)')
plt.title('E x f')
plt.legend()
plt.grid(True)  # Add gridlines for better readability

plt.show()