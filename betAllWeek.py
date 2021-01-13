import requests
from requests import get
from bs4 import BeautifulSoup
import json

with open("loginInfo.json") as f:
    login_info = json.load(f)

login_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}

login_data = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '/wEPDwUKLTg5ODYzNjcwNmRkXszDJmhfnU5Qggm+1d5EGW7pMAA=',
    '__VIEWSTATEGENERATOR': 'C2EE9ABB',
    '__EVENTVALIDATION': '/wEWBgKS+4LCBAL4lt/gCgLHhaW/AwLIlrvGCgLZh4jSAQKMseCTDpiT7taRIGvGwZv/iPAWfED+shsz',
    'ctl00$MainContent$ctlLogin$_UserName': login_info["betallweek.com"]["username"],
    'ctl00$MainContent$ctlLogin$_Password': login_info["betallweek.com"]["password"],
    'ctl00$MainContent$ctlLogin$BtnSubmit': 'Login',
    'ctl00$MainContent$ctlLogin$_IdBook': '',
    'ctl00$MainContent$ctlLogin$Redir': '',
    'AgentName': login_info["betallweek.com"]["username"]
}

# Login
login = "https://backend.betallweek.com/login.aspx"
s = requests.Session()
s.post(login, headers=login_headers, data=login_data)

# Get data
def get_data(sport):
    global response
    # Football info
    if ("football" == sport.lower()):
        url = "https://backend.betallweek.com/wager/CreateSports.aspx"

        url_headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'cookie': 'SPSI=' + s.cookies.get_dict()['SPSI'] + '; SPSE=' + s.cookies.get_dict()['SPSE'] + '; UTGv2=' + s.cookies.get_dict()['UTGv2'] + '; spcsrf=' + s.cookies.get_dict()['spcsrf'],
        }

        params = (
            ('WT', '0'),
        )

        url_data = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': '/wEPDwUKLTg0MDMxOTM5NQ9kFgJmD2QWBAIBD2QWBmYPZBYYAgcPFgIeA3NyYwUVL01TL21zLWltZy5waHA/dD1sb2dvZAITDw8WAh4HVmlzaWJsZWdkZAIbDw8WAh8BaGRkAh0PDxYCHwFoZGQCIQ8PFgIfAWhkZAIlDxYCHwFoZAIzDw8WAh8BaGRkAjkPFgIeBFRleHQFBVFEMDA2ZAI9DxYCHwIFAjAgZAJBDxYCHwIFBDcwMCBkAkUPFgIfAgUCMCBkAkcPFgIfAWgWAgIDDxYCHwIFAjAgZAIBD2QWEgILDxYCHwIFBDcwMCBkAg8PFgIfAgUCMCBkAhMPFgIfAgUCMCBkAhUPFgIfAWhkAhcPFgIfAWgWAgIDDxYCHwIFAjAgZAIZDxYCHwIFBVFEMDA2ZAIdDxYCHgRocmVmBTBodHRwOi8vd3d3LmJldGFsbHdlZWsuY29tL3Nwb3J0c2Jvb2sucGhwP2xhbmc9ZW5kAh8PFgIfAwUuaHR0cDovL3d3dy5iZXRhbGx3ZWVrLmNvbS9yYWNlYm9vay5waHA/bGFuZz1lbmQCIQ8WAh8DBSxodHRwOi8vd3d3LmJldGFsbHdlZWsuY29tL2Nhc2luby5waHA/bGFuZz1lbmQCAg9kFg4CAQ8WAh8ABRUvTVMvbXMtaW1nLnBocD90PWxvZ29kAgsPDxYCHwFnZGQCEw8PFgIfAWhkZAIVDw8WAh8BaGRkAhkPDxYCHwFoZGQCHQ8PFgIfAWhkZAIlDw8WAh8BaGRkAgIPZBYCAgEPZBYGZg9kFggCAQ8PFgYeCENzc0NsYXNzBRpidG4tcHJvZ3Jlc3Mgcm91bmRlZC0wIGNvbB4LTmF2aWdhdGVVcmwFGX4vd2FnZXIvQ3JlYXRlU3BvcnRzLmFzcHgeBF8hU0ICAmRkAgMPDxYGHwQFIGJ0bi1wcm9ncmVzcyByb3VuZGVkLTAgY29sIHB1bHNlHwUFHn4vd2FnZXIvQ3JlYXRlU3BvcnRzLmFzcHg/V1Q9MB8GAgJkZAITDw8WBh8EBRFidG4gYnRuLXNlY29uZGFyeR8FBRl+L3dhZ2VyL0NyZWF0ZVNwb3J0cy5hc3B4HwYCAmRkAhUPDxYGHwQFDmJ0biBidG4tYWN0aXZlHwUFHn4vd2FnZXIvQ3JlYXRlU3BvcnRzLmFzcHg/V1Q9MB8GAgJkZAIBDxYCHwFnZAIMDxYCHwFnZGTxoa7z+z9bCuBk3IH7q1HrJ0Ix1A==',
            '__VIEWSTATEGENERATOR': '3DB83FCB',
            '__EVENTVALIDATION': '/wEWJwLhl5XQDQLw3aLWAwKgq/7iAQKxyJ2UCwL93/63BgL935KTDwL936buBwL937pJAv3fzqQJAv3f4v8BAv3f9toKAv3firYDAv3fnpEMAsfd7vcOAsbd7vcOAsXd7vcOAsTd7vcOAsPd7vcOAsLd7vcOAsHd7vcOAsDd7vcOAr/d7vcOAr7d7vcOAsfdgtMHAsbdgtMHAsXdgtMHAsTdgtMHAsPdgtMHAsLdgtMHAsHdgtMHAsDdgtMHAr/dgtMHAr7dgtMHAsfdli4Cxt2WLgLF3ZYuAt3m06QJAuqVhrQGAuuOzfEP6tf0umXZqbYQt1qLpFj9ri8RkpQ=',
            'lg_877': '877',
            'ctl00$WagerContent$btn_Continue': 'Continue',
            'ctl00$WagerContent$hidden_ResponsiveInput': '0',
            'AgentName': login_info["betallweek.com"]["username"]
        }

        response = s.post(url, headers=url_headers, params=params, data=url_data)
        print("Not implemented yet")
    # If statement end

    #Basketball info
    elif ("basketball" == sport.lower()):
        url = "https://backend.betallweek.com/wager/CreateSports.aspx"

        url_headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'cookie': 'SPSI=' + s.cookies.get_dict()['SPSI'] + '; SPSE=' + s.cookies.get_dict()['SPSE'] + '; UTGv2=' + s.cookies.get_dict()['UTGv2'] + '; spcsrf=' + s.cookies.get_dict()['spcsrf'],
        }

        params = (
            ('WT', '0'),
        )

        url_data = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': '/wEPDwUKLTg0MDMxOTM5NQ9kFgJmD2QWBAIBD2QWBmYPZBYYAgcPFgIeA3NyYwUVL01TL21zLWltZy5waHA/dD1sb2dvZAITDw8WAh4HVmlzaWJsZWdkZAIbDw8WAh8BaGRkAh0PDxYCHwFoZGQCIQ8PFgIfAWhkZAIlDxYCHwFoZAIzDw8WAh8BaGRkAjkPFgIeBFRleHQFBVFEMDA2ZAI9DxYCHwIFAjAgZAJBDxYCHwIFBDcwMCBkAkUPFgIfAgUCMCBkAkcPFgIfAWgWAgIDDxYCHwIFAjAgZAIBD2QWEgILDxYCHwIFBDcwMCBkAg8PFgIfAgUCMCBkAhMPFgIfAgUCMCBkAhUPFgIfAWhkAhcPFgIfAWgWAgIDDxYCHwIFAjAgZAIZDxYCHwIFBVFEMDA2ZAIdDxYCHgRocmVmBTBodHRwOi8vd3d3LmJldGFsbHdlZWsuY29tL3Nwb3J0c2Jvb2sucGhwP2xhbmc9ZW5kAh8PFgIfAwUuaHR0cDovL3d3dy5iZXRhbGx3ZWVrLmNvbS9yYWNlYm9vay5waHA/bGFuZz1lbmQCIQ8WAh8DBSxodHRwOi8vd3d3LmJldGFsbHdlZWsuY29tL2Nhc2luby5waHA/bGFuZz1lbmQCAg9kFg4CAQ8WAh8ABRUvTVMvbXMtaW1nLnBocD90PWxvZ29kAgsPDxYCHwFnZGQCEw8PFgIfAWhkZAIVDw8WAh8BaGRkAhkPDxYCHwFoZGQCHQ8PFgIfAWhkZAIlDw8WAh8BaGRkAgIPZBYCAgEPZBYGZg9kFggCAQ8PFgYeCENzc0NsYXNzBRpidG4tcHJvZ3Jlc3Mgcm91bmRlZC0wIGNvbB4LTmF2aWdhdGVVcmwFGX4vd2FnZXIvQ3JlYXRlU3BvcnRzLmFzcHgeBF8hU0ICAmRkAgMPDxYGHwQFIGJ0bi1wcm9ncmVzcyByb3VuZGVkLTAgY29sIHB1bHNlHwUFHn4vd2FnZXIvQ3JlYXRlU3BvcnRzLmFzcHg/V1Q9MB8GAgJkZAITDw8WBh8EBRFidG4gYnRuLXNlY29uZGFyeR8FBRl+L3dhZ2VyL0NyZWF0ZVNwb3J0cy5hc3B4HwYCAmRkAhUPDxYGHwQFDmJ0biBidG4tYWN0aXZlHwUFHn4vd2FnZXIvQ3JlYXRlU3BvcnRzLmFzcHg/V1Q9MB8GAgJkZAIBDxYCHwFnZAIMDxYCHwFnZGTxoa7z+z9bCuBk3IH7q1HrJ0Ix1A==',
            '__VIEWSTATEGENERATOR': '3DB83FCB',
            '__EVENTVALIDATION': '/wEWJwLhl5XQDQLw3aLWAwKgq/7iAQKxyJ2UCwL93/63BgL935KTDwL936buBwL937pJAv3fzqQJAv3f4v8BAv3f9toKAv3firYDAv3fnpEMAsfd7vcOAsbd7vcOAsXd7vcOAsTd7vcOAsPd7vcOAsLd7vcOAsHd7vcOAsDd7vcOAr/d7vcOAr7d7vcOAsfdgtMHAsbdgtMHAsXdgtMHAsTdgtMHAsPdgtMHAsLdgtMHAsHdgtMHAsDdgtMHAr/dgtMHAr7dgtMHAsfdli4Cxt2WLgLF3ZYuAt3m06QJAuqVhrQGAuuOzfEP6tf0umXZqbYQt1qLpFj9ri8RkpQ=',
            'lg_877': '877',
            'ctl00$WagerContent$btn_Continue': 'Continue',
            'ctl00$WagerContent$hidden_ResponsiveInput': '0',
            'AgentName': login_info["betallweek.com"]["username"]
        }

        response = s.post(url, headers=url_headers, params=params, data=url_data)
    # Else statement end

    # Save content
    content = response.content

    # Create soup
    soup = BeautifulSoup(content, features="lxml")

    info = soup.find_all("tbody")

    # Login info error checker
    if (info is None):
        print("Error: Your login info for 'purewage.com' is incorrect\n")
        input()
        quit()

    lines = {}

    test_file = open("./test/betAllWeek.html", "w+")
    test_file.write(soup.prettify())
    test_file.close()

    cookies_file = open("./test/betallweek_cookies.txt", "w+")
    cookies_file.write(json.dumps(s.cookies.get_dict(), indent=4))
    cookies_file.close()

# Function end
