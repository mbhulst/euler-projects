# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from
# top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
# a 15K text file containing a triangle with one-hundred rows.

filename = "problem_67_matrix.txt"
with open(filename, 'r') as f:
    data = f.read()
rows = data.split("\n")
triangle = [[int(y) for y in x.split(" ")] for x in rows]

triangle_sum = [[triangle[0][0]]]

for row in range(1, len(triangle)):
    triangle_sum_row = []
    for column in range(len(triangle[row])):
        sum_new_1 = 0
        sum_new_2 = 0
        if column-1 >= 0:
            sum_new_1 = triangle[row][column] + triangle_sum[row-1][column-1]
        if column < len(triangle[row])-1:
            sum_new_2 = triangle[row][column] + triangle_sum[row-1][column]
        triangle_sum_row.append(max(sum_new_1, sum_new_2))
    triangle_sum.append(triangle_sum_row)

print(triangle_sum)

print(max(triangle_sum[-1]))
