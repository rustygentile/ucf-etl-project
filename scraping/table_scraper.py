from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
from splinter import Browser
import datadotworld as dw
import time 


# Open URL list from DataWorld and iterate one by through the urls.
dw_csv = dw.load_dataset('rustygentile/ncaa-etl-2018', force_update=True)
url_list = dw_csv.dataframes['game_urls_2018_active']
url_list.head()
for url in url_list['urls']:
    url = url + '/boxscore'
    print(url)

    # Use chrome driver to execute path and load url into the chrome driver to launch site. 
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    #url = "https://www.ncaa.com/game/basketball-men/d1/2018/03/22/kansas-st-kentucky/boxscore"
    browser.visit(url)
    browser.driver.set_window_size(3840, 2160)

    # record HTML of website into variable. 
    html = browser.html
    #response = requests.get(url)
    soup = BeautifulSoup(html, 'lxml')
    tables = pd.read_html(html)
    away_table = tables[1]
    away_table

    # Locate away team class and pull name
    away_active = soup.find_all('div', class_='boxscore-team-selector-team awayTeam-bg-primary_color homeTeam-border-primary_color away active')
    away_team = away_active[0].text.strip()
    print(f'!!!!!!!!!!!!!!!!!!!!!AWAY TEAM: {away_team} !!!!!!!!!!!!!!') 
    game_score = tables[0]

    # Close browser.
    browser.quit()

    # Reload site to get home team on second tab of table. 
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    browser.driver.set_window_size(3840, 2160)
    print('Sleeping 10 seconds......')
    time.sleep(10)
    print(url)

    # Find class for home team. 
    elems = browser.find_by_css('div[class="boxscore-team-selector-team homeTeam-bg-primary_color awayTeam-border-primary_color home"]')
    elems


    # Scroll the page down to activate the java script on page and the click the class. 
    # elems[0].click() is commented out because of an add that appeared on some of the pages.
    # we could not figure out how to compensate for the ad so when the program sleeps i'm manually
    # clicking the home team tab.
    browser.execute_script("window.scrollTo(0, 200)")
    #elems[0].click()
    html = browser.html

    #response = requests.get(url)
    soup = BeautifulSoup(html, 'lxml')
    home_active = soup.find_all('div', class_='boxscore-team-selector-team homeTeam-bg-primary_color awayTeam-border-primary_color home active')

    print(f'ERROR CATCH: {home_active}')
    home_team = home_active[0].text.strip()
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! HOME TEAM: {home_team} !!!!!!!!!!!!!!!')


    # Re-store html for launched page in the google drive. HTML now contains the home team table data. 
    # Read the table from the html and store in variable. 
    html = browser.html
    tables = pd.read_html(html)
    home_table = tables[1]
    home_table

    # Print game score table. 
    game_score

    # Clean URL to pull team vs team match name and create varaible containing appropriate names
    # per team. 
    cleaned_url = url.split('/d1/')[1].replace('/', "_").replace('-', '_')

    home_csv = cleaned_url + '_' + home_team + '.csv'
    away_csv = cleaned_url + '_' + away_team + '.csv'
    game_csv = cleaned_url + '_game_results' + '.csv'

    # To use these remove to + .csv from the variables above. 
    #home_table.to_csv('game_htmls/' + home_csv + '.csv')
    #away_table.to_csv('game_htmls/' + away_csv + '.csv')
    #game_score.to_csv('game_htmls/' + game_csv + '.csv')

    # Close browser.
    browser.quit()
    # Write csv's to Data.World. 
    with dw.open_remote_file('rustygentile/ncaa-etl-2018', home_csv) as w:
        home_table.to_csv(w, index=False)
        
    with dw.open_remote_file('rustygentile/ncaa-etl-2018', away_csv) as w:
        away_table.to_csv(w, index=False)

    with dw.open_remote_file('rustygentile/ncaa-etl-2018', game_csv) as w:
        game_score.to_csv(w, index=False)


