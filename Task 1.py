#!/usr/bin/env python
# coding: utf-8

# # area of circle

# In[ ]:




import math as m
def area_of_circle(r):
    return 2*(m.pi)*r


print("Please provide radius")
radius = float(input())

area = area_of_circle(radius)

print("Area: ", area)


# # a function to get the largest number between 3

# In[ ]:


#a function to get the largest number between 3
def large(a,b,c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    else:
        return c
k = float(input())
l=float(input())
m=float(input())
ln = large(k,l,m)
print("Largest number beetween three: ", ln)


# # a function to convert the vowels of a string into 1 and consonants into 0

# In[8]:


#a function to convert the vowels of a string into 1 and consonants into 0
def vowel_convertion(input_str):
        vowels = 'aeiou'
        VOW = 'AEIOU'
        out_str=''
        for char in input_str:
            if char in vowels:
                out_str+='1'
            elif char in VOW:
                out_str+='1'
            else:
                out_str+='0'
        return out_str
    
inp = input()
print(vowel_convertion(inp))
                
              









# # Repeat Input String

# In[11]:


# Repeat Input String
def doub_str(ip):
    return ip+ip

you = input()
print(doub_str(you))


# # Use FILTER() to show an array/list of elements with "P" inside.

# In[28]:


#Use FILTER() to show an array/list of elements with "P" inside.

def ret_p(string):
    return 'P'in string or'p' in string
my=input().split()
print(my)
type(my)
out = list(filter(ret_p,my))
print(out)
        
    


# # Use MAP() to add a "P" if "P" is not there.

# In[35]:


#Use MAP() to add a "P" if "P" is not there.
def add_p(string):
    if 'P' not in string:
        string+='P'
        return string
    else:
        return string
    
my=input().split()
print(my)
out = list(map(add_p,my))
print(out)


# # Use REDUCE() to get the sum of this list: [1, 2, 3, 4] -> [10] 

# In[38]:


#Use REDUCE() to get the sum of this list: [1, 2, 3, 4] -> [10] 
from functools import reduce
def lis():
   return list(map(int,input().split()))
input_list = lis()
sum_list = reduce(lambda x, y: x + y, input_list)
print(sum_list)


# In[ ]:




