import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar


# Parameters
x0 = 0.5
y0 = 0.5
num_iterations = 1000
r_values = [2 + 0.001 * i for i in range(2001)]
all_results = []

# Function to generate the logistic map
def logistic_map(r, x0, y0, num_iterations):    
    results = []
    x = x0
    y = y0
    for _ in range(num_iterations):
        z = r * (x*y)*(1-x)*(1-y)
        results.append([x, y, z])
        all_results.append([x, y, z,r])
        x = r * x * (1 - x)
        y = r * y * (1 - y)
    return results

z_values = []
for r in r_values:
    results = logistic_map(r, x0,y0, num_iterations)
    z_values.append([result[2] for result in results])

z_values = np.array(z_values)

# Save the structured array as a CSV file
np.savetxt('array_data.csv', all_results, delimiter=',')

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(r_values, z_values, ',k', alpha=0.25)
plt.title('Logistic Map: r vs. z')
plt.xlabel('r')
plt.ylabel('z')
plt.grid(True)

# Save the plot to a file
plt.savefig('plot.png')