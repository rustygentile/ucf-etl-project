from bs4 import BeautifulSoup
import time
import requests

def scrape_info():

    # Visit NCAA site
    url = ('https://www.ncaa.com/news/basketball-men/article/2018-04-13/2018-ncaa-tournament-and-final-four-viewership-attendance')

    # Scrape page into Soup
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")

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

    # Return results
    return four_data
