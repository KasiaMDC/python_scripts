# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:46:52 2024

@author: Kasia
"""

  
def my_split(sentence):
    list1 = []  
    
    if sentence.isspace():
        return []
    elif len(sentence) == 0:
        return []
        
    sentence = sentence.strip(" ")
    
    while " " in sentence:
        end_index = sentence.find(" ")
        word = sentence[0 : end_index] 
        sentence = sentence[end_index + 1 : ]
        list1.append(word)
    else: list1.append(sentence)   

    return list1

sentence = "To be or not to be, that is the question"

print(my_split(sentence))