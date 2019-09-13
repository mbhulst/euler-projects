# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

num = 20
max_answer = int(1E9)
range_end = num + 1
answer = 0
remainder = 0

for answer in range(num, max_answer, num):
    remainder = 0
    for i in range(1, range_end):
        remainder = remainder + (answer % i)
    if remainder == 0:
        break
#print(remainder)
print("The smallest positive number that is evenly divisible by {} is {}." .format(num, answer))
