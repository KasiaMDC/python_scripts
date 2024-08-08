# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:59:42 2024

@author: Kasia
"""

class WeekDayError(Exception):
    pass
	

class Weeker:
    
    __week_days = {
        'Mon' : 1,
        'Tue' : 2,
        'Wed' : 3,
        'Thu' : 4,
        'Fri' : 5,
        'Sat' : 6,
        'Sun' : 7
    }

    def __init__(self, day):
        
        self.day = day
        
        if self.day not in self.__week_days:
            raise WeekDayError
            
    def __str__(self):
        
        return self.day 

    def add_days(self, n):
        
        #days_to_add = n % 7 
        day_number = self.__week_days[self.day]
        result = (n + day_number) % 7
                
        key_list = list(self.__week_days.keys())
        val_list = list(self.__week_days.values())
        position = val_list.index(result)
        self.day = key_list[position]

        
    def subtract_days(self, n):
       #days_to_subtract = n % 7 
       day_number = self.__week_days[self.day]
       result = (day_number - n) % 7
       if result < 0:
           result = 7 - result
       if result == 0:
           result = 7
               
       key_list = list(self.__week_days.keys())
       val_list = list(self.__week_days.values())
       position = val_list.index(result)
       self.day = key_list[position]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
