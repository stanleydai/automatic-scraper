#!/usr/bin/env python
# coding: utf-8

# In[1]:


#scraping bbc


# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


response = requests.get("https://www.bbc.com/")
doc = BeautifulSoup(response.text)


# In[12]:


titles = doc.select(".media__title a")


# In[10]:


for title in titles:
    print((title.text).strip())


# In[17]:


for title in titles:
    print((title.text).strip())
    print(title['href'])


# In[25]:


import pandas as pd

rows = []

for title in titles:
    row = {}
    # title
    row['title'] = title.text.strip()
    #link
    row['url'] = title['href']
    
    rows.append(row)

df = pd.DataFrame(rows)
df


# In[26]:


df.to_csv("bbc.csv", index = False)


# In[ ]:




