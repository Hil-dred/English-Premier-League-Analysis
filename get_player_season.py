import pandas as pd

def get_season_csv(file: str, year: str, position: str):
    season = pd.read_csv(file)
    season = season.groupby(season['Season'])
    season = season.get_group(year)
    season = season.groupby(season['Position']).get_group(position)
    return season

def get_new_columns(position:str, season):
    season['OVR'] = season['OVR(%)']
    if position == 'FW' :
        season["goals_Rank"] = season['Goals'].rank(pct=True)
        season["passes_Rank"] = season['Passes'].rank(pct=True)
        season["assits_Rank"] = season['Assists'].rank(pct=True)
        season["SOT_Rank"] = season['SOT'].rank(pct=True)
        season["HeadGoal_Rank"] = season['HeadGoal'].rank(pct=True)
        season['shots_Rank'] = season['Shots'].rank(pct=True)
        print(type(season))
        for i in range(len(season)):
            season['OVR'].iloc[i] = int((season['goals_Rank'].iloc[i]*0.35 +  season['assits_Rank'].iloc[i]*0.2 + season['passes_Rank'].iloc[i]*0.1 + season['SOT_Rank'].iloc[i]*0.25+ season['shots_Rank'].iloc[i]*0.1 + season['HeadGoal_Rank'].iloc[i]*0.1)*100)

    if position == 'MF' :
        season["goals_Rank"] = season['Goals'].rank(pct=True)
        season["passes_Rank"] = season['Passes'].rank(pct=True)
        season["assits_Rank"] = season['Assists'].rank(pct=True)
        season["Interceptions_Rank"] = season['Interceptions'].rank(pct=True)
        season["Crosses_Rank"] = season['Crosses'].rank(pct=True)
        season["ThrBall_Rank"] = season['ThrBall'].rank(pct=True)
        print(type(season))

        for i in range(len(season)):
            season['OVR'].iloc[i] = int((season['goals_Rank'].iloc[i]*0.1 + season['assits_Rank'].iloc[i]*0.2 + season['passes_Rank'].iloc[i]*0.3 + season['Interceptions_Rank'].iloc[i]*0.2+ season['Crosses_Rank'].iloc[i]*0.1+ season['ThrBall_Rank'].iloc[i]*0.1)*100)

    if position == 'DF' :
        season["goals_Rank"] = season['Goals'].rank(pct=True)
        season["passes_Rank"] = season['Passes'].rank(pct=True)
        season["Blocks_Rank"] = season['Blocks'].rank(pct=True)
        season["Interceptions_Rank"] = season['Interceptions'].rank(pct=True)
        season["Tackles_Rank"] = season['Tackles'].rank(pct=True)
        season["Clears_Rank"] = season['Clears'].rank(pct=True)

        for i in range(len(season)):
            season['OVR'].iloc[i] = int((season['goals_Rank'].iloc[i]*0.05 +  season['Blocks_Rank'].iloc[i]*0.25 + season['passes_Rank'].iloc[i]*0.1 + season['Interceptions_Rank'].iloc[i]*0.15+season['Tackles_Rank'].iloc[i]*0.25 +season['Clears_Rank'].iloc[i]*0.2)*100)
    
    return season

def player_season_score(file: str, player: str, year: str, position: str) -> int:
    '''
    player -> Name of the Player
    season -> Season to find its rating
    position -> Position played 
    '''
    analysedYear = get_season_csv(file=file, year=year, position=position)
    players = get_new_columns(position, analysedYear)
    player_row= players.loc[players['Player'] == player]
    return player_row['OVR']

if __name__ == '__main__':
   a = player_season_score(file='OVR_data.csv', player="N'Golo Kanté", year= '2016-2017', position='MF')
   print(a)