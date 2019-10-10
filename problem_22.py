# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

with open('problem_22_names.txt', 'r') as file:         # import names as string
    names = file.read()
names_list = names.split('","')                         # split into list of separate names
names_list.sort()                                       # sort alphabetically

name_score = 0
for name in range(len(names_list)):                     # iterate over list of names
    letter_score = 0
    for letter_number in range(len(names_list[name])):  # iterate over letters in a name
        letter = names_list[name][letter_number]        # find which letter it is
        letter_score += (ord(letter) - 64)              # determine the worth of that letter (using build in dictionary)
    name_score += (name + 1) * letter_score             # indexes start at 0, but the first name = 1

print('The total of all the name scores in the file is {}.' .format(name_score))
