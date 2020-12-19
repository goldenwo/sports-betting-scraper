import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import json

login_info = {}
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
  'account': login_info["username"],
  'password': login_info["password"],
  'btn_login': 'Login',
  'IdBook': '33,42,147,151'
}


url = "https://www.purewage.com/login.aspx"

s = requests.Session()

response = s.post(url, headers=headers, data=data)
