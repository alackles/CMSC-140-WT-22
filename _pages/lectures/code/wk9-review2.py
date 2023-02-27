from pathlib import Path
import pandas as pd

filename = Path("./data/MLB_batting_raw_data.csv")

players = []
with open(filename) as f:
    for line in f.readlines():
        player_data = line.split(",")
        players.append(player_data)

players_pd = pd.read_csv(filename)

print(players_pd)
print(players_pd["team_abbrev"])
