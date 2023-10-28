
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


is_leap_year = False
weekdays = {"saturday": 0, "sunday": 1, "monday": 2, "tuesday": 3, "wednesday": 4, "thursday": 5, "friday": 6}
months = {"january": 31, "february": 28, "march": 31, "april": 30, "may": 31, "june": 30, "july": 31, "august": 31, "september": 30, "october": 31, "november": 30, "december": 31}
month_days_not_leap_year = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_days_leap_year = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
curr_month_list = month_days_not_leap_year
first_january_1901_day = (2 + 365) % 7

curr_day = first_january_1901_day
counter = 0

for i in range(1901, 2001):
    if leap_year(i):
        curr_month_list = month_days_leap_year
    else:
        curr_month_list = month_days_not_leap_year
    for j in range(1, len(months) + 1):
        curr_day = (curr_day + curr_month_list[j]) % 7
        if curr_day == 1:
            counter += 1

print(counter)
