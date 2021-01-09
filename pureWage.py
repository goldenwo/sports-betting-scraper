import requests
from requests import get
from bs4 import BeautifulSoup
import json

with open("loginInfo.json") as f:
  login_info = json.load(f)

headers = {
    'authority': 'www.purewage.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'sec-ch-ua-mobile': '?0',
    'origin': 'https://www.purewage.com',
    'upgrade-insecure-requests': '1',
    'dnt': '1',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.purewage.com/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__cfduid=d9a8d3b1aa6573e08f3430ce18ff94dbf1608325317',
}

data = {
  'account': "error",
  'password': "error",
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
      'authority': 'www.purewage.com',
      'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
      'accept': '*/*',
      'dnt': '1',
      'x-requested-with': 'XMLHttpRequest',
      'sec-ch-ua-mobile': '?0',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'origin': 'https://www.purewage.com',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://www.purewage.com/wager/Sports.aspx?lid=2124',
      'accept-language': 'en-US,en;q=0.9',
      'cookie': '__cfduid=d9a8d3b1aa6573e08f3430ce18ff94dbf1608325317; ASP.NET_SessionId=d3ttri55rphu3t45wgncq145; pl=; ASPSESSIONIDCSCAQCDR=PLAONFECAPKKAGEIKMKFCOPO; ASPSESSIONIDSQCSDRRS=KCMJLEGALFICBNMPBBKJOKND; ASPSESSIONIDSQBRATRS=NPAAIADBLENMDPDBGOKPOGLG',
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

    response = requests.post(url, headers=url_headers, data=url_data)
  # If statement end

  #Basketball info
  elif ("basketball" == sport.lower()):
    url = "https://www.purewage.com/wager/betslip/getLinesbyLeague.asp"

    url_headers = {
        'authority': 'www.purewage.com',
        'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        'accept': '*/*',
        'dnt': '1',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.purewage.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.purewage.com/wager/Sports.aspx',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '__cfduid=d9a8d3b1aa6573e08f3430ce18ff94dbf1608325317; ASP.NET_SessionId=d3ttri55rphu3t45wgncq145; pl=; ASPSESSIONIDCSCAQCDR=PLAONFECAPKKAGEIKMKFCOPO; ASPSESSIONIDSQCSDRRS=KCMJLEGALFICBNMPBBKJOKND; ASPSESSIONIDSQBRATRS=NPAAIADBLENMDPDBGOKPOGLG; ASPSESSIONIDQQCTAQQS=BGGBHMPBPIMGEHDBGPKMKEBC; ASPSESSIONIDQQARQADS=JKBFAGODBDLIJLJILHJJICNB',
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

    response = requests.post(url, headers=url_headers, data=url_data)
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
    input()
    quit()

  return lines
# Function end
