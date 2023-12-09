# SteamMonitor
Python script to monitor the status of a user.

## Requirements
- Python 3.x or higher. [Download](https://www.python.org/downloads/)
- Jupyter if you want to use .ipynb version
    ```bash
    pip install jupyter
    ```

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
- Change `steamID` to the ID of a user you want to monitor, the status of the user should be public.
- Change `period` to the time period you want to monitor, its unit is minute.

## Run
- Add python to environment variables (usually auto added after install Python). Run the line below in cmd in the script path.
    ```bash
    python SteamMonitor.py
    ```

## Note
- There is also a .ipynb version for Jupyter user.
- This script will create two logs, one is for save status for every minutes, another is for save status when the user status changes. Both logs are in .csv format.
- Not recommended to change period less than 1, as it may lead to request failure.

## Disclaimer
- Only for educational purpose. Do not use it for illegal activities.
