# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    # if month in (1, 3, 5, 7, 8, 10, 12)  this is to use a
    if month == 1 or month == 3 or month == 5 or month == 7 \
            or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            if is_leap_year(year):
                return 29
            else:
                return 28
        else:
            return 30


def next_day(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < days_in_month(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def date_is_before(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
        year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def days_between_dates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    # program defensively! Add an assertion if the input is not valid!
    # assert (date_is_before(year1, month1, day1, year2, month2, day2))
    assert not date_is_before(year2, month2, day2, year1, month1, day1)
    days = 0

    while date_is_before(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = next_day(year1, month1, day1)
        days += 1

    return days


def test():
    # test with 30-day months:
    assert days_between_dates(2013, 1, 1, 2013, 1, 1) == 0
    assert days_between_dates(2013, 1, 1, 2013, 1, 2) == 1
    assert next_day(2013, 1, 1) == (2013, 1, 2)
    assert next_day(2013, 4, 30) == (2013, 5, 1)
    assert next_day(2012, 12, 31) == (2013, 1, 1)
    assert next_day(2013, 2, 28) == (2013, 3, 1)
    assert next_day(2013, 9, 30) == (2013, 10, 1)
    assert days_between_dates(2013, 1, 1, 2014, 1, 1) == 365
    print('Test case passed for the stubs')

    test_cases = [((2012, 9, 30, 2012, 10, 30), 30),
                  ((2012, 1, 1, 2013, 1, 1), 365),
                  ((2012, 9, 1, 2012, 9, 4), 3)]

    for (args, answer) in test_cases:
        result = days_between_dates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()
