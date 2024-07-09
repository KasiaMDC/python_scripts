# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:19:13 2024

@author: Kasia
"""

def user_input():
    state = True
    
    while state:
            birth_date = input("Write your birth date (DDMMYYYY): ")
            if len(birth_date) != 8:
                print("Please use system DDMMYYYY")
                continue
            if not birth_date.isnumeric():
                print("Please use system DDMMYYYY, only digits")
                continue
            state = False
            
    return birth_date


def digit_of_life(birth_date):
    digit_of_life = birth_date.replace('0','')
    
    while len(digit_of_life) != 1:
        sum_of_digits = 0
        digits = list(digit_of_life)
        
        for i in range(len(digits)):
            sum_of_digits += int(digits[i])
            
        digit_of_life = str(sum_of_digits)
        digit_of_life = digit_of_life.replace('0','')
        
        
    return digit_of_life
  
  
birth = user_input()
digit = digit_of_life(birth)
print(digit)

