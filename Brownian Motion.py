#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# Brownian Motion for Chunky Hamsters
# Sneha Nair -260850706

# In[6]:


## intiate a variable N which we may change as we wish
N=100
## Speed Array
V= [0]*N
alpha = 0.02
## We need some type of intitial condition which I will just set to be zero for now
V[0]=0


# In[14]:


for i in range (1,N):
    ##generates a number between 0 and 1 that will gives us 50-50 probability of having either +1 step,-1 step 
    ## based on uniform distribution.
    
    move = np.random.uniform(0,1)
    if move<0.5:
        V[i]=V[i-1]-alpha*V[i-1]+1
    if move>0.5:
        V[i]=V[i-1]-alpha*V[i-1]-1


# In[16]:


print('Here is the array of the V_(T):')
print(V)


# In[27]:


## I just need to make array of the from 0 to N. 
times = list(range(0, N))
## Now we can plot this in case anyone is interested.
plt.plot(times,V,'r-')
plt.xlabel('Time')
plt.ylabel('Speed')
plt.title('Hamster Brownian Motion')


# THANKS
