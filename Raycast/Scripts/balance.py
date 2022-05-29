#!/usr/bin/env python3

# Raycast Script Command Template
#
# Dependency: This script requires Python 3
# Install Python 3: https://www.python.org/downloads/release
#
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Balance
# @raycast.mode compact
# @raycast.packageName Raycast Scripts
# @raycast.argument1 { "type": "text", "placeholder": "Cash", "optional": false }
# @raycast.argument2 { "type": "text", "placeholder": "Revolut", "optional": false }
# @raycast.argument3 { "type": "text", "placeholder": "Bank", "optional": false }
#
# Optional parameters:
# @raycast.icon 🏦
# @raycast.currentDirectoryPath ~
# @raycast.needsConfirmation false
#
# Documentation:
# @raycast.description Check if my balance is actually what I have documented in Spendee
# @raycast.author Emanuil
# @raycast.authorURL https://www.github.com/gospodinove

import sys
import json
from spendee import Spendee


def format(number):
    return "BGN {:.2f}".format(number)


cash = float(sys.argv[1])
revolut = float(sys.argv[2])
bank = float(sys.argv[3])

balance = cash + revolut + bank

# file look-up starts at ~ (see line 19)
credentials_file = open(
    "Projects/Configurations/Raycast/Scripts/balance-credentials.json"
)
credentials = json.load(credentials_file)
credentials_file.close()

spendee = Spendee(email=credentials["email"], password=credentials["password"])

wallets = spendee.wallet_get_all()

target = None

for wallet in wallets:
    if wallet["name"] == "Main":
        # for some reason, there is a deficit of 2 in the wallet's balance
        target = round(wallet["balance"] + 2, 2)
        break

if target == None:
    print(f"No target. Your balance is {format(balance)}.")
elif target > balance:
    print(f"Track those {format(target - balance)}!")
elif target < balance:
    print(f"You are {format(balance - target)} in the clear!")
else:
    print("You are spot on!")
