# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:17:33 2024

@author: Kasia
"""

def read_int(prompt, min, max):
    
    state = True
    while state:
        try: 
            user_input = input(prompt)
            user_input = int(user_input)
            assert user_input >= min and user_input <= max
            state = False
        except ValueError:
            print("wrong input")
        except AssertionError:
            print("the value is not within permitted range (",  min, "..", max, ")")

    return user_input  


v = read_int( 'Enter a number from -10 to 10: ', -10, 10)

print("The number is:", v)

