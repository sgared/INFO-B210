#!/usr/bin/env python
# coding: utf-8

# ''INFO-B 210: Information Infrastructure I
# 
# Assignment 1: Numeric Variables
# '''
# 
# ### Purpose:
# '''
# The purpose of this assignment is to utilize python programming in practical setting to solve real world problems.
# 
# Skills:
# In order to complete this assignment you will need to
# 
# use critical thinking to write code to answer the questions
# 
# practice Python fundamentals and best practices
# '''
# 
# ### Knowledge:
# '''
# 1. This assignment will help you gain the following:
# 
# how to create and utilize numeric variables
# 
# utilize mathematical operators '''

# I will be using the following functions. 

# In[1]:


def cash_register(a, b):
    change = a - b
    return change


# In[2]:


def cel_kel(a): 
    change = a + 273
    return change


# In[3]:


def kel_fahr(a):
    change = 9/ 5 *  (a - 273) + 32
    return change


# In[4]:


def fahr_cel(a):
    change = 5/9  * (a - 32)
    return change


# 

# 1. In the time before credit cards and electronic banking, stores often had to make change for customers. 
# The modern United States Treasury uses 4 different coins for denominations less than 1 dollar quarters, dimes, nickles, 
# and pennies each worth $0.25, $0.10, $0.05, and $0.01 respectively. Additionally, they issue dollars in denominations of 
# $100, $50, $20, $10, $5, and $1. In the following problems, you will be given an amount tendered, and the total cost. 
# Write a program that will determine the amount of change needed and 
# the minimum amount of each of the dollar denominations and coins needed for the transaction. '''

#  ### a. $100 tendered, $36.57 cost

# In[5]:


result = cash_register(100, 36.57)
print(result)


# ### b. $80 tendered, $64.09 cost

# In[6]:


result1 = cash_register(80, 64.09)
print(round(result1,2))


# ### c. $10 tendered, $3.81 cost

# In[7]:


result2 = cash_register(10, 3.81)
print(round(result2,2))


# ### d. $50 tendered, $14.36 cost

# In[8]:


result3 = cash_register(50, 14.36)
print(round(result3,2))


# 2.Around the world there are 3 commonly used scales used for measuring temperature, 
# Celsius, Kelvin, and Fahrenheit. In the following problems you will be given a temperature in one scale, 
# and a different scale. Write a program that will calculate the temperature for the given scale. 
# Consider the following link for formulas converting between temperature scales: https://www.thoughtco.com/temperature-conversion-formulas-609324Links to an external site.
# '''

# ## a. 98.6°F, Celsius

# In[9]:


temp = fahr_cel(98.6)
print(temp)


# ### b. 329.7 Kelvin, Fahrenheit

# In[10]:


temp1 = kel_fahr(329.7)
print(temp1)


# ### c. -60.9°C, Kelvin

# In[11]:


temp2 = cel_kel(-60.9)
print(temp2)

