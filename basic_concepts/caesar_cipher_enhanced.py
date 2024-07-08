# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 20:24:59 2024

@author: Kasia

asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25 )
prints out the encoded text.
"""
code_point_of_Z = 90
code_point_of_A = 65
code_point_of_z = 122
code_point_of_a = 97

def user_input_for_encryption():
    sentence = input("Write a sentence to be encrypted ")
    
    state = True
    while state:
        try:
            number = int(input('Write a number for the shift '))
            if(number < 1 or number > 25): 
                print("I need a number between 1 and 25. Try again1")
                continue
            state = False
        except:    
            print("I need a number between 1 and 25. Try again")
            continue   
    
    return (sentence, number)
    
def caesar_cipher(sentence, caesar_shift):
    
    cipher = ''
    
    
    for char in sentence:
        
        if char.isspace() or not char.isalpha():
            cipher +=char
        elif char.isupper():
            char = ord(char) + caesar_shift
            if(char > code_point_of_Z): 
                char = char - (code_point_of_Z - code_point_of_A) - 1
            cipher += chr(char)  
        elif char.islower():
            char = ord(char) + caesar_shift
            
            if(char > code_point_of_z): 
                char = char - (code_point_of_z - code_point_of_a) - 1
            cipher += chr(char)  
      
        
    return cipher


user_input = user_input_for_encryption()
sentence = user_input[0]
caesar_shift = user_input[1]
print(caesar_cipher(sentence, caesar_shift))




