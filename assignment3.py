# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 20:20:17 2020

@author: vmunavalli
"""
import numpy as np
#    Task 1:
#    1.
#    Write a function to compute 5/0 and use try/except to catch the exceptions

def compute():
    try:
        (5/0)
    except:
        print("5/0  => not divisible")
        
compute()



#2.
#Implement a Python program to generate all sentences where subject is in ["Americans",
#"Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].
#Hint: Subject,Verb and Object should be declared in the program as shown below.
#subjects=["Americans ","Indians"]
#verbs=["play","watch"]
#objects=["Baseball","Cricket"]
#Output should come as below:
#Americans play Baseball.
#Americans play Cricket.
#Americans watch Baseball.
#Americans watch Cricket.
#Indians play Baseball.
#Indians play Cricket.
#Indians watch Baseball.
#Indians watch Cricket.


def GetSentence():
    subjects=["Americans ","Indians"]
    verbs=["play","watch"]
    objects=["Baseball","Cricket"]
    
    lst  = [tag + " "+ entry + " " + obj for tag in subjects for entry in verbs for obj in objects ]
    
    [print(l) for l in lst]
    
GetSentence()


#Task 2:
#1.
#Write a function so that the columns of the output matrix are powers of the input vector.
#The order of the powers is determined by the increasing boolean argument. Specifically, when
#increasing is False, the i-th output column is the input vector raised element-wise to the power
#of N - i - 1.
#HINT: Such a matrix with a geometric progression in each row is named for Alexandre-
#Theophile Vandermonde.

def GetPowerOfInputVector(ipvector, n, increasing=False):    
    if not increasing:
        output_matrx = np.array([x**(n-1-i) for x in ipvector for i in range(n)]).reshape(ipvector.size,n)
    elif increasing:
         output_matrx = np.array([x**i for x in ipvector for i in range(n)]).reshape(ipvector.size,n)    
    return output_matrx



inputvector = np.array([8,2,3,4,6])
no_col_opmat = 3
op_matx_dec_order = GetPowerOfInputVector(inputvector,no_col_opmat,False)
op_matx_inc_order = GetPowerOfInputVector(inputvector,no_col_opmat,True)

print("Number of columns in output matrix should be:",no_col_opmat,"\n")
print("Input array in decreasing order of powers:\n\n",op_matx_dec_order,"\n")
print("Input array in increasing order of powers:\n\n",op_matx_inc_order,"\n")



