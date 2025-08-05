#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd 


# In[17]:


df = pd.read_csv(r'C:\Users\vijay sharma\Documents\aa.csv',encoding='ISO-8859-1')


# In[9]:


df = df.dropna()
df = df.drop_duplicates()


# In[10]:


text_columns = ['Country', 'Segment']
for col in text_columns:
    df[col] = df[col].str.strip().str.lower()


# In[11]:


df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')


# In[12]:


df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]


# In[13]:


if 'postal_code' in df.columns:
    df['postal_code'] = df['postal_code'].astype(str)


# In[14]:


df.to_csv('cleaned_aa.csv', index=False)


# In[18]:


df


# In[ ]:





# In[ ]:




