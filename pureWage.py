import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
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
while True:
  sport = input("What sport? (Enter 'football' or 'basketball'): ")
  print()
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
    break

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
    break

# Save content
content = response.content

# Create soup
soup = BeautifulSoup(content, features="lxml")

rows = soup.find_all("div", class_="row")

lines = {}

for row in rows:
  player_info = row.find("div", class_="linesTeam row-offset-0 col-lg-4 col-md-4 col-sm-4 col-xs-12")
  bet = row.find("a", class_="btn btn-light btn-sm btn-block regular-line")
  if (player_info is not None and bet is not None):
    bet_string = bet.get_text().replace("\u00bd", "(1/2)")
    lines[player_info.get_text()] = bet_string

def save_lines():
  file4 = open("./test/lines.json", "w+")
  json.dump(lines, file4)

