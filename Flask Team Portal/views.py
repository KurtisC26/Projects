from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import  login_required, current_user
from .modles import Note
import json
import pandas as pd

from . import db

from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder,boxscorefourfactorsv2


views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
# @login_required
def home():

    nba_teams = teams.get_teams()
    current_user_team = [team for team in nba_teams if team['abbreviation'] == current_user.email][0]
    current_user_team_id = current_user_team['id']

    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=current_user_team_id)
    last_5_games = gamefinder.get_data_frames()[0]
    last_5_games = last_5_games.head(5)
    last_5_games = last_5_games[['GAME_DATE','MATCHUP','PTS',"FGA","FG3M","FG3A","FTA","TOV"]]
    last_5_games = last_5_games.sort_values(by="GAME_DATE", ascending=True)

    last_5_games["MATCHUP"] = last_5_games["MATCHUP"].str[4:]
    last_5_games["test"] = last_5_games["GAME_DATE"] + " " +last_5_games["MATCHUP"]
    
    
     

    three_made = last_5_games.FG3M.tolist()
    three_attempts = last_5_games.FG3A.tolist()
    turnovers = last_5_games.TOV.tolist()
    # games = last_5_games[['GAME_DATE']]
    games = last_5_games.test.tolist()

    
    
    table = boxscorefourfactorsv2.BoxScoreFourFactorsV2(1522100075).get_data_frames()[0]
    


    print(current_user.email)
    
    return render_template("home.html",tables=[table.to_html(classes='data')],titles=table.columns.values, user = current_user,turnovers=turnovers,games=games,three_attempts=three_attempts,three_made=three_made)




@views.route('/schedule',methods=['GET','POST'])
def schedule():

    nba_teams = teams.get_teams()
    current_user_team = [team for team in nba_teams if team['abbreviation'] == current_user.email][0]
    current_user_team_id = current_user_team['id']
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=current_user_team_id)
    games = gamefinder.get_data_frames()[0]
    games = games[games['SEASON_ID']=='22021']
    games = games[['SEASON_ID','GAME_ID','GAME_DATE','TEAM_NAME','MATCHUP','WL']]

    wins = games[games['WL']=='W']
    wins = wins[['GAME_ID']].count()
    loses = games[games['WL']=='L']
    loses = loses[["GAME_ID"]].count()
    

    return render_template('schedule.html',user=current_user, tables=[games.to_html(classes='data')],titles=games.columns.values, wins=wins,loses=loses)




@views.route('/team-tracking',methods=['GET','POST'])
def team_salary():
    return render_template('track_stats_team.html',user=current_user)

@views.route('/post-game-report',methods=['GET','POST'])
def post_game():
    nba_teams = teams.get_teams()
    current_user_team = [team for team in nba_teams if team['abbreviation'] == current_user.email][0]
    current_user_team_id = current_user_team['id']

    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=current_user_team_id)
    last_game = gamefinder.get_data_frames()[0]
    last_game = last_game.head(1)
    last_game_id = last_game['GAME_ID']
    last_game_date = last_game["GAME_DATE"][0]
    last_game_matchup = last_game["MATCHUP"][0]
    last_game_points = last_game["PTS"][0]
    last_game_diff = last_game["PLUS_MINUS"][0]
    opponent_score = last_game_points+last_game_diff
    
    table = boxscorefourfactorsv2.BoxScoreFourFactorsV2(last_game_id).get_data_frames()[0]
    table = table[table["TEAM_ID"]==current_user_team_id]
    table = table[["PLAYER_NAME","START_POSITION","MIN","EFG_PCT","FTA_RATE","TM_TOV_PCT","OREB_PCT","OPP_EFG_PCT","OPP_FTA_RATE","OPP_TOV_PCT","OPP_OREB_PCT"]]
    return render_template('post_game_report.html',user=current_user,opponent_score=opponent_score, last_game_points=last_game_points,matchup = last_game_matchup, last_game_date = last_game_date, tables=[table.to_html(classes='data')],titles=table.columns.values)



@views.route('/delete-note', methods=["POST"])
def delete_note():
    note_data = json.loads(request.data)
    noteId = note_data['noteID']   
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})




