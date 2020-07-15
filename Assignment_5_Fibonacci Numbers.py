#!/usr/bin/env python
# coding: utf-8

# In[1]:


fibonacci = []
for i in range(2): fibonacci.append(1)
for i in range(8): fibonacci.append(fibonacci[i]+fibonacci[i+1])
print("fibonacci numbers:", fibonacci)


# In[ ]:




