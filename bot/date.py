import datetime as dt


def today_str():
    return '/'.join(list(reversed(str(dt.date.today()).split('-'))))


def ten_years_ago_str():
    return '/'.join(list(reversed(str(dt.date.today() - dt.timedelta(days=3650)).split('-'))))
