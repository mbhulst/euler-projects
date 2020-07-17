# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# E.g., the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
# exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
# two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
# written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
# this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# Find all abundant numbers below 28123:

abundant_numbers = []

for number in range(28123):
    sum_divisors = 0
    for divisor in range(1, int(number/2 + 1)):
        if number % divisor == 0:
            sum_divisors += divisor
    if sum_divisors > number:
        abundant_numbers.append(number)
print(len(abundant_numbers))

# Determine all the sums of these numbers:

sum_abundant_numbers = []

for abundant_number in range(len(abundant_numbers)):
    for summator in range(abundant_number, len(abundant_numbers)):
        possible = abundant_numbers[abundant_number] + abundant_numbers[summator]
        if possible <= 28123:
            sum_abundant_numbers.append(abundant_numbers[abundant_number] + abundant_numbers[summator])
print(len(sum_abundant_numbers))


# Check which are not in sum_abundant_numbers

sums = set(sum_abundant_numbers)

answer = 0
for number in range(1, 28123):
    yes_or_no = number in sums
    if yes_or_no is False:
        answer += number

print(answer)
