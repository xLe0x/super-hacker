# 4.​ Check if a given year is a leap year.


def is_leap(year: int):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


print(is_leap(1900))
print(is_leap(2025))
