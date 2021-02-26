#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf
print(tf.__version__)


# In[5]:


## February 25
## freecodecamp Tensor Flow Lecture 2

import tensorflow as tf

print(tf.version)

t = tf.zeros([5,5,5,5])

#print(t)

t = tf.reshape(t,[625])
print(t)


# In[ ]:




