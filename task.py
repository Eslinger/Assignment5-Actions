import math


def firstrun():
    return "success"


def circle(radius):
    area = math.pi * (radius**2)
    return area


def first_last(list):
    fandl = []
    fandl.append(list[0])
    fandl.append(list[len(list)-1])
    return fandl


def date_days(date1, date2):
    days = (date2 - date1).days
    return days
