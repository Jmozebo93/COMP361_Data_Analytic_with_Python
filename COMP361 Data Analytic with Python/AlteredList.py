#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:09:05 2023

@author: jordanmozebo
"""

def AlteredList():
    print("Enter a list of numbers: ");
    list_nums = list(eval(input()));
    
    print("The first half: ", list_nums[:int((len(list_nums)/2))]);
    print("The second half: ", list_nums[int((len(list_nums)/2)):])
    
    if list_nums[0] > list_nums[len(list_nums) - 1] :
        list_nums[0], list_nums[len(list_nums) - 1] = list_nums[len(list_nums) - 1], list_nums[0]
    elif list_nums[0] < list_nums[len(list_nums) - 1] :
        list_nums[0] += 1
        list_nums[len(list_nums) - 1] +=1
    else:
        list_nums[0] = 0
        list_nums[len(list_nums) - 1] = 0
    print("Altered list: ", list_nums)
    
AlteredList()