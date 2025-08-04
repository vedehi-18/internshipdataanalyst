#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


df= pd.read_csv(r'C:\Users\vijay sharma\Documents\demo.csv')


# In[3]:


df.head


# In[4]:


print("Initial Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())


# In[9]:


df_cleaned = df.dropna().copy() 


# In[10]:


df_cleaned = df_cleaned.drop_duplicates()


# In[11]:


text_columns = ['make', 'model', 'trim', 'body', 'transmission', 'color', 'interior', 'state', 'seller']
for col in text_columns:
    df_cleaned.loc[:, col] = df_cleaned[col].str.strip().str.lower()


# In[15]:


df_cleaned['saledate'] = pd.to_datetime(df_cleaned['saledate'], errors='coerce', utc=True)
df_cleaned = df_cleaned[df_cleaned['saledate'].notnull()]
df_cleaned['saledate'] = df_cleaned['saledate'].apply(lambda x: x.strftime('%d-%m-%Y'))


# In[16]:


df_cleaned.columns = [col.strip().lower().replace(" ", "_") for col in df_cleaned.columns]


# In[18]:


df_cleaned['year'] = df_cleaned['year'].astype(int)
df_cleaned['condition'] = df_cleaned['condition'].astype(int)
df_cleaned['odometer'] = df_cleaned['odometer'].astype(int)
df_cleaned['mmr'] = df_cleaned['mmr'].astype(int)
df_cleaned['sellingprice'] = df_cleaned['sellingprice'].astype(int)


# In[19]:


df_cleaned.to_csv("demo_cleaned.csv", index=False)

print("Data cleaning complete. File saved as 'demo_cleaned.csv'.")


# In[20]:


# Reload the saved file
df_check = pd.read_csv("demo_cleaned.csv")

# Preview the top few rows
print(df_check.head())


# In[ ]:




