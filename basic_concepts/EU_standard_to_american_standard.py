# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 09:32:53 2024

@author: Kasia
"""
# 1 American mile = 1609.344 metres;
#1 American gallon = 3.785411784 litres.
#

miles_to_kilometers = 1.609344
gallons_to_litres = 3.785411784

def liters_100km_to_miles_gallon(liters):

     return (100 * gallons_to_litres)/(liters*miles_to_kilometers)

def miles_gallon_to_liters_100km(miles):
    
     return (100 * gallons_to_litres)/(miles*miles_to_kilometers)
   
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))