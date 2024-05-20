# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:37:32 2024

@author: Kasia
"""

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(6))