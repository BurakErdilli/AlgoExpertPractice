# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 21:38:22 2024

@author: Burak
"""


def binarySerach(array, target):
    found = False
    k = 0
    l = len(array)

    while l != k:
        index = (l+k)//2
        if array[index] == target:
            return index
        elif array[index] > target:
            l = index-1
        elif array[index] < target:
            k = index+1
    return -1


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 6

index = binarySerach(array, target)
