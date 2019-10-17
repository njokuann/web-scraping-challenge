#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests


# In[2]:


# Set chromedriver path
def browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)


# In[3]:



# Visit url
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[4]:

def soup(url):
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


# In[5]:


title = soup.find('div', class_='content_title').text
title


# In[6]:


paragraph = soup.find('div', class_='article_teaser_body').text
paragraph


# # JPL Mars Space Images

# In[100]:


# set chromedriver path
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[101]:


# visit url
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)


# In[102]:


response = requests.get(url)


# In[103]:


data = response.text


# In[104]:


# scrape browser
html = browser.html
soup = BeautifulSoup(html, 'html.parser')       


# In[105]:


soup.find_all(class_="carousel_items")


# In[106]:


tags = soup.find_all('div', class_='carousel_items')
tags


# In[107]:


tags = soup.find('article')['style']
tags


# In[108]:


new_img_url = tags.split("('", 1)[1].split("')")[0]
new_img_url


# In[109]:


featured_image_url = "https://www.jpl.nasa.gov" + new_img_url
featured_image_url


# # More Stuff

# In[110]:


# set chromedriver path
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[111]:


url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)


# In[112]:


soup = BeautifulSoup(browser.html, 'html.parser')


# In[113]:


print(soup.prettify())


# In[114]:


mars = soup.find_all(class_='TweetTextSize')[0].text
mars


# # Table Stuff

# In[115]:


# set chromedriver path
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[116]:


url = 'https://space-facts.com/mars/'
browser.visit(url)


# In[117]:


table_df = pd.read_html(url)[1]
table_df


# In[118]:


table_df.columns=["description", "value"]
table_df.set_index('description', inplace=True)
table_df


# # last stuff

# In[7]:


# set chromedriver path
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[8]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[9]:


# scrape browser
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


soup.find_all('div', class_='item')


# In[ ]:


soup.find_all('a', class_='itemLink product-item')


# In[ ]:


names = soup.find_all('h3')
names


# In[ ]:


titles = []
for name in names:
    name = soup.find('h3')
    names.append('h3')
titles


# In[ ]:


img_urls = []
for title in titles:
    browser.click_link_by_partial_text(title)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    img_urls.append(soup.find("div", class_="downloads").find("a")["href"])
img_urls


# In[ ]:




