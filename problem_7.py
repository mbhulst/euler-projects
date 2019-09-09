# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

num = 4
prime_factors = [2, 3]

# find all prime factors
while len(prime_factors) < 10002:
    num = num + 1
    for i in range(2, num//2):
        if (num % i) == 0:
            break
    else:
        prime_factors.append(num)

print("The 10001st prime number is {}." .format(prime_factors[10000]))
