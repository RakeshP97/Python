#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 14:20:42 2019

"""

def is_triangular(k):
    '''
    k: postive integer
    returns True if k is triangular , and
    False otherwise
    '''
    sum =0
    i=1
    while sum < k:
        sum+=i
        i +=1
        if sum == k:
            return True
    return False

import math
def find_number(low,high, f):
    '''
    s: string of lower -case letters without spaces
    returns the longest substring of s sorted in alphabetical order
    '''
    if low<high:
        for i in range(round(math.log2(100))):
            guess = int((high+low)//2)
            comp = f(guess)
            if comp > 0:
                low = guess
            elif comp <0:
                high = guess
            else:
                return (guess, i+1)
            

def get_longest_sorted(s):
    '''
    s: string of lower -case letters without spaces
    returns the longest substring of s sorted in alphabetical order
    '''
    longetAscendingStr = ''
    currentLongestStr = s[0]
    for i in range(1,len(s)):
        if s[i-1] <= s[i]:
            currentLongestStr += s[i]
        else:
            if len(longetAscendingStr) < len(currentLongestStr):
                longetAscendingStr = currentLongestStr
            currentLongestStr=s[i]
    if len(longetAscendingStr) < len(currentLongestStr):
        longetAscendingStr = currentLongestStr
    return longetAscendingStr