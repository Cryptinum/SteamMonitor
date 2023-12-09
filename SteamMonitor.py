import warnings, requests
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np
from datetime import datetime
import ciso8601, time

# Steam ID for monitoring
steamID = "shiranaiwa"

# Global Settings
np.set_printoptions(suppress=True)
warnings.filterwarnings("ignore")  # Suppress warnings.
pd.options.display.max_rows = 10  # Display no more than 10 rows.

urlTemplate = "https://steamcommunity.com/id/{}"
url = urlTemplate.format(steamID)
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
page = requests.get(url, headers=headers, verify=False)  # Do not verify
page.encoding = "utf-8"
soup = BeautifulSoup(page.text, "html.parser")

# Current time
now = datetime.now()

print(now)
print(forteenDaysTotal(soup))
print(statusNow(soup))
print(gameNow(soup))

def forteenDaysTotal(soup):
    '''Total game time in last 14 days, 0 if fail to get element.'''
    source = soup.find_all("div", class_="recentgame_quicklinks recentgame_recentplaytime"    )
    return float(source[0].text.strip()[:-19]) if source else 0.0

def statusNow(soup):
    '''Current status.'''
    return soup.find_all("div", class_="profile_in_game_header")[0].text.strip()

def gameNow(soup):
    ''' Current game, empty string if fail to get element (no game playing).'''
    source = soup.find_all("div", class_="profile_in_game_name")
    return source[0].text.strip() if source else ""
