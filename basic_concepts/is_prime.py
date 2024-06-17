# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 09:27:50 2024

@author: Kasia
"""

def is_prime(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True
 
for i in range(1, 20):
    if is_prime(i + 1):
    	print(i + 1, end=" ")
print()