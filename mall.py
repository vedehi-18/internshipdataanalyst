#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[9]:


file_path = r'C:\Users\vijay sharma\Documents\Mall_Customers.csv'  
df = pd.read_csv(file_path)


# In[3]:


print(df.isnull().sum())
df = df.dropna()


# In[4]:


df = df.drop_duplicates()


# In[5]:


if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].str.lower().str.strip()


# In[6]:


df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')


# In[7]:


int_columns = ['age', 'spending_score_(1-100)', 'annual_income_(k$)']
for col in int_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)


# In[8]:


df.head


# In[10]:


output_path = r'C:\Users\vijay sharma\Documents\Mall_Customers.csv'
df.to_csv(output_path, index=False)
print(f"Cleaned file saved at: {output_path}")


# In[11]:


df.head


# In[ ]:




