#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 12:57:46 2017

@author: christophergreen
Power digit sum
Problem 16
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

a=str(2**1000);
tot=0;
i=0;
while i<len(a):
    tot+=int(a[i]);
    i+=1;
print("the sum of the digits of 2^1000 is",tot);  #-->1366 CORRECT