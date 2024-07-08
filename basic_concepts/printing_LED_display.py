# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:10:51 2024

@author: Kasia
"""
jedynka = ['  *','  *','  *','  *','  *']
dwojka = ['***','  *','***','*  ','***']
trojka = ['***','  *','***','  *','***']
czworka = ['* *','* *','***','  *','  *']

numbers = {
    '1' : jedynka,
    '2' : dwojka,
    '3' : trojka,
    '4' : czworka
    }

def print_seven_digits_display(word):
 
    global numbers
    
    i = 0
    state = True
    while state:
        for char in word:
            char = numbers.get(char)
            print(char[i],' ',  end ='')
            continue
        i +=1
        if i == 5: state = False
        print('')
       
        
number = '4321'    

print_seven_digits_display(number)