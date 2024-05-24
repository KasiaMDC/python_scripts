# -*- coding: utf-8 -*-
"""
Created on Mon May 20 13:53:15 2024

@author: Kasia
"""

""""Napisz prosty program, który wykona się zadaną przez użytkownika liczbę razy. Z każdym uruchomieniem pętli wyświetli informacje:
– czy liczba jest wielokrotnością 3
– czy liczba jest wielkorotnością 4
– wyświtli „hurra” jeżeli liczba dzieli się zarówno przez 3 jak i 4
– wyświetli gwiazdkę, jeśli żaden z powyższych warunków nie jest spełniony"""

import random

def is_multiple_three(n):
    if n % 3 == 0:
        return True
    else:
        return False
        
def is_multiple_four(n):
    if n % 4 == 0:
        return True
    else:
        return False
    
def user_input():
   number_of_times = int(input('How many times should I do that?'))  
   
   return number_of_times
   
def solution(number_of_times):
    
    star = '*'
    
    for i in range(1,number_of_times+1):
        
        random_number = random.randrange(0, 100, 1)
        
        if (is_multiple_three(random_number)):
            print(str(random_number) +  ' is a multiple of three')
        elif (is_multiple_four(random_number)):
            print(str(random_number) + ' is a multiple of four')
        elif ((is_multiple_four(random_number)) and (is_multiple_three(random_number))):
             print('huraaa')
        else:
            print(star)
            if(star < len(50)):
                star = star + '*'

def main():
    input_of_user = user_input()
    solution(input_of_user)
    
if __name__ == '__main__':
    main()



        
