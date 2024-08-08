# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 20:52:04 2024

@author: Kasia
"""
class Timer:
    
    __ok = 5
    
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        
        if self.__hours < 10:
            print_hour = '0' + str(self.__hours)
        else: print_hour = str(self.__hours)
        
        if self.__minutes < 10:
            print_minutes = '0' + str(self.__minutes)
        else: print_minutes = str(self.__minutes)
        
        if self.__seconds < 10:
             print_seconds = '0' + str(self.__seconds)   
        else: print_seconds = str(self.__seconds) 
            
        return print_hour + ":" + print_minutes + ":" + print_seconds  
            
    def next_second(self):
        
        self.__seconds += 1
        
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes +=1
            
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours +=1
                
                if self.__hours == 24:
                    self.__hours = 0
            
        
                    

    def prev_second(self):
       
        self.__seconds -= 1
        
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes -=1
            
            if self.__minutes == -1:
                self.__minutes = 59
                self.__hours -=1
                
                if self.__hours == -1:
                    self.__hours = 23
            


timer = Timer(23, 59, 59)
print('first', timer.__dict__)

timer.__seconds = 22
print(timer.__seconds)
print(timer._Timer__seconds)
print('second', timer.__dict__)
#del timer._Timer__seconds

print(hasattr(timer, '_Timer__seconds'))
print(hasattr(timer, '__seconds'))
print(timer._Timer__ok)
print(hasattr(timer, '_Timer__ok'))
print(hasattr(timer, '__ok'))

print('third', timer.__dict__)

timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)