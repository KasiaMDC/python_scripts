
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 08:44:47 2024

@author: Kasia
"""

input_file_name = 'C:\\Users\Felipe\Documents\one.txt'
alphabet_dict = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

from os import strerror

try:
    stream = open(input_file_name, 'r')
    content = stream.read()
    for char in content:
        char = char.lower()
        if char in alphabet_dict:
            value = alphabet_dict[char] 
            value +=1
            alphabet_dict[char] = value
    stream.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
            
for char in alphabet_dict:
    if alphabet_dict[char] != 0:
        print(char, '->', alphabet_dict[char])

print()        
print('inny sposob')
print('_'*20)

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
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
            
for char in alphabet_dict2:
    if alphabet_dict2[char] != 0:
        print(char, '->', alphabet_dict2[char])        
        