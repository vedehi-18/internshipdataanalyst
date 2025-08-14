#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sqlite3


conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

sample_data = [
    ("Laptop", 5, 60000),
    ("Laptop", 3, 60000),
    ("Phone", 10, 20000),
    ("Phone", 6, 20000),
    ("Tablet", 4, 15000),
    ("Tablet", 5, 15000),
    ("Headphones", 8, 3000),
    ("Headphones", 12, 3000)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)


conn.commit()
conn.close()

print("sales_data.db created successfully with sample data!")


# In[7]:


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt



# In[10]:


conn = sqlite3.connect("sales_data.db")


query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""


df = pd.read_sql_query(query, conn)



print(df)



# In[9]:


plt.figure(figsize=(8,5))
plt.bar(df['product'], df['revenue'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.title('Revenue by Product')
plt.xticks(rotation=45)
plt.tight_layout()


plt.savefig("sales_chart.png")
plt.show()


conn.close()


# In[ ]:




