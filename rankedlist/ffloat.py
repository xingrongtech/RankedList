#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:01:14 2018

@author: xingrongtech
"""

class FFloat():
    
    def __init__(self, numInput):
        if type(numInput) == float:
            self.__str = '%g' % numInput
            self.__num = numInput
        else:
            self.__str = numInput
            self.__num = float(numInput)
        
    def __abs__(self):
        return abs(self.__num)
        
    def __gt__(self, obj):
        if type(obj) == FFloat:
            return self.__num > obj.__num
        else:
            return self.__num > obj
    
    def __lt__(self, obj):
        if type(obj) == FFloat:
            return self.__num < obj.__num
        else:
            return self.__num < obj
    
    def __ge__(self, obj):
        if type(obj) == FFloat:
            return self.__num >= obj.__num
        else:
            return self.__num >= obj
    
    def __le__(self, obj):
        if type(obj) == FFloat:
            return self.__num <= obj.__num
        else:
            return self.__num <= obj
        
    def __add__(self, obj):
        if type(obj) == FFloat:
            return self.__num + obj.__num
        else:
            return self.__num + obj
        
    def __radd__(self, obj):
        if type(obj) == FFloat:
            return obj.__num + self.__num
        else:
            return obj + self.__num
        
    def __sub__(self, obj):
        if type(obj) == FFloat:
            return self.__num - obj.__num
        else:
            return self.__num - obj
        
    def __rsub__(self, obj):
        if type(obj) == FFloat:
            return obj.__num - self.__num
        else:
            return obj - self.__num
        
    def __mul__(self, obj):
        if type(obj) == FFloat:
            return self.__num * obj.__num
        else:
            return self.__num * obj
        
    def __rmul__(self, obj):
        if type(obj) == FFloat:
            return obj.__num * self.__num
        else:
            return obj * self.__num
        
    def __truediv__(self, obj):
        if type(obj) == FFloat:
            return self.__num / obj.__num
        else:
            return self.__num / obj
        
    def __rtruediv__(self, obj):
        if type(obj) == FFloat:
            return obj.__num / self.__num
        else:
            return obj / self.__num
    
    def __str__(self):
        return self.__str
        
    def __repr__(self):
        return self.__str
    
    def toFloat(self):
        return self.__num
