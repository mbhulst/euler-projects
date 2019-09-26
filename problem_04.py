# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

product_list = []
c_string = 0
palindromes = []

# find all products of two 3-digit numbers
for a in range(1, 1000):
    for b in range(1, 1000):
        product = a * b
        product_list.append(product)

# find all palindromes amongst these products
for c in product_list:
    c_string = str(c)
    if c_string == c_string[::-1]:
        palindromes.append(c)

# find largest palindrome
palindromes_max = max(palindromes)

print("The largest palindrome made from the product of two 3-digit numbers is {}." .format(palindromes_max))
