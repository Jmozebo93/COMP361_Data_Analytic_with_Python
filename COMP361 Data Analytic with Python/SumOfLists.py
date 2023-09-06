#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:16:24 2023

@author: jordanmozebo
"""

def SumOfLists():
    print("Enter a list for numbers for the first list: ")
    list_num1 = list(eval(input()));
    
    print("Enter a list of numbers for the second list: ")
    list_num2 = list(eval(input()))
    
    new_list = []
    
    if len(list_num1)  > len(list_num2) :
        for i in range(len(list_num2)):
            sum = list_num1[i] + list_num2[i]
            new_list.append(sum)
            
        print("The new list :", new_list)
        
    elif len(list_num1) < len(list_num2) :
        for i in range(len(list_num1)):
            sum = list_num1[i] + list_num2[i]
            new_list.append(sum)
            
        
        print("The new list :", new_list)   
        
    else:
        for i in range(len(list_num1)):
            sum = list_num1[i] + list_num2[i]
            new_list.append(sum)
            
        print("The new list :", new_list) 
        
SumOfLists()
            