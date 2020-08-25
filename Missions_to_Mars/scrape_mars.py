from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

#Creating one dictionary to store all the information
mars_info = {}

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)



def scrape():
    ###########################
    #### Getting NASA NEWS ####
    ###########################
    
    # Visit NASA url
    nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(nasa_url)
    
    # Create a Beautiful Soup object
    news_html = browser.html
    news_soup = bs(news_html, 'html.parser')
    
    # Getting the Latest Title and paragraph
    latest_news = news_soup.find('ul', class_="item_list")
    news_title = latest_news.find('div', class_="content_title").find("a").text
    news_para = latest_news.find('div', class_="article_teaser_body").text
    
    #Dictionary info entry
    mars_info['news_title'] = news_title
    mars_info['news_paragraph'] = news_para
    
    
    ################################################
    #### JPL Mars Space Images - Featured Image #### 
    ################################################
    
    
    #Visit JPL url
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)
    
    # Create a Beautiful Soup object
    JPL_html = browser.html
    JPL_soup = bs(JPL_html, 'html.parser')
    
    # finding the image url
    image = JPL_soup.find("article")["style"].replace('background-image: url(','').replace(');', '')[1:-1]
    featured_image_url = url.replace("/spaceimages/?search=&category=Mars", '') + image
    
    #Dictionary info entry
    mars_info['featured_image_url'] = featured_image_url
    
    
    ####################
    #### MARS FACTS ####
    ####################
    
    
    #Visit Facts url
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    
    # Getting the table from the url
    table = pd.read_html(url)
    mars_facts = table[0]
    mars_facts.columns = ["Description", "Value"]
    facts_html = table_need.to_html("table.html")
    
    mars_info['tables'] = facts_html
    
    
    #########################
    #### Mars Hemisphere ####
    #########################
    
    
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)
    hemi_html = browser.html
    hemi_soup = bs(hemi_html, "html.parser")
    hemisphere_image_urls = []
    # Get all the hemispheres through items class
    items = hemi_soup.find_all("div", class_="item")
    clean_url = "https://astrogeology.usgs.gov"
    for item in items:
        #Getting the title
        title = item.find("h3").text
    
        #Getting the image
        image = item.find("a", class_="itemLink product-item")["href"]
        info_url = clean_url + image
        #Going into the info page
        browser.visit(info_url)
        html_info = browser.html
        soup_info = bs(html_info, "html.parser")
        big_image = soup_info.find("img", class_="wide-image")["src"]
        big_image_url = clean_url + big_image
        
        hemisphere_image_urls.append({"Titles": title, "image_url": big_image_url})
    
    mars_info['Hemisphere_Info'] = hemisphere_image_urls
    
    browser.quit()
    return mars_info
    
    
    
