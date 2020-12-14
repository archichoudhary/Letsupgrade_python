#!/usr/bin/env python
# coding: utf-8

# Day 3 
# Question 1
# 

# In[1]:



#Use IF ELSE and ELIF to write a program in python for your Report Cards.

marks = 80
if marks >= 90:
  grade = 'A'
elif marks >= 80:
  grade = 'B'
elif marks >= 70:
  grade = 'C'
elif marks >= 60:
  grade = 'D'
else:
  grade = 'F'
print(grade)


# Question 2

# In[2]:


#Use For Loop to Print Prime Numbers in between 1 to 1000

lower = 1
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num >= 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# Question 3

# In[8]:


# Multiplication table (from 1 to 10) in Python

for num in range(1,11):
    print(num)
    for i in range(1, 11):
        print(num,"x",i," = ", num*i)
   


# Question 4

# In[10]:


#Write a program to Print X Prime Numbers using While Loop starting from 0, and take the INput of X from the user.


Range = int(input("enter the number till where the prime no.s should be print "))
Number = 1
while(Number <= Range):
    count = 0
    i = 2
    
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
    Number = Number  + 1


# In[ ]:




