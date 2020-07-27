#!/usr/bin/env python
# coding: utf-8

# In[2]:


x = input("pls enter a sentence:  ").lower()
z = {i: x.count(i) for i in set(x) if i.isspace() or i.isalpha()}
print('\n', z)        
    


# In[ ]:




