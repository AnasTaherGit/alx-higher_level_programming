#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_weight = 0
    total_weighted_score = 0
    for score, weight in my_list:
        total_weight += weight
        total_weighted_score += score * weight
    return total_weighted_score / total_weight
