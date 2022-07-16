#!/usr/bin/env python
# coding: utf-8

# # Scrape 
# 
# https://www.marylandpublicschools.org/stateboard/Pages/Meetings-2018.aspx (Links to an external site.)
# 
# Tier 1: Scrape the date, URL to agenda, URL to board minutes
# 
# Tier 2: Download agenda items to an "agendas" folder and board minutes to a "minutes" folder
# 

# In[81]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[82]:


response = requests.get("https://www.marylandpublicschools.org/stateboard/Pages/Meetings-2018.aspx")
doc = BeautifulSoup(response.text)


# In[83]:


print(doc.prettify())


# In[84]:


#find the highest category that contains all the info I want
tbody = doc.find("tbody")


# In[85]:


for url in tbody.find_all("a"):
    print(url)


# In[86]:


for url in tbody.find_all("a"):
    
    if "Agenda" in url["title"]:
        print(url["title"])
        print(url["href"])
    
    if "Minutes" in url["title"]:
        print(url["title"])
        print(url["href"])
    
        print ("----")


# In[87]:


#save that info - the dataframe as a list of dictionary
#complete the url
#!= is not
#[:-14] take 14 characters from the tail to be removed - without that, it shows the title of the url
#agenda = None / minutes = None are the empty variable to be filled when "if" is met
#"empty" these variable at the end of the thrid "if" to reset for the next row in the loop

urls = []

agenda = None
minutes = None

for url in tbody.find_all("a"):
    date = (url["title"][:-14])
    if "Agenda" in url["title"]:
        agenda = "https://www.marylandpublicschools.org" + (url["href"])
        
    if "Minutes" in url["title"]:
        minutes = "https://www.marylandpublicschools.org" + (url["href"])   
   

    if agenda != None and minutes != None:
        url = {
                "date": date,
                "agenda" : agenda,
                "minutes" : minutes
            }
        
        urls.append(url)
        
        agenda = None
        minutes = None
    
df = pd.DataFrame(urls)
df


# In[88]:


from urllib.request import urlretrieve


# In[89]:


#check the first dic of the list
urls[0]


# In[90]:


#urls is a list of dictionaries
#A/B: save to A folder with the file name B
# + is to concatenate
for info in urls:
    print("Downloading", info["agenda"])
    urlretrieve(info["agenda"], filename = "Agenda/" + info["date"])
    
    
    print("Downloading", info["minutes"])
    urlretrieve(info["minutes"], filename = "Minutes/" + info["date"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




