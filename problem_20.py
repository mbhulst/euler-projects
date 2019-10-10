# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

product = 100

for number in reversed(range(1, product)):
    product = product * number

print(product)

digits = str(product)
sum_digits = 0

for i in range(len(digits)):
    sum_digits = sum_digits + int(digits[i])

print("The sum of the digits in the number 100! is {}." .format(sum_digits))
