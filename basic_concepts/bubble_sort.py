# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def swap_places(list):
    a = list[0]
    list[0] = list[1]
    list[1] = a
    
    return list

def bubble_sort(list):
    n = len(list)
    swapped = True

    while swapped == True:
        swapped = False
        for i in range(1,n):
            if(list[i-1]<list[i]):
                swapped_list = swap_places([list[i-1],list[i]])
                list[i-1] = swapped_list[0]
                list[i] = swapped_list[1]
                swapped = True
                
    return list


list = [90, 67, 4, 0, 0, 34, 76]

print(bubble_sort(list))

