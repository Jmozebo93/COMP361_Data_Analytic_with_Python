#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:28:18 2023

@author: jordanmozebo
"""

def my_slice(lst, start, step, length):
    if length is None:
        return lst[start::step]
    else:
        end = start + length
        return lst[start:end:step]
