
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 08:44:47 2024

@author: Kasia
"""

input_file_name = 'C:\\Users\Felipe\Documents\one.txt' # dziala bez eskejpwania \ ??
output_file_name = 'C:\\Users\\Felipe\\Documents\\two2.txt' # nie dziala bez eskejpwania \ ??

from os import strerror


alphabet_dict2 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
            
try:
    stream = open(input_file_name, 'r')
    for line in stream:
        for char in line:
            char = char.lower()
            if char in alphabet_dict2:
                value = alphabet_dict2[char] 
                value +=1
                alphabet_dict2[char] = value
                
    stream = open(output_file_name, 'w')
    for char in sorted(alphabet_dict2.keys(), key = lambda x : alphabet_dict2[x], reverse = True):  
        if alphabet_dict2[char] != 0:
            stream.write(char + '->' + str(alphabet_dict2[char]) + '\n')
    stream.close()               
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


           
       
        
         
        