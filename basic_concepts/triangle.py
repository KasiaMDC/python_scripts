# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 08:53:05 2024

@author: Kasia
"""

from hypotenuse import Point


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        
        
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        
        return self.__vertices[0].distance_from_point(self.__vertices[1]) + self.__vertices[1].distance_from_point(self.__vertices[2]) + self.__vertices[2].distance_from_point(self.__vertices[0])


def main():
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())

if __name__ == '__main__':
    main()