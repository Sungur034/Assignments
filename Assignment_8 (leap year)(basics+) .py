#!/usr/bin/env python
# coding: utf-8

# In[1]:


(lambda x : print(f"{x} is a leap year") if ((x % 400 == 0) or (x % 4 == 0 and x % 100 != 0)) else print(f"{x} is not a leap year"))(x = int(input("pls enter a year : ")))


# In[ ]:





# In[ ]:




