# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

num = 4
prime_factors = [2, 3]

# find all prime factors
while num < 2000000:
    num = num + 1
    for i in range(2, int((num**0.5)+1)):
        if (num % i) == 0:
            break
    else:
        prime_factors.append(num)

print(prime_factors)
print("The sum of all the primes below two million is {}." .format(sum(prime_factors)))
