#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dictionary Data Type


# In[ ]:


# -- Dictinary is also a collection data type and it's combination of key:value pairs.
# -- Dictionary is mutable object but the key should be immutable.

# How to define dictionary?

# dict = {key1:value1, key2:value2, .., keyN:valueN}


# In[13]:


# How to initialize empty dictionary

alien_1 ={} 

# how to store data in empty dictionary
alien_1['color'] = 'yellow'
alien_1['points'] = 10
alien_1['score'] = 50
alien_1['net_total'] = 100
print(alien_1)

print(alien_1['net_total']) # To print the value with key (Here we assigned value 100 to key net_total)

print(f"The alien is in {alien_1['color']}")
print("------------")
      
alien_1['color'] = 'blue' # updating dict color value in dict since it's mutable obj     
print(f"The alien is now in {alien_1['color']}")


# In[3]:


alien_0={'color':'green', 'points':5}
print(alien_0)

print(alien_0['color']) 


# In[17]:


# How to Access values with get() method

employee = {'name':'Naresh', 'eid':'ABC123', 'contact_no':9012345}

print(employee.get('name'))
print(employee['name']) # here key assigned in square brackets

# Diff b/w accssing value with using key with get(key) method and square[key] brackets
# -- The diff while using get() method retuns "None" instaed of "KeyError" if the key not found in dictionary.

print(employee.get('address'))
print(employee['address'])


# In[ ]:




