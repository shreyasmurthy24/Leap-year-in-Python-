# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:57:34 2020

@author: shreyas
"""
#Method 1
year = int(input())
if year % 4 == 0 and year % 100 != 0 :
    print('Leap')
elif year % 100 == 0 and year % 400 != 0:
    print('Not leap year')
elif year % 400 == 0:
    print('Leap year.')
else:
    print('Not leap')
