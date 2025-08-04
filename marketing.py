#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[25]:


file_path= r'C:\Users\vijay sharma\Documents\marketing_campaign (1).csv'
with open(file_path, encoding='utf-8') as f:
    lines = f.readlines()


# In[26]:


header = lines[0].strip().split('\t')  # split header by tab
rows = [line.strip().split('\t') for line in lines[1:]] 


# In[27]:


df = pd.DataFrame(rows, columns=header)


# In[28]:


df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')


# In[29]:


numeric_cols = ['year_birth', 'income', 'recency', 'mntwines', 'mntfruits',
                'mntmeatproducts', 'mntfishproducts', 'mntsweetproducts', 'mntgoldprods']
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')


# In[30]:


if 'dt_customer' in df.columns:
    df['dt_customer'] = pd.to_datetime(df['dt_customer'], dayfirst=True, errors='coerce')


# In[31]:


for col in ['education', 'marital_status']:
    if col in df.columns:
        df[col] = df[col].str.lower().str.strip()


# In[32]:


df = df.drop_duplicates()
df = df.dropna()


# In[33]:


print(" Cleaned data:")
print(df.head())


# In[34]:


output_path = r'C:\Users\vijay sharma\Documents\marketing_campaign (1).csv'
df.to_csv(output_path, index=False)
print(f"\n✅ Cleaned file saved to: {output_path}")


# In[35]:


df.head


# In[ ]:




