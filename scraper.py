import os
import json

data = {}
filename = "loginInfo.json"
supported_sites = ["purewage.com", "ibet.ag", "everysport247.com", "betallweek.com"]
supported_sports = ["football", "basketball"]

def generate_login_info():
    # purewage.com
    purewage_username = input("Please enter your username for purewage.com: ")
    purewage_password = input("Please enter your password for purewage.com: ")
    purewage_dict = {"username":purewage_username, "password":purewage_password}
    data["purewage.com"] = purewage_dict
    print()
    # ibet.ag
    ibet_username = input("Please enter you username for ibet.ag: ")
    ibet_password = input("Please enter you password for ibet.ag: ")
    ibet_dict = {"username":ibet_username, "password":ibet_password}
    data["ibet.ag"] = ibet_dict
    print()
    # everysport247.com
    everysport247_username = input("Please enter you username for everysport247.com: ")
    everysport247_password = input("Please enter you password for everysport247.com: ")
    everysport247_dict = {"username":everysport247_username, "password":everysport247_password}
    data["everysport247.com"] = everysport247_dict
    print()
    # betallweek.com
    betallweek_username = input("Please enter you username for betallweek.com: ")
    betallweek_password = input("Please enter you password for betallweek.com: ")
    betallweek_dict = {"username":betallweek_username, "password":betallweek_password}
    data["betallweek.com"] = betallweek_dict
    print()
    # Creates JSON file
    with open(filename, "w") as fp:
        json.dump(data, fp, indent = 4)

# Script starts here
print("Sports Props Betting Scraper v1.0\n")
print("Sites supported: ")
for site in supported_sites:
    print(site)
print()
print("Sports supported: ")
for sport in supported_sports:
    print(sport)
print()

# If loginInfo.json exists
if (os.path.exists(filename) and os.path.getsize(filename) > 0):
    # If you want to make edits to login info
    while True:
        edits = input("Would you like to edit any of your login information? [Y/N]: ")
        print()
        if ("y" == edits.lower()):
            generate_login_info()
            break
        elif("n" == edits.lower()):
            break

    # Copies info from loginInfo.json into data dictionary
    with open(filename) as login_info:
        data = json.load(login_info)


# Else generate json file with login info
else:
    generate_login_info()

# Get data
while (True):
    sport = input("What sport? (Enter 'football' or 'basketball'): ")
    print()
    if (sport.lower() == "football" or sport.lower() == "basketball"):
        # purewage info import
        import pureWage
        purewage_data = pureWage.get_data(sport)
        purewage_datafile = open("./test/purewage_data.json", "w+")
        json.dump(purewage_data, purewage_datafile, indent = 4)

        # everysport247 info import
        import everysport247
        everysport247_data = everysport247.get_data(sport)
        #everysport247_datafile = open("./test/everysport247_data.json", "W+")
        #json.dump(everysport247_data, everysport247_datafile, indent = 4)

        #betallweek info import
        import betAllWeek
        betallweek_data = betAllWeek.get_data(sport)
        #betallweek_datafile = open("./test/betallweek_data.json", "W+")
        #json.dump(betallweek_data, betallweek_datafile, indent = 4)
        break
    else:
        print("Please enter either 'football' or 'basketball'\n")


input("Press enter to exit\n")
