#!/usr/bin/env python
# coding: utf-8

# In[1]:


# How to verfiy python version
import sys
print(sys.executable)
print(sys.version)


# In[2]:


# Hello Message
print("Hello!!..")


# In[31]:


### Variables and Data Types

# 1. Python is completely object oriented progamming language and not "statically typed". So, we do not need to decalre variable before using or declare their type.
# 2. Every variable in python as object.
# 3. Variable is a name given to value not to a memory location to store value. Variable can access with thier identifier(name).
# 4. Variable is case-sensitive

myvar="Naresh"
print(myvar)

myvar = 527
print(myvar)

# If we want to know the type of data assigned to variable use type() function.
myvalue=527
type(myvalue)

#  ---- Number Type ------ #
a = 10
b = 20
a+b


# In[9]:


# ----- String Type ----- #
 # -- String is a series of charecters.
 # --String is an immutable object.
# how to define sting
name = "Naresh"
print(name)


# In[10]:


# String Methods 
 #-- title()/lower()/upper()

name = "naresh"
print(name.title())
print(name.lower())
print(name.upper())


# In[13]:


# Declaration of String
 #- single quotes/double quotes/triple quotes

declare = 'test'
declare1 = "test1"
declare2 = """test2"""
print(declare)
print(declare1)
print(declare2)


# In[27]:


# f- strings
first_name = "Naresh"
last_name = "Chamakuri"
full_name = f"{first_name} {last_name}"
print(full_name)

# If we want to print full_name in capital?
print(full_name.upper())

# lower letters
print(full_name.lower())


# In[30]:


# Adding and trimming white spaces
message = "hello!"
print(message)

#adding tab at satrting
print('\thello!!')

# Python provided 3 methods (strip()/ rstrip()/ lstrip()) to trim white spaces to string objects.
message = "hello!!!  "
print(message.rstrip()) #removes the white saces from right side

message = " hello!!!!"
print(message.lstrip()) # removes white space from left side

message = " hello!!!!! "
print(message.strip()) # removes white space from both side


# In[35]:


# To print the o/p in new line
print("Languages:\nC\nJava\nPython\nShell Scripting")


# In[ ]:




