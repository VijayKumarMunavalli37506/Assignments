# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:44:57 2020

@author: vmunavalli
"""


#Session2
#1 Write a Python Program to implement your own myreduce() function which works exactly like
#Python's built-in function reduce(

def myreduce(func, my_list):
    # Get first item in sequence and assign to
    result = my_list[0]# iterate over remaining items in sequence and apply reduction function 
    for item in my_list[1:]:
        result = func(result, item)
    return result

# test myreduce function
def mul(x,y): return x * y

print(mul(5,10))
print(myreduce(mul,[5,10,2,3,4]))



#2 Write a Python Program to implement your own myfilter() function which works exactly like
#Python's built-in function reduce(

def myfilter(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False  
  
# sequence 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 
  
# using filter function 
filtered = filter(myfilter, sequence) 
  
print('The filtered letters are:') 
for s in filtered: 
    print(s) 
    
#Implement List comprehensions to produce the following lists.
#Write List comprehensions to produce the following Lists

#['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
#[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
#[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
    
#########
lst = "ACADGILD"
alphabet_list = [ alphabet for alphabet in lst ]
print ("ACADGILD == " + str(alphabet_list))


given_lst = ['x','y','z']
result = [ item*num for item in given_lst for num in range(1,5)  ]
print("['x','y','z'] == " +   str(result))


#new_list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in given_lst  ]
print("['x','y','z'] == " +   str(result))



#########
input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] ==" +  str(result))

#########
input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =" +  str(result))

#########
input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =" +  str(result))


#Implement a function longestWord() that takes a list of words and returns the longest one

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["PHP", "Exercises", "Backend"]))



#Task 2:
#1.1
#Write a Python Program(with class concepts) to find the area of the triangle using the below
#formula.
#area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#Function to take the length of the sides of triangle from user should be defined in the parent
#class and function to calculate the area should be defined in subclass.



class AreaOfTriangle:
  def __init__(self,a,b,c):
    self.a = a
    self.b = b
    self.c = c
    
  def getAreaofTriangle(self):      
      s = (self.a + self.b + self.c) / 2
      area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
      print('The area of the triangle is %0.2f' % area)

class CalculateAreaofTriangle(AreaOfTriangle):
    pass

#val = AreaOfTriangle(1,2,3)
result = CalculateAreaofTriangle(1.2,2.3,3.2)

result.getAreaofTriangle()
    


#Write a function filter_long_words() that takes a list of words and an integer n and returns the list
#of words that are longer than n.
def filter_long_words(n, str):  
    word_len = []  
    txt = str.split(" ")  
    for x in txt:  
        if len(x) > n:  
            word_len.append(x)  
    return word_len   
print(filter_long_words(3, "The quick brown fox jumps over the lazy dog"))  



#Write a Python program using function concept that maps list of words into a list of integers
#representing the lengths of the corresponding words .
#Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
#Here 2,3 and 4 are the lengths of the words in the list.


input_list = ['ab','cde','erty']
result = [ len(a) for a in input_list]
print(result)



#2.2
#Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
#a vowel, False otherwise

vowels = ['a','e','i','o','u']

def check_SingleCharacter_Volwel(c):

    if len(c)<1 :
        if c in vowels:
            print("true")
        else:
            print("false")
    else:
        print("please provide single charachter")
    
   
check_SingleCharacter_Volwel('ab')    
    