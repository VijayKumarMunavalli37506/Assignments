# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:31:52 2020

@author: vmunavalli
"""

import math
import re

#2. Write a program which will find all such numbers which are divisible by 7 but are not a multiple
#of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
#comma-separated sequence on a single line.

nl=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print (','.join(nl))


#3. Write a Python program to accept the user's first and last name and then getting them printed in
#the the reverse order with a space between first name and last name.

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print (lname + " " + fname)


#Write a Python program to find the volume of a sphere with diameter 12 cm.
#Formula: V=4/3 * π * r


pi = math.pi
r = float(12/2)
V= 4.0/3.0*pi* r
print('The volume of the sphere is: ',V)



#Task 2:
#1.
#Write a program which accepts a sequence of comma-separated numbers from console and
#generate a list.
values = input("Input some comma seprated numbers : ")
list = values.split(",")
#tuple = tuple(list)
print('List : ',list)
#print('Tuple : ',tuple)

#2.
#Create the below pattern using nested for loop in Py
n = 5
for j in range(1,n):
    print("* " * j)
for num in reversed(range(n + 1)) : 
    print ("* "* num) 


#Write a Python program to reverse a word after accepting the input from the user.
word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


#Write a Python Program to print the given string in the format specified in the sample output.
#WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
#SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
#its citizens
#Sample Output:
#WE, THE PEOPLE OF INDIA,
#having solemnly resolved to constitute India into a SOVEREIGN, !
#SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
#and to secure to all its citizens




text = 'WE,THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens'

lst = re.split(',',text,3)

#lst [0] = lst[0]+ ","+ lst[1]
#lst[1] =""

for a in lst:
    print(a,",")
    print("  ")


