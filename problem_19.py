# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.

# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

days = 1  # 1 Jan 1900 is day number 1 (Monday), so 0 is Sunday!
first_of_the_months = [days]  # store the day number (after 1 Jan 1900) of each first of the month


for year in range(1900, 2001):
    for month in range(1, 13): # calculate for each year how long each monht takes
        if month == 2:                                                      # Feb
            if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:       # Feb: regular leap year
                first_of_the_months.append(days + 29)
                days += 29
            elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:     # Feb: leap year during century
                first_of_the_months.append(days + 28)
                days += 28
            elif year % 4 == 0 and year % 400 == 0:                         # Feb: leap year during century
                first_of_the_months.append(days + 29)
                days += 29
            else:                                                           # Feb: other years, no leap year
                first_of_the_months.append(days + 28)
                days += 28
        elif month == 4 or month == 6 or month == 9 or month == 11:         # Apr, Jun, Sep, Nov
            first_of_the_months.append(days + 30)
            days += 30
        else:                                                               # Jan, Mar, May, Jul, Aug, Oct, Dec
            first_of_the_months.append(days + 31)
            days += 31

sundays = 0
for day in range(len(first_of_the_months) - 1):     # The for loop also calculates 1 Jan 2001, so -1
    if (first_of_the_months[day]) % 7 == 0:         # Which first of the months are Sundays, because 0 = Sunday
        sundays += 1
print('During the twentieth century {} Sundays fell on the first of the month.' .format(sundays - 2))
# 1900 had 2 Sundays on the first of the month, so -2
