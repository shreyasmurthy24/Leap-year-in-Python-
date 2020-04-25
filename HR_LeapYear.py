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


#Method 2
#def isLeap(year):
#    leap = False
#    return year % 4 == 0 and (year % 100 != 0 and year % 400 == 0)
#
#year = int(input())
#print(isLeap(year))

#Print in SINGLE LINE
#for i in range(5):
#    print(i, end=' ')



