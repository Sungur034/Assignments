#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number=int(input("Enter a number between 1-100:"))

for i in range(1,number+1):
    if i%3==0 and i%5!=0:
        print("Fizz")
    elif i%3!=0 and i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)

