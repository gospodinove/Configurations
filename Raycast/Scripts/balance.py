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

cash = float(sys.argv[1])
revolut = float(sys.argv[2])
bank = float(sys.argv[3])

# TODO: Figure out how to get the target from Spendee

print("Your balance is: {:.2f} BGN".format(cash + revolut + bank))
