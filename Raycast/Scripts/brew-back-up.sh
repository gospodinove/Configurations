#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Brew back up
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description Back up current Homebrew bundle
# @raycast.author Emanuil
# @raycast.authorURL https://github.com/gospodinove

brew bundle dump --file=~/Projects/Configurations/Brewfile --force

echo "Backed up!"
