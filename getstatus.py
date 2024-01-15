from bs4 import BeautifulSoup


def forteenDaysTotal(soup):
    """Total game time in last 14 days, 0 if fail to get element."""
    source = soup.find_all("div", class_="recentgame_quicklinks recentgame_recentplaytime")
    return float(source[0].text.strip()[:-19]) if source else 0.0


def statusNow(soup):
    """Current status."""
    source = soup.find_all("div", class_="profile_in_game_header")
    return source[0].text.strip() if source else ""


def gameNow(soup):
    """Current game, empty string if fail to get element (no game playing)."""
    source = soup.find_all("div", class_="profile_in_game_name")
    return source[0].text.strip() if source else ""

def getIcon(soup):
    """Reture the url of user's avatar if avaliable, else Steam icon."""
    source = soup.find_all("div", class_="playerAvatarAutoSizeInner")
    return source[0].find_all("img")[-1]['src'] if source else "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Steam_icon_logo.svg/512px-Steam_icon_logo.svg.png"