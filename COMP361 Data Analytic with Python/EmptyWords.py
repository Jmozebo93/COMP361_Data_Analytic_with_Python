#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 15:30:22 2023

@author: jordanmozebo
"""

def EmptyWords():
    print("Enter a word: ");
    words = input();
    fullwords = " ";
    
    fullwords += words+" ";
    
    while(len(words) != 0):
        print("Enter another word: ")
        words = input()
        fullwords += words+" ";
        
    print("Here is the entire words: ",fullwords)
    
EmptyWords()