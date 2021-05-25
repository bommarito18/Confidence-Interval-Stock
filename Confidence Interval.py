#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import numpy as np
from scipy.stats import norm


# In[42]:


ms = pd.read_csv('../Data/MSFT.csv')
ms.head()


# In[43]:


ms['logReturn'] = np.log(ms['Close'].shift(-1)) - np.log(ms['Close'])


# In[50]:


norm.ppf(0.95)


# In[51]:


norm.ppf(.05)


# In[45]:


sample_size = ms['logReturn'].shape[0]
sample_mean = ms['logReturn'].mean()
sample_std = ms['logReturn'].std(ddof=1) / sample_size**0.5
print(sample_size)
print(sample_mean)
print(sample_std)


# In[1]:


mu, sigma = 0.0008769175067270367, 0.00023324185521014144
norm_dist = np.random.normal(mu, sigma, 100)


# In[48]:


z_left = norm.ppf(0.05)
z_right = norm.ppf(0.95)

interval_left = sample_mean+z_left*sample_std
interval_right = sample_mean+z_right*sample_std


# In[49]:


print('Sample Mean is ', sample_mean)
print('*********************************************')
print('90% confidence interval is ')
print(interval_left,interval_right)


# In[ ]:




