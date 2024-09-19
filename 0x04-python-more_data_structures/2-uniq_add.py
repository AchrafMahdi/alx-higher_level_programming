#!/usr/bin/python3
def uniq_add(my_list):
    unique_sum = 0
    unique_set = set()

    for element in my_list:
        if element not in unique_set:
            unique_sum += element
            unique_set.add(element)

    return unique_sum
