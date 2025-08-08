#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import sqlite3

# Load the CSV file
df = pd.read_csv(r'C:\Users\vijay sharma\Documents\test.csv', encoding="latin1")

# Connect to SQLite (creates a DB in memory or file)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Save DataFrame to SQL table
df.to_sql("data", conn, if_exists="replace", index=False)

# Example SQL query: total sales per country
query = """
SELECT Country, SUM(Quantity * UnitPrice) AS TotalSales
FROM data
GROUP BY Country
ORDER BY TotalSales DESC
LIMIT 5;
"""

# Run the query
result = cursor.execute(query)

# Fetch and print the results
for row in result.fetchall():
    print(row)

# Close the connection
#conn.close()


# In[16]:


df.to_sql("data", conn, if_exists="replace", index=False)

query = """
SELECT * 
FROM data
WHERE Country = 'Germany';

"""

result = cursor.execute(query)


for row in result.fetchall():
    print(row)

#conn.close()


# In[18]:


df.to_sql("data", conn, if_exists="replace", index=False)


query = """
SELECT Country, TotalSales
FROM (
    SELECT Country, SUM(Quantity * UnitPrice) AS TotalSales
    FROM data
    GROUP BY Country
) AS CountrySales
ORDER BY TotalSales DESC
LIMIT 5;

"""


result = cursor.execute(query)


for row in result.fetchall():
    print(row)


#conn.close()


# In[19]:


df.to_sql("data", conn, if_exists="replace", index=False)


query = """
SELECT 
    Country, 
    SUM(Quantity * UnitPrice) AS TotalSales, 
    AVG(Quantity * UnitPrice) AS AvgOrderValue
FROM data
GROUP BY Country;


"""


result = cursor.execute(query)


for row in result.fetchall():
    print(row)


# In[20]:


df.to_sql("data", conn, if_exists="replace", index=False)


query = """
CREATE VIEW country_sales_summary AS
SELECT 
    Country, 
    SUM(Quantity * UnitPrice) AS TotalSales,
    COUNT(DISTINCT InvoiceNo) AS TotalOrders
FROM data
GROUP BY Country;


"""


result = cursor.execute(query)


for row in result.fetchall():
    print(row)


# In[24]:


import sqlite3

# Connect to the database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create indexes one at a time
cursor.execute("CREATE INDEX IF NOT EXISTS idx_country ON data(Country);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_invoice_date ON data(InvoiceDate);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_stockcode_customerid ON data(StockCode, CustomerID);")

print(conn)


print(" Indexes created successfully.")



# In[ ]:




