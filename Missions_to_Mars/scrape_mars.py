#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests


# In[2]:

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)



# Visit url
def scrape():

    browser = init_browser()

    mars_data = {}

    # going to nasa url
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('div', class_='content_title').text
    paragraph = soup.find('div', class_='article_teaser_body').text

    mars_data["title"] = title
    mars_data["paragraph"] = paragraph



# # JPL Mars Space Images

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    response = requests.get(url)
    data = response.text
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    soup.find_all(class_="carousel_items")
    tags = soup.find_all('div', class_='carousel_items')
    tags = soup.find('article')['style']
    new_img_url = tags.split("('", 1)[1].split("')")[0]
    featured_image_url = "https://www.jpl.nasa.gov" + new_img_url

    mars_data["featured_image_url"] = featured_image_url


     



    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)

    soup = BeautifulSoup(browser.html, 'html.parser')

    print(soup.prettify())

    
    mars = soup.find_all(class_='TweetTextSize')[0].text

    mars_data["mars"] = mars


# Mars Table URL 
    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    table_df = pd.read_html(url)[1]


    table_df.columns=["description", "value"]
    table_df.set_index('description', inplace=True)

    mars_data["table_df"] = table_df


# Mars hq images
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)



    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    soup.find_all('div', class_='item')




    soup.find_all('a', class_='itemLink product-item')
    




    names = soup.find_all("h3")





    hemisphere_image_urls = []
    for i in range (4):
        names = soup.find('h3')
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        half_url = soup.find('img', class_= 'wide-image')['src']
        new_title = soup.find('h2', class_='title')
        whole_url = 'https://astrogeology.usgs.gov' + half_url
        dict = {'title': new_title, 'whole_url': whole_url}
        hemisphere_image_urls.append(dict)

    mars_data["hemisphere_image_urls"] = hemisphere_images_url

    return mars_data








