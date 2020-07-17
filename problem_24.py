# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
# 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

permutations = []
digits = range(0, 10)

while len(permutations) < 1000001:
    for digit_1 in digits:
        digits_remaining_2 = [i for i in digits if i != digit_1]
        for digit_2 in digits_remaining_2:
            digits_remaining_3 = [i for i in digits_remaining_2 if i != digit_2]
            for digit_3 in digits_remaining_3:
                digits_remaining_4 = [i for i in digits_remaining_3 if i != digit_3]
                for digit_4 in digits_remaining_4:
                    digits_remaining_5 = [i for i in digits_remaining_4 if i != digit_4]
                    for digit_5 in digits_remaining_5:
                        digits_remaining_6 = [i for i in digits_remaining_5 if i != digit_5]
                        for digit_6 in digits_remaining_6:
                            digits_remaining_7 = [i for i in digits_remaining_6 if i != digit_6]
                            for digit_7 in digits_remaining_7:
                                digits_remaining_8 = [i for i in digits_remaining_7 if i != digit_7]
                                for digit_8 in digits_remaining_8:
                                    digits_remaining_9 = [i for i in digits_remaining_8 if i != digit_8]
                                    for digit_9 in digits_remaining_9:
                                        digits_remaining_10 = [i for i in digits_remaining_9 if i != digit_9]
                                        for digit_10 in digits_remaining_10:
                                            permutations.append(digit_1*1000000000 + digit_2*100000000 + digit_3*10000000 +
                                                                digit_4*1000000 + digit_5*100000 + digit_6*10000 +
                                                                digit_7*1000 + digit_8*100 + digit_9*10 + digit_10)
print(permutations)
print(permutations[999999])
