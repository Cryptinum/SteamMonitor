import warnings, requests, time
from bs4 import BeautifulSoup

# import pandas as pd
# import numpy as np
from datetime import datetime

from getstatus import *

# Global Settings
# np.set_printoptions(suppress=True)
warnings.filterwarnings("ignore")  # Suppress warnings.
# pd.options.display.max_rows = 10  # Display no more than 10 rows.

# User for monitoring
steamID = "shiranaiwa"
period = 1


urlTemplate = "https://steamcommunity.com/id/{}"
url = urlTemplate.format(steamID)
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

previousStatus = [None for _ in range(3)]

while True:
    try:
        # Request user page
        page = requests.get(url, headers=headers, verify=False)  # Do not verify
        page.encoding = "utf-8"
        soup = BeautifulSoup(page.text, "html.parser")

        if page.status_code is 200:
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            total = forteenDaysTotal(soup)
            status = statusNow(soup)
            game = gameNow(soup)
            nowStatus = [total, status, game]

            with open(steamID+'_StatusLog.csv','a') as file:
                file.write(f'{now},{total},{status},{game}\n')
            if nowStatus != previousStatus:
                with open(steamID+'_ChangeLog.csv', 'a') as changeFile:
                    changeFile.write(f'{now},{total},{status},{game}\n')
                print(f'[{now}],{total},{status} - {game}')
                previousStatus = nowStatus
            else:
                print(f'[{now}],{total},{status} - {game}')
        else:
            print(f'Failed to retrieve data for {steamID}. Status Code: {page.status_code}')

    except requests.exceptions.RequestException as e:
        print(f"Error occurred for {steamID}: {e}")
    time.sleep(period * 60)
