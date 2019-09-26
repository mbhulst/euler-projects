# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

digits = str(2**1000)
sum_digits = 0

for i in range(len(digits)):
    sum_digits = sum_digits + int(digits[i])
    print(sum_digits)

print(sum_digits)