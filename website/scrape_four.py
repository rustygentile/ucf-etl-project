from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit NCAA site
    url = ('https://www.ncaa.com/news/basketball-men/article/2018-04-13/2018-ncaa-tournament-and-final-four-viewership-attendance')
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Find the src for the final four info image
    four_final =soup.find('div',class_='inline-left')
    four_final_photo = four_final.find_all('img')
    #read the link
    for link in  four_final_photo:
        infographic_link = link['src']

    # Store data in a dictionary
    four_data = {
        "four_info": infographic_link
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return four_data
