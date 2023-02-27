from pathlib import Path
import pandas as pd

filename = Path("./data/MLB_batting_raw_data.csv")

#players = []
#with open(filename) as f:
#    for line in f.readlines():
#        player_data = line.split(",")
#        players.append(player_data)
#
#players_pd = pd.read_csv(filename)

#print(players_pd)

teams = players_pd["team_abbrev"]
unique_teams = []

# Go through the list and if it's already in the list, don't do anything
for team in teams:
    if team in unique_teams:
        pass
    else:
        unique_teams.append(team)
unique_teams.sort()
print(unique_teams)

# use built-ins
print(sorted(pd.unique(teams)))

# use set
print(sorted(set(teams)))
