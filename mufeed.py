#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv('/kaggle/input/football-players-datasets-2015-2024/Latest Football  Players 2024 Data.csv')


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.describe()


# In[7]:


df.info()


# In[8]:


plt.hist(df['Goals'], bins=20, edgecolor='red')
plt.title('Distribution of Players Goals')
plt.xlabel('Goals')
plt.ylabel('Number of Players')
plt.show()


# In[9]:


sns.boxplot(x=df['Seasons Ratings'])
plt.title('Distribution of Seasons Ratings')
plt.xlabel('Seasons Ratings')
plt.show()


# In[10]:


sns.scatterplot(x='Goals', y='Assists', data=df)
plt.title('Goals vs Assists')
plt.xlabel('Assists')
plt.ylabel('Goals')
plt.show()


# In[ ]:




