#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 19:40:13 2023

@author: jordanmozebo
"""

def with_factors(lst1, lst2):
    def has_factor(x, fcts):
      return any(x % factor == 0 for factor in fcts)
    
    return list(filter(lambda x: has_factor(x, lst2), lst1))
            