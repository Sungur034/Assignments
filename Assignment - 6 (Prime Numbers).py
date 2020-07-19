#!/usr/bin/env python
# coding: utf-8

# In[1]:


primes = []
count  = 0
for n in range(2,101) :
    for i in range (1,n+1) :
        if n % i == 0 :
            count += 1
    if count == 2 :
        primes.append(n)
    count = 0
print(primes)


# In[ ]:




