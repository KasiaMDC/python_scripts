# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 21:03:13 2024

@author: Kasia
"""

def is_anagram(first_text, second_text):
    
    if len(first_text) and len(second_text) == 0:
        print("this is not an anagram2")
        return
    
    first_text = first_text.replace(' ','').upper()
    second_text = second_text.replace(' ','').upper()
    
    first_text = list(first_text)
   # first_text = list(first_text).sort() -->nie mozna w jednej linii, wychodzi None
    first_text.sort()
    
    second_text = list(second_text)
    second_text.sort()
  
    
    
    if(str(first_text) == str(second_text)):
        print("this is an anagram")
    else:
        print("this is not an anagram")



    
first_text = 'rail safetyt' 
    
second_text = 'fairy tales'

is_anagram(first_text, second_text)
