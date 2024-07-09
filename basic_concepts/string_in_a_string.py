# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:48:58 2024

@author: Kasia

are the characters comprising the first string hidden inside the second string
"""

def is_text_in(text, text_in):
    text = text.upper()
    text_in = text_in.upper()
    index = 0
    char_multiple_times_in_text = []
    
    for char in text_in:
        how_many_times_in_text = text_in.count(char)
        
        if char in char_multiple_times_in_text:
            continue
        
        if how_many_times_in_text == 1:
            if char in text:
                continue
            else: 
                return print("No")
        else:
            char_multiple_times_in_text.append(char)
            
            for i in range(how_many_times_in_text):
                if char in text[index:]:
                    next_index = text[index:].index(char)
                    index += next_index + 1
                    continue
                else: 
                    return print("No")
            
    return print("Yes")
        
a = 'donu'
b = 'Nabucodonosor'

is_text_in(b,a)
       
    