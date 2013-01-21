def days_difference(day1, day2):
    return (day2 - day1)


def get_weekday(weekday, num_days):
    return (weekday + (num_days % 7)) % 7


def get_birthday_weekday(weekday, yearday, birthday):
    return get_weekday(weekday, days_difference(yearday, birthday))

