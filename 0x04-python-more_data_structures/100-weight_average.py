#!/usr/bin/python3
def weight_average(my_list=[]):
    total_weight, avg = 0, 0
    for i in list(map(lambda x: x[1], my_list)):
        total_weight += i
    for i in list(map(lambda x: x[0] * x[1] / total_weight, my_list)):
        avg += i
    return (avg)
