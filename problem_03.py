# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

num = 600851475143
prime_factors = []
sum_prime_factors = 1
store_prime_factor = 0

# find all prime factors
for a in range(1, num):
    if num % a == 0 and a != 1:
        prime_factors.append(a)

        # check which have to be multiplied to obtain the number
        if sum_prime_factors < num:
            store_prime_factor = a
            sum_prime_factors = sum_prime_factors * a
        else:
            print("The largest prime factor of the number {} is {}." .format(num, store_prime_factor))
            break
