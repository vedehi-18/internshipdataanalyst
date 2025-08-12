#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import sqlite3
df = pd.read_csv( r'C:\Users\vijay sharma\Downloads\Online Sales Data.csv')


# In[14]:


df = df.rename(columns={
    "Transaction ID": "order_id",
    "Date": "order_date",
    "Total Revenue": "amount"
})


df["order_date"] = pd.to_datetime(df["order_date"])


conn = sqlite3.connect(":memory:")
df.to_sql("online_sales", conn, index=False, if_exists="replace")


# In[15]:


query = """
SELECT
    strftime('%Y', order_date) AS year,
    strftime('%m', order_date) AS month,
    SUM(amount) AS monthly_revenue,
    COUNT(DISTINCT order_id) AS order_volume
FROM online_sales
GROUP BY year, month
ORDER BY year, month;
"""

result_df = pd.read_sql(query, conn)
print("Monthly Revenue & Order Volume:")
print(result_df)

top3_query = """
SELECT
    strftime('%Y', order_date) AS year,
    strftime('%m', order_date) AS month,
    SUM(amount) AS monthly_revenue
FROM online_sales
GROUP BY year, month
ORDER BY monthly_revenue DESC
LIMIT 3;
"""

top3_df = pd.read_sql(top3_query, conn)
print("\nTop 3 Months by Revenue:")
print(top3_df)



# In[16]:


query = """
SELECT
    strftime('%Y', order_date) AS year,
    strftime('%m', order_date) AS month,
    SUM(amount) AS monthly_revenue,
    COUNT(DISTINCT order_id) AS order_volume
FROM online_sales
GROUP BY year, month
ORDER BY year, month;
"""

result_df = pd.read_sql(query, conn)


print("Grouped by Year and Month:")
print(result_df)


# In[12]:


query = """
SELECT
    strftime('%Y', order_date) AS year,
    strftime('%m', order_date) AS month,
    SUM(amount) AS monthly_revenue  -- SUM() calculates total revenue
FROM online_sales
GROUP BY year, month
ORDER BY year, month;
"""

result_df = pd.read_sql(query, conn)


print("Monthly Revenue using SUM():")
print(result_df)


# In[17]:


query = """
SELECT
    strftime('%Y', order_date) AS year,
    strftime('%m', order_date) AS month,
    COUNT(DISTINCT order_id) AS order_volume  -- COUNT DISTINCT for unique orders
FROM online_sales
GROUP BY year, month
ORDER BY year, month;
"""

result_df = pd.read_sql(query, conn)


print("Monthly Order Volume using COUNT(DISTINCT order_id):")
print(result_df)


# In[18]:


query = """
SELECT
    strftime('%Y', order_date) AS year,
    strftime('%m', order_date) AS month,
    SUM(amount) AS monthly_revenue,
    COUNT(DISTINCT order_id) AS order_volume
FROM online_sales
GROUP BY year, month
ORDER BY monthly_revenue DESC;  -- Sorting by revenue from highest to lowest
"""

result_df = pd.read_sql(query, conn)


print("Monthly Revenue & Order Volume (Sorted by Revenue Descending):")
print(result_df)


# In[19]:


query = """
SELECT
    strftime('%Y', order_date) AS year,
    strftime('%m', order_date) AS month,
    SUM(amount) AS monthly_revenue,
    COUNT(DISTINCT order_id) AS order_volume
FROM online_sales
WHERE order_date BETWEEN '2024-03-01' AND '2024-06-30'  -- Time period filter
GROUP BY year, month
ORDER BY year, month
LIMIT 3;  -- Limit to first 3 results
"""

result_df = pd.read_sql(query, conn)

print("Limited Results for Specific Time Period (Mar 2024 - Jun 2024, First 3 Rows):")
print(result_df)


# In[ ]:




