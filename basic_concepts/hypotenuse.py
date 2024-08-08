# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:26:36 2024

@author: Felipe
"""

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        
        self.__x = x
        self.__y = y

    def getx(self):
        
        return self.__x

    def gety(self):
        
        return self.__y

    def distance_from_xy(self, x, y):
        
        x2 = self.__x
        y2 = self.__y
        
        return math.hypot(x2 - x, y2 - y)

    def distance_from_point(self, point):
        
        x2 = self.__x
        y2 = self.__y
        
        x = point.getx()
        y = point.gety()
        
        return math.hypot(x2 - x, y2 - y)


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
