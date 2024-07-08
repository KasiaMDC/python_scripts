# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 20:24:59 2024

@author: Kasia

using the following assumptions:

it accepts Latin letters only (note: the Romans used neither whitespaces nor digits)
all letters of the message are in upper case (note: the Romans knew only capitals)
"""
code_point_of_Z = 90
code_point_of_A = 65
caesar_shift = 1

def caesar_cipher(sentence):
    
    sentence = sentence.replace(" ","").upper()
    print(sentence)
    cipher = ''
    
    for char in sentence:
        char = ord(char) + caesar_shift
                
        if(char > code_point_of_Z): 
            char = char - (code_point_of_Z - code_point_of_A) - 1
            
        
        cipher += chr(char)
        
    return cipher

def caesar_decipher(sentence):
    cipher = ''
    
    for char in sentence:
        char = ord(char) - caesar_shift
        if char < code_point_of_A:
            char = char + (code_point_of_Z - code_point_of_A) + 1
            print(char)
        cipher += chr(char)
    
    return cipher


sentence = 'AVE CAESArZ'

sentence = caesar_cipher(sentence)
print(sentence)
print(caesar_decipher(sentence))



