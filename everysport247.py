import requests
from requests import get
from bs4 import BeautifulSoup
import json

with open("loginInfo.json") as f:
  login_info = json.load(f)

login_headers = {
    'authority': 'everysport247.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'sec-ch-ua-mobile': '?0',
    'origin': 'https://everysport247.com',
    'upgrade-insecure-requests': '1',
    'dnt': '1',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'empty',
    'referer': 'https://everysport247.com/Common/Dashboard',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__cfduid=d50a524b1b06496bf220e3b111a0d5c271608349604; ASP.NET_SessionId=ht0czcbgvijgqp52um553pzy',
    'Referer': '',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Origin': 'chrome-extension://hdokiejnpimakedhajhdlcegeplioahd',
    'x-requested-with': 'XMLHttpRequest',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/plain, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'If-None-Match': '"eBsX1miKkVOhCepUWBu886yVJN4="',
}

login_data = {
  'UserName': login_info["everysport247.com"]["username"],
  'Password': login_info["everysport247.com"]["password"],
  'BetType': '0'
}

# Login
login = "https://everysport247.com/Security/ValidateCredentials"
s = requests.Session()
s.post(login, headers=login_headers, data=login_data)

# Get data
def get_data(sport):
  global response
  # Football info
  if ("football" == sport.lower()):
    print("Not implemented yet")
  # If statement end

  #Basketball info
  elif ("basketball" == sport.lower()):
    url = "https://everysport247.com/Betting/Betting/DefaultGetScheduleDetails"

    url_headers = {
      'authority': 'everysport247.com',
      'cache-control': 'no-cache',
      'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
      'sec-ch-ua-mobile': '?0',
      'dnt': '1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
      'accept': '*/*',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-user': '?1',
      'sec-fetch-dest': 'empty',
      'referer': 'https://everysport247.com/Common/Dashboard',
      'accept-language': 'en-US,en;q=0.9',
      'cookie': '__cfduid=d50a524b1b06496bf220e3b111a0d5c271608349604; ASP.NET_SessionId=wo0tsxttyt5ocbmwyqqeizqh',
      'Referer': 'https://everysport247.com/Content/Css/teamlogos.css?v=205',
      'DNT': '1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
      'Origin': 'https://everysport247.com',
      'x-requested-with': 'XMLHttpRequest',
      'pragma': 'no-cache',
      'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
      'X-Requested-With': 'XMLHttpRequest',
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'origin': 'https://everysport247.com',
    }

    url_data = {
      'BetType': '0',
      'Array': 'MTY0LDE2NSwxMjczLDEwOTEsMTQ3MCwxMjU2LDE2NzYsODU1LDEwMTksMTQ4MQ==',
      'TeaserType': '-1'
    }

    response = requests.post(url, headers=url_headers, data=url_data)
  # Else statement end

  # Save content
  content = response.content

  # Create soup
  soup = BeautifulSoup(content, features="lxml")

  test_file = open("./test/eversport247.html", "w+")
  test_file.write(soup.prettify())
  test_file.close()

  cards = soup.find_all(lambda tag: tag.name == "div" and tag.get("class") == ["card container-for-filter"])

  # Login info error checker
  if (cards is None):
    print("Error: Your login info for 'everysport247.com' is incorrect\n")
    input()
    quit()

  lines = {}
  foundInfo = False

  for card in cards:
    betItems = card.find("div", class_="bet-item")
    for item in betItems:
      player_info = item.find("div", class_="col-6 cl-rpy-2 cl-rpx-2")
      bet_info = item.find("div", class_="custom-control custom-checkbox cl-checkbox bmt")
      if (player_info is not None and bet_info is not None):
        foundInfo = True
        player_info_string = " ".join(player_info.get_text().split())
        bet_string = bet_info.get_text().replace("\u00bd", "(1/2)")
        lines[player_info_string] = bet_string
    # If statement end
  # For loop end

  # Site change error checker
  if (foundInfo == False):
    print("Error: Either there are no player props for your selected sport at this time or this version of the scraper no longer supports 'everysport247.com'\n")
    input()
    quit()

  return lines
# Function end
