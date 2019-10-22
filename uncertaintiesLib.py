# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:30:22 2019

@author: justi
"""

import math

def square(x):
    return x*x

def UncertAdd(arr):
    sum = 0
    for i in range (0,len(arr),1):
        sum = sum + (square(arr[i]))
    return math.sqrt(sum)

#put in array of measurment uncertainties,then array of values, then the actual answer to get the calculated uncertainty
def UncertMult(arr,vals,ans): 
    sum = 0
    for i in range(0,len(arr),1):
        term = arr[i]/vals[i]
        sum = sum + square(term)
    ret = math.sqrt(sum) * ans
    return ret

#put in the uncertainity of the base, the base, and the exponent of the exponential and get uncertainty of exponential
def UncertExp(uBase,Base,exp): 
    ret = (uBase/base)*exp
    return ret

#put in the uncertainty of the log parameter, and the value of the log parameter and get uncertainty of the log
def UncertLog(uA,A):
    ret = 0.434*(uA/A)
    return ret
    

def GetAverages(arr):
    sum = 0
    for i in range(0,len(arr),1):
        sum = sum + arr[i]
    return sum/len(arr)