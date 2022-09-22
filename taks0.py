# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 14:43:58 2022

@author: acer
"""

for num in range(1,100):
    string = ""
    if num % 5 == 0 and num % 3 == 0:
        string = string + "Fizzbuzz"
    elif num % 5 == 0:
        string = string + "Buzz"
    elif num % 3 == 0:
        string = string + "Fizz"
    else:
        string = string + str(num)
    print(string)