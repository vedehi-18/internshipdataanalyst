#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


file_path = r'C:\Users\vijay sharma\Documents\medical.csv'
df = pd.read_csv(file_path)


# In[3]:


print(df.isnull().sum())
df = df.dropna()


# In[4]:


df = df.drop_duplicates()


# In[5]:


for col in ['gender', 'country']:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.lower()


# In[6]:


for col in df.columns:
    if "date" in col.lower(): 
        df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')


# In[7]:


df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')


# In[8]:


if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(0).astype(int)


# In[9]:


df.head


# In[11]:


df.to_csv(r'C:\Users\vijay sharma\Documents\medical.csv', index=False)
print(" Cleaned file saved successfully.")


# In[12]:


df.head


# In[ ]:




