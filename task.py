import math


def firstrun():
    return "success"


def circle_area(radius):
    area = radius * (math.pi ** 2)
    return area


def first_and_last(some_list):
    return "first: " + str(some_list[0]) + ", last: " + str(some_list[len(some_list)-1])
