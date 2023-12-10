# SteamMonitor
Python script to monitor the status of a user.

## Requirements
- Python 3.x or higher. [Download](https://www.python.org/downloads/)

## Install
1. Clone the repository by git
    ```bash
    git clone https://github.com/Cryptinum/SteamMonitor.git
    ```

2. Install requirements by pip
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
- Configue all options in file SteamMonitor.py
- Change `steamID` to the ID of a user you want to monitor, the status of the user needs to be public.
- Change `period` to the time period you want to monitor, its unit is minute.

## Run
- Add python to environment variables (usually auto added after install Python), then run the line below in cmd at the script path.
    ```bash
    python SteamMonitor.py
    ```

## Note
- This script will create two logs, one is for saving status for every minutes, another is for saving status when the user status changes. Both logs are in .csv format.
- Not recommended to change period to less than 1, as it may lead to request failure.

## Disclaimer
- Only for educational purpose. Do not use it for illegal activities.
