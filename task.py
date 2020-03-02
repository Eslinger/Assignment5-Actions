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
