import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Calculate y values
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label='sin(x)', color='blue')
plt.plot(x, y_cos, label='cos(x)', color='green')

# For tan(x), limit the y-values to avoid vertical asymptotes in plot
y_tan = np.tan(x)
y_tan[np.abs(y_tan) > 10] = np.nan  # Avoid drawing extreme values
plt.plot(x, y_tan, label='tan(x)', color='red')

# Add labels, legend, and grid
plt.title('Graphs of sin(x), cos(x), and tan(x)')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.grid(True)
plt.legend()
plt.ylim(-2, 2)  # Set y-limit for better visibility
plt.show()
