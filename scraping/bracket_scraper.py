# Dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datadotworld as dw


bracket_url = 'https://www.ncaa.com/brackets/basketball-men/d1/2018'
bracket_html = requests.get(bracket_url)

# Soup setup
soup = BeautifulSoup(bracket_html.text, 'html.parser')

# Get all the urls
urls = []
for a in soup.find_all('a', href=True):
    urls.append(a['href'])


# Filter out the games and export
base_game_url = "https://www.ncaa.com"
game_urls = []
for url in urls:
    if '/game/basketball-men/' in url:
        game_urls.append(f'{base_game_url}{url}')

game_urls_df = pd.DataFrame({'urls': game_urls})

with dw.open_remote_file('rustygentile/ncaa-etl', 'game_urls_2018.csv') as w:
    game_urls_df.to_csv(w, index=False)
