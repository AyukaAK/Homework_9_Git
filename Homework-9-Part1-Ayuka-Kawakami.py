#!/usr/bin/env python
# coding: utf-8

# # Scrape the following into CSV files. Each one is broken up into multiple tiers – the more you scrape the tougher it is!
# 
# https://www.congress.gov/members 
# 
# Tier 1: Scrape their name and full profile URL, and additional
# 
# Tier 2: Separate their state/party/etc into separate columns
# 
# Advanced: Scrape each person's actual data from their personal project

# In[11]:


#import what's needed
import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[12]:


response = requests.get('https://www.congress.gov/members')
doc = BeautifulSoup(response.text)
print(doc.prettify())


# In[30]:


#find the highest category that contains all the info I want
doc.find_all("li", class_="expanded")


# In[39]:


#because it's a list, do the for loop
for headline in doc.find_all("li", class_="expanded"):
    #name
    print (headline.find("span").text)
    #url
    print (headline.find("a")["href"])
    
    #another for loop inside the span to print each strong and span which are the details
    for span in headline.find_all("span", class_="result-item"):
        print (span.find("strong").text) 
        print (span.find("span").text) 
    print ("----")


# In[50]:


#save that info  - the dataframe as a list of dictionary
#complete the url
members = []

for headline in doc.find_all("li", class_="expanded"):
    name = (headline.find("span", class_="result-heading").text)
    url = (headline.find("a")["href"])

    if url.startswith('/'):
        url = "https://www.congress.gov" + url
    
    member = {
            'name' : name,
            'url': url,
        }
        
    for span in headline.find_all("span", class_="result-item"):
        x = (span.find("strong").text) 
        y = (span.find("span").text) 
        
        member[x]=y
        
    
    members.append(member)
    
df = pd.DataFrame(members)
df


# In[52]:


#check the first of the list in the column title
df.name[0]


# In[54]:


#get rid of the spaces in front of and the end of the title
df.name = df.name.str.strip()


# In[55]:


df.to_csv("congress_members.csv" , index=False)


# In[ ]:





# In[ ]:




