#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q) Want to print lanuages in capital letters in display, so i assigned value to string and called string in print, it's printing in without assign values to languages

header="languages"

print(header)
print(header.upper())
print("\n")

print("header:\nC\nJava") # how to print "LANGUAGE" here??? 
#print(header.upper()":\nC\Java\nPython") -- throwing syntax error
print("\n")

heading=header.upper() # here assigning output value to new variable(identifier) and printing, it's giving expected o/p.
print(heading)


# In[29]:


#Numbers

a = 5
b = 3
c = a*b
print(c)
print('Total:', c)
print("\n")

# Values assigning to mutliple identifiers
x, y, z = 10, 20, 30
print('Printing only X and Z:', x, z)
print(z, y)
print("\n")

# type() -- it'll return the type of value
type(z)


# In[34]:


# Built in Functions for Numbers

# -- int, float, complex, round, hex, oct, pow, abs

myintvalue = 9

myfloatvalue = float(myintvalue) # converting intger value to float using built-in function
print('Float:', myfloatvalue)
print('------')

myfloat = 7.5

myint=int(myfloat) # converting float value to integer using built-in function
print('Integer:', myint)
print('-----')

myround=round(myfloat)
print('Round:', myround)
print('----')

mycomplex = complex(myfloat)
print('Complex:', mycomplex)
print('------')


# In[37]:


# hex, oct, pow, abs
myint = 6

myhex=hex(myint)
print('Hexa Value:', myhex)
print('----')

myoct=oct(myint)
print('Octal Value:', myoct)
print('------')

mypow = pow(myint,2)
print('Power of myint Value:', mypow)
print('------')

value = -222
myabs = abs(value)
print('Absolute No:', myabs)


# In[40]:


# Strings

mystring = "nareshchamakuri"
print(mystring)

print(mystring[0])

print(mystring[:6])

print(mystring[6:])


# In[47]:


myString="""Hello
"Welcome to Python" 
programming"""

print(myString)


# In[66]:


first_name = "Naresh"
last_name = "Chamakuri"
Age = 26

full_name = first_name+last_name
print(full_name)

print("Hello Mr.%s %s" %(first_name,last_name))
print('----')

print("Hello {} {}!!!,".format(first_name,last_name))
print('----')

print("Hello this is {:s} {:s} and I'm {:d}".format(first_name,last_name,Age))


# In[81]:


# Lists
#--List is mutuable obj
#--List is a collection of items in a particular order

Trending_Jobs = ['Python Developer','Data Analytics','Data Science','AWS','DevOps']
print(Trending_Jobs)

print('Favourite Job:', Trending_Jobs[3])
print("-------")

# To print elements from List
print(*Trending_Jobs)
print('-----')

print(*Trending_Jobs, sep=",")
print('------')

print(*Trending_Jobs, sep="\t")
print('-------')

print(*Trending_Jobs, sep="\n")


# In[ ]:




