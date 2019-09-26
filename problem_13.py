# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import numpy as np
data = np.genfromtxt("problem_13_matrix.txt")

sum_numbers = 0

for i in range(100):
    sum_numbers += data[i]

print(sum_numbers)
