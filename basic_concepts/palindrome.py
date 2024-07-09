# -*- coding: utf-8 -*-
"""
Created on Fri May 31 21:05:57 2024

@author: Kasia
"""

def is_palindrome(sentence):
    
    if not len(sentence):
        print("It's not a palindrome")
        return
   
    sentence = sentence.replace(' ', '').upper()
    sentence = list(sentence)
    
    i = 0
    for i in range(len(sentence)//2):
        if(sentence[0 + i] == sentence[-1 - i]):
            i +=1
            continue
        else:
            print("It's not a palindrome")
            return
    
    print("It's a palindrome")
    
def is_palindrome2(sentence):
    
    if not len(sentence):
        print("It's not a palindrome")
        return
    
    sentence = sentence.replace(' ', '').upper()
    
    
    

sentence = "Eleven animals I slam in a net"

is_palindrome(sentence)