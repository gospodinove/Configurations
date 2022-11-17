#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title NBA Teams
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🏀

# Documentation:
# @raycast.description Get the next games of your favorite NBA teams
# @raycast.author Emanuil
# @raycast.authorURL https://github.com/gospodinove

from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.static import teams
import pandas as pd
import datetime

teams = teams.get_teams()

# add one day due to the time difference between USA and BG
def localize_date(date):
  return date + datetime.timedelta(days=1)

def get_last_team_game_date(team_id):
  games = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id).get_data_frames()[0]
  date_raw = games['GAME_DATE'][0]
  return datetime.datetime.strptime(date_raw, '%Y-%m-%d')

def get_last_team_game_date_localized(team_id):
  game_date = get_last_team_game_date(team_id)
  return localize_date(game_date)

def is_today(date):
  return date.date() == datetime.datetime.today().date()

def is_yesterday(date):
  yesterday = datetime.datetime.today() - datetime.timedelta(days = 1)
  return date.date() == yesterday.date()

def format_date(date):
  if (is_today(date)):
    return 'Today'

  if (is_yesterday(date)):
    return 'Yesterday'

  return date.strftime("%d %b")

favorite_teams = ['GSW', 'BKN', 'MEM']

for team in teams:
  if team['abbreviation'] in favorite_teams:
    team_last_game = get_last_team_game_date_localized(team['id'])
    print(f"{team['abbreviation']}: {format_date(team_last_game)}")
