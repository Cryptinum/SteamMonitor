import warnings, requests, time
from bs4 import BeautifulSoup
import platform

# import pandas as pd
# import numpy as np
from datetime import datetime

from getstatus import *

winTag = platform.system().lower() == 'windows' and platform.version()[0:2] in ['10', '11']
if winTag:
    from win11toast import toast

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

previousStatus = [None for _ in range(4)]

while True:
    try:
        # Request user page
        page = requests.get(url, headers=headers, verify=False)  # Do not verify
        page.encoding = "utf-8"
        soup = BeautifulSoup(page.text, "html.parser")

        if page.status_code == 200:
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            total = forteenDaysTotal(soup)
            status = statusNow(soup)
            game = gameNow(soup)
            nowStatus = [now, total, status, game]

            with open(steamID+'_StatusLog.csv','a', encoding='utf-8') as file:
                file.write(f'{now},{total},{status},{game}\n')
            if nowStatus[2:] != previousStatus[2:]:
                with open(steamID+'_ChangeLog.csv', 'a', encoding='utf-8') as changeFile:
                    changeFile.write(f'{previousStatus[0]},{previousStatus[1]},{previousStatus[2]},{previousStatus[3]}\n')
                    changeFile.write(f'{now},{total},{status},{game}\n')
                print(f'[{now}] total={total}, {status} - {game}')
                if winTag:
                    toast(f'Status changed', f'Now: {now}\n{status} - {game}\nLast 14 days: {total} h', icon=getIcon(soup), audio={'silent': 'true'},) # notify in win10/11 system
            else:
                print(f'[{now}] total={total}, {status} - {game}')
            previousStatus = nowStatus
        else:
            print(f'Failed to retrieve data for {steamID}. Status Code: {page.status_code}')

    except requests.exceptions.RequestException as e:
        print(f"Error occurred for {steamID}: {e}")
    time.sleep(period * 60)
