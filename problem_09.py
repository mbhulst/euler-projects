# A Pythagorean triplet is a set of three natural numbers, a < b < c, fow which, a^2 + b^2 = c^2.
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

end_range = 500
find_sum = 1000

for a in range(end_range):
    for b in range(a+1, end_range):
        c = (a**2 + b**2)**0.5
        if a + b + c == find_sum:
            print(int(a*b*c))
            break
