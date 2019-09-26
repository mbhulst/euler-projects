# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# options = 0

# for grid_size in range(1, 10):
#    options += 2

grid_number = 20
options_total_half = 1
options_column = 1
for i in range(2, grid_number+1):
    options_column = options_column + grid_number-1
    options_total_half = options_total_half + options_column
    print(i, options_column, options_total_half, options_total_half*2)

# not solved yet!