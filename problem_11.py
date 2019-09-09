# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?

import numpy as np
data = np.genfromtxt("problem_11_matrix.txt", delimiter=" ")

# find greatest product horizontally
max_product_hor = 0
for i in range(0, len(data[0, :])-3):
    for j in range(0, len(data[0, :])-3):
        product_hor = data[j, i] * data[j, i+1] * data[j, i+2] * data[j, i+3]
        if product_hor > max_product_hor:
            max_product_hor = product_hor
# print("The greatest product horizontally is {}. " .format(max_product_hor))

# find greatest product vertically
max_product_ver = 0
for i in range(0, len(data[:, 0])-3):
    for j in range(0, len(data[:, 0])-3):
        product_ver = data[i, j] * data[i+1, j] * data[i+2, j] * data[i+3, j]
        if product_ver > max_product_ver:
            max_product_ver = product_ver
# print("The greatest product vertically is {}. " .format(max_product_ver))

# find greatest product diagonally
max_product_dia = 0
for j in range(0, len(data[0, :])-3):
    for i in range(0, len(data[0, :])-3):
        product_dia = data[i, j] * data[i+1, j+1] * data[i+2, j+2] * data[i+3, j+3]
        if product_dia > max_product_dia:
            max_product_dia = product_dia
# print("The greatest product diagonally is {}. " .format(max_product_dia))

max_product_dia_2 = 0
for j in range(0, len(data[0, :])-3):
    for i in range(2, len(data[0, :])-1):
        product_dia_2 = data[i, j] * data[i-1, j+1] * data[i-2, j+2] * data[i-3, j+3]
        if product_dia_2 > max_product_dia_2:
            max_product_dia_2 = product_dia_2
# print("The greatest product diagonally is {}. " .format(max_product_dia_2))

max_value = max(max_product_hor, max_product_ver, max_product_dia, max_product_dia_2)

print("The greatest product in the same direction is {}." .format(int(max_value)))
