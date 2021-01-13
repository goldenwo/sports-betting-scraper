import requests
from requests import get
from bs4 import BeautifulSoup
import json

with open("loginInfo.json") as f:
  login_info = json.load(f)

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}

data = {
  'account': login_info["purewage.com"]["username"],
  'password': login_info["purewage.com"]["password"],
  'btn_login': 'Login',
  'IdBook': '33,42,147,151'
}

# Login
login = "https://www.purewage.com/login.aspx"
s = requests.Session()
s.post(login, headers=headers, data=data)

# Get data
def get_data(sport):
  global response
  # Football info
  if ("football" == sport.lower()):
    url = "https://www.purewage.com/wager/betslip/getLinesbyLeague.asp"

    url_headers = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
      'cookie': '__cfduid=' + s.cookies.get_dict()['__cfduid'] + '; ASP.NET_SessionId=' + s.cookies.get_dict()['ASP.NET_SessionId'],
    }

    url_data = {
      'pid': '239216',
      'aid': '21276',
      'idp': '3123',
      'idpl': '4347',
      'idc': '97087093',
      'idlt': '1',
      'idls': '2',
      'idl': '2124',
      'nhll': 'C',
      'mlbl': 'N',
      'utc': '-5',
      'idlan': '0',
      'bid': '42'
    }

    response = s.post(url, headers=url_headers, data=url_data)
  # If statement end

  #Basketball info
  elif ("basketball" == sport.lower()):
    url = "https://www.purewage.com/wager/betslip/getLinesbyLeague.asp"

    url_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'cookie': '__cfduid=' + s.cookies.get_dict()['__cfduid'] + '; ASP.NET_SessionId=' + s.cookies.get_dict()['ASP.NET_SessionId'],
    }

    url_data = {
      'pid': '239216',
      'aid': '21276',
      'idp': '3123',
      'idpl': '4347',
      'idc': '99798398',
      'idlt': '1',
      'idls': 'E',
      'idl': '690',
      'nhll': 'C',
      'mlbl': 'N',
      'utc': '-5',
      'idlan': '0',
      'bid': '42'
    }

    response = s.post(url, headers=url_headers, data=url_data)
  # Else statement end

  # Save content
  content = response.content

  # Create soup
  soup = BeautifulSoup(content, features="lxml")

  rows = soup.find_all("div", class_="row")

  # Login info error checker
  if (rows is None):
    print("Error: Your login info for 'purewage.com' is incorrect\n")
    input()
    quit()

  lines = {}
  foundInfo = False

  for row in rows:
    player_info = row.find("div", class_="linesTeam row-offset-0 col-lg-4 col-md-4 col-sm-4 col-xs-12")
    bet = row.find("a", class_="btn btn-light btn-sm btn-block regular-line")
    if (player_info is not None and bet is not None):
      foundInfo = True
      player_info_string = " ".join(player_info.get_text().split())
      bet_string = bet.get_text().replace("\u00bd", "(1/2)")
      lines[player_info_string] = bet_string
    # If statement end
  # For loop end

  # Site change error checker
  if (foundInfo == False):
    print("Error: Either there are no player props for your selected sport at this time or this version of the scraper no longer supports 'purewage.com'\n")
    print("Data from purewage will not be added to the calculations.")

  return lines
# Function end
