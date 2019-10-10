# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

divisors_all = [0, 1]
# number = 284
for number in range(2, 10001):

    # check the number of divisors of each number
    divisors = [0]
    for possible_divisor in range(1, number//2 + 1):
        if number % possible_divisor == 0:
            divisors.append(possible_divisor)
    divisors_all.append(sum(divisors))
print(divisors_all)

sum_amicable_num = 0

for number in range(2, 10001):
    yes_or_no = number in divisors_all
    indexes = []
    if yes_or_no is True:
        indexes = [i for i, x in enumerate(divisors_all) if x == number]
    for index in range(len(indexes)):
        if divisors_all[number] == indexes[index] and number != indexes[index]:
            print(number, indexes[index])
            sum_amicable_num += number
print('The sum of all the amicable numbers under 10000 is {}.' .format(sum_amicable_num))
