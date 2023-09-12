#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 20:58:24 2023

@author: jordanmozebo
"""

def pairs_factors(lst):
    result = [(x, [y for y in lst if x % y == 0 and x != y]) for x in lst]
    
    return result;