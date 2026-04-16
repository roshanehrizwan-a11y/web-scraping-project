#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[6]:


url = "https://www.worldometers.info/world-population/population-by-country/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print(response.status_code)


# In[7]:


soup = BeautifulSoup(response.text, "html.parser")


# In[8]:


table = soup.find("table")

print(table)


# In[9]:


rows = table.find_all("tr")


# In[12]:


header_row = table.find("tr")

headers = [th.text.strip() for th in header_row.find_all("th")]
print(headers)


# In[10]:


data = []

for row in rows[1:]:
    cols = row.find_all("td")

    if len(cols) > 0:
        data.append([col.text.strip() for col in cols])


# In[13]:


df = pd.DataFrame(data, columns=headers)

df.head()


# In[14]:


print(df.shape)
print(df.columns)
df.head()


# In[15]:


df = df.replace(",", "", regex=True)


# In[16]:


df.to_csv("world_population.csv", index=False)

