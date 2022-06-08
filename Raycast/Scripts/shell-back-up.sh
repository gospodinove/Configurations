#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Shell back up
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description Back up current Homebrew bundle & NodeJS global packages
# @raycast.author Emanuil
# @raycast.authorURL https://github.com/gospodinove

brew bundle dump --file=~/Projects/Configurations/Brewfile --force

npm list --global --parseable --depth=0 | sed '1d' | awk '{gsub(/\/.*\//,"",$1); print}' > ~/Projects/Configurations/NodeJS/global-modules.txt

echo "Backed up!"
