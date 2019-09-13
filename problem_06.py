# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# define range
number_range = range(1, 101)

# calculate sum of squares
square_number_range = [x**2 for x in number_range]
sum_square_number_range = sum(square_number_range)

# calculate square of sum
sum_number_range = sum(number_range)
square_sum_number_range = sum_number_range**2

# calculate difference
difference = square_sum_number_range - sum_square_number_range

print("The difference between the sum of the squares of the first one hundred natural numbers "
      "and the square of the sum is {}." .format(difference))
