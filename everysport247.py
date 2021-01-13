import requests
from requests import get
from bs4 import BeautifulSoup
import json

with open("loginInfo.json") as f:
  login_info = json.load(f)

login_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
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
    url = "https://everysport247.com/Betting/Betting/DefaultGetScheduleDetails"

    url_headers = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
      'cookie': '__cfduid=' + s.cookies.get_dict()['__cfduid'] + '; ASP.NET_SessionId=' + s.cookies.get_dict()['ASP.NET_SessionId'],
    }

    url_data = {
      'BetType': '0',
      'Array': 'MTY0LDE2NSwxMjczLDEwOTEsMTQ3MCwxMjU2LDE2NzYsODU1LDEwMTksMTQ4MQ==',
      'TeaserType': '-1'
    }

    response = s.post(url, headers=url_headers, data=url_data)

    print("Not implemented yet")
  # If statement end

  #Basketball info
  elif ("basketball" == sport.lower()):
    url = "https://everysport247.com/Betting/Betting/DefaultGetScheduleDetails"

    url_headers = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
      'cookie': '__cfduid=' + s.cookies.get_dict()['__cfduid'] + '; ASP.NET_SessionId=' + s.cookies.get_dict()['ASP.NET_SessionId'],
    }

    url_data = {
      'BetType': '0',
      'Array': 'MTY0LDE2NSwxMjczLDEwOTEsMTQ3MCwxMjU2LDE2NzYsODU1LDEwMTksMTQ4MQ==',
      'TeaserType': '-1'
    }

    response = s.post(url, headers=url_headers, data=url_data)
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
    print("Data from everysport247 will not be added to the calculations.")

  cookies_file = open("./test/everysport247_cookies.txt", "w+")
  cookies_file.write(json.dumps(s.cookies.get_dict(), indent=4))
  cookies_file.close()

  return lines
# Function end
