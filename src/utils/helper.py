# Module for binary search
from bisect import bisect_left

def binary_search(a, x):
    elem = bisect_left(a, x)
    # check the data
    status = False
    if elem != len(a) and a[elem] == x:
        status = True
    return status