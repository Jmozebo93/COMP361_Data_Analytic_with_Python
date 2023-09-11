#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 08:56:38 2023

@author: jordanmozebo
"""

def sum_threshold(num, *lst):
    sum = 0;
    
    if (len(lst) == 0):
        return 0;
    
    for i in lst:
        if(sum + i > num):
            break
        sum += i;
       
    return sum
        
        