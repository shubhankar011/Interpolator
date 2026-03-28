import matplotlib.pyplot as plt
import numpy as np

# Your square root approximation method
def approx_sqrt(x):
    a = int(np.sqrt(x))
    a2, b2 = a*a, (a+1)*(a+1)
    if a2 == x: return float(a)
    return a + (x - a2) / (b2 - a2)

x_vals = np.arange(1, 2001)
errors = [abs(np.sqrt(x) - approx_sqrt(x)) for x in x_vals]

plt.plot(x_vals, errors, color='red')
plt.title("Error Analysis of Linear Interpolation")
plt.xlabel("Number (x)")
plt.ylabel("Absolute Error")
plt.savefig('sqrt_error_plot.png')