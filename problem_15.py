# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

import numpy as np

grid_size = 20

grid = np.ones((grid_size + 1, grid_size + 1))

for x in range(1, grid_size + 1):
    for y in range(1, grid_size + 1):
        grid[x, y] = int(grid[x - 1, y] + grid[x, y - 1])

print("There are {} routes from the top left corner to the bottom right corner in a {}x{} grid."
      .format(int(grid[grid_size, grid_size]), grid_size, grid_size))
