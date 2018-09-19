# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 21:14:06 2018

@author: Hieu
"""

def checkPermutation(s1, s2):
    setS1 = set(s1)
    count = 0
    for i in s2:
        if i in setS1:
            count += 1
    if count == len(s1):
        return True
    else:
        return False