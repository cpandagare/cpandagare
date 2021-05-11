#!/usr/bin/env python
# coding: utf-8

# In[1]:


## numbers which are divisible by 7 but are not a multiple of 5

for i in (range(2001,3200)):
    if i%7 ==0:
        if i%5!=0:    
            print(i)


# In[2]:


## to accept the user's first and last name and printed in reverse with a space

a= input("Enter your first name ")
b=input("Enter your second name ")

print(a[::-1],b[::-1])


# In[4]:


## VOlume of Sphere with diameter 12 cm

import math
d=12
r=6
y=(4/3)
h=6**3
vol= y*math.pi*h
print('Volume of Sphere =',vol, "cubic cm")


# In[ ]:




