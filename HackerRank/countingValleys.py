# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:00:07 2018

@author: Hieu
"""

def countingValleys(n, s):
    """
    Input: n is number of steps Gary takes
    s is the string describing his path (U is 1 step up in alt, D is 1 step down in alt)
    Returns integer denotes number of valleys traversed
    """
    # count number of times the rollingSum is -1  when GOING DOWN
    valley = rollingSum = 0
    for i, path in enumerate(s):
        if path == 'D' and rollingSum == 0:
            rollingSum -= 1
            valley += 1
        elif path == 'U':
            rollingSum += 1
        else:
            rollingSum -= 1
        print (rollingSum)
    return valley