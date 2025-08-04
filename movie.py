#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


file_path = r'C:\Users\vijay sharma\Documents\movie.csv'  # ← Replace this path with the correct one
df = pd.read_csv(file_path)


# In[3]:


print(df.isnull().sum())
df = df.dropna()


# In[4]:


df = df.drop_duplicates()


# In[5]:


text_columns = ['genre', 'country', 'language', 'rating', 'certificate']
for col in text_columns:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.lower()


# In[6]:


date_columns = [col for col in df.columns if 'date' in col.lower()]
for col in date_columns:
    df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')


# In[7]:


df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')


# In[8]:


int_columns = ['runtime', 'votes', 'year', 'score']
for col in int_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)


# In[9]:


output_path = r'C:\Users\vijay sharma\Documents\movie.csv'  
df.to_csv(output_path, index=False)
print(f" Cleaned file saved to: {output_path}")


# In[10]:


df.head


# In[ ]:




