# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 16:17:05 2022

@author: Dr. Albert Esterline
"""
from sum_threshold import sum_threshold
from my_slice import my_slice

lst = [7, 2, 12, 9, 15, 4, 11, 5]
print('The sum of the elemenst, left to right, without exceeding the')
print('threshold 40 is ', sum_threshold(40, *lst))
print('The same but with a threshold of 70: ', sum_threshold(70, *lst))
print('With an empty list of numbers: ', sum_threshold(50))

print('my_slice(lst): ', my_slice(lst))
print('my_slice(lst, start=2, step=1): ', my_slice(lst, start=2, step=1))
print('my_slice(lst, start=2, length=5): ', my_slice(lst, start=2, length=5))
print('my_slice(lst, length=5): ', my_slice(lst, length=5))

print('with_factors(lst, [2, 5]): ', with_factors(lst, [2, 5]))

print('pairs_factors(lst): ', pairs_factors(lst))
