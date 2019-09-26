# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

numbers_all = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
               'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
len_all = []

for number_i in range(1, len(numbers_all)):
    len_number = len(numbers_all[number_i])
    print(numbers_all[number_i], len_number)
    len_all.append(len_number)

number_xx_all = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred']
number_x_all = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for number_xx in range(2, 10):
    for number_x in range(0, 10):
        len_number = len(number_xx_all[number_xx]) + len(number_x_all[number_x])
        print(number_xx_all[number_xx], number_x_all[number_x], len_number)
        len_all.append(len_number)
        numbers_all.append(number_xx_all[number_xx] + number_x_all[number_x])

number_xxx_all = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number_xxx_extra = len('hundredand')
len_total = sum(len_all)

for number_xxx in range(1, 10):
    len_total = len_total + sum(len_all) + \
        99 * (len(number_xxx_all[number_xxx]) + len('hundredand')) + \
        1 * (len(number_xxx_all[number_xxx]) + len('hundred'))
    print(number_xxx, len_total)

print(len_total + len('onethousand'))
