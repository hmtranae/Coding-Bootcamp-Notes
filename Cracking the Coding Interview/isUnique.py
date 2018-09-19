# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 16:47:00 2018

@author: Hieu
"""

def isUnique(s):
    letterSet = set()
    for letter in s:
        if letter not in letterSet:
            letterSet.add(letter)
        elif letter in letterSet:
            return False
    return True