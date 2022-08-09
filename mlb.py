import statsapi
import datetime
now = datetime.datetime.now()
rookie = statsapi.league_leaders('homeRuns',season=2022,playerPool = 'rookies', limit=10)
print(now)
print(f"Rookie Home Run Leaders\n{rookie}")