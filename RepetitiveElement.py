"""
This function get a iterable and delete repetitive elements of it .
"""

from collections import OrderedDict
def unique_in_order(iterable):
    return list(OrderedDict.fromkeys(list(iterable)))


print(unique_in_order("aadmfl"))




