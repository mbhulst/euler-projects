# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

multiples = []
num = 1000

# list natural numbers below a certain number that are multiples of 3 or 5
for i in range(1, num):
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)

# calculate sum of these multiples
multiples_sum = sum(multiples)

print("The sum of all the multiples of 3 or 5 below {} is {}." .format(num, multiples_sum))
