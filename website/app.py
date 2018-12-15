# Importing Dependencies
import pandas as pd
from flask import Flask, render_template, redirect, make_response,request, jsonify
import os
import json
from flask_pymongo import PyMongo


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine, func
#################################################
# Database Setup
#################################################
# Web sites use threads, but sqlite is not thread-safe.
# These parameters will let us get around it.
# However, it is recommended you create a new Engine, Base, and Session
#   for each thread (each route call gets its own thread)
engine = create_engine("sqlite:///static/Resources/ncaa_Rank_Seed2018.sqlite",
    connect_args={'check_same_thread':False},
    poolclass=StaticPool)
#################################################



# Relect the existing database into a new model.

Base = automap_base()

# Reflect the table.

Base.prepare(engine, reflect=True)

# Save a reference to the ranks table as "Ranks".

Ranks = Base.classes.ranks

# Save a reference to the seeds table as "Seed".

Seeds = Base.classes.seeds

# Create our session link from Python to the database.

session = Session(engine)
######################
# Create an instance of Flask
app = Flask(__name__, static_url_path='/static')

# Read all the data for all 4 regions
east_team = json.load(open('static/Resources/east_teams.json'))
west_team = json.load(open('static/Resources/west_teams.json'))
midwest_team = json.load(open('static/Resources/midwest_teams.json'))
south_team = json.load(open('static/Resources/south_teams.json'))

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/four_app")
######################
# Route to render index.html
@app.route("/")
def home():

   return render_template("index.html")
#--------------------
# Route to render east.html template using json data
@app.route("/east")
def east_region():

   return render_template("east.html",east_team=east_team)
#--------------------
# Route to render west.html template using json data
@app.route("/west")
def west_region():

   return render_template("west.html",west_team=west_team)
#--------------------
# Route to render south.html template using json data
@app.route("/south")
def south_region():

   return render_template("south.html",south_team=south_team)
#--------------------
# Route to render midwest.html template using json data
@app.route("/midwest")
def midwest_region():

   return render_template("midwest.html",midwest_team=midwest_team)
#--------------------
# Route to render bracket.html: display the full bracket of all teams
@app.route("/bracket")
def bracket():

   return render_template("bracket.html")
#--------------------
# Route to render table.html: Display the raw data from csv file
@app.route("/table")
def data():

   return render_template("table.html")
#--------------------
# Route to render final_four.html template using data from Mongo
@app.route("/final_four")
def final_four():
   # Find one record of data from the mongo database
 

   return render_template("final_four.html")
#--------------------
# Route to render final.html template using csv data
@app.route("/finals")
def finals():

   return render_template("finals.html")
#-------------------
#--------------------
#error handler
@app.errorhandler(404)
def not_found(error):
   return make_response(jsonify({'error': 'Not found'}), 404)
#--------------------
@app.route("/API")
def mainapi():
    """List all available api routes."""
    return render_template("api_home.html")
#--------------------
@app.route("/api/2017/team_names")
def teamname():
    teams = []
    with open('static/Resources/team-list-2017.json') as json_data:
        team_test = json.load(json_data)
        for team in team_test:
            teams.append(team['name'])
        return jsonify(teams)

#--------------------
@app.route("/api/2017/team")
@app.route("/api/2017/team/<name>")
def team(name=None):
    if not name:
        with open('static/Resources/team-list-2017.json') as json_data:
            team_test = json.load(json_data)
            return jsonify(team_test)
    with open('static/Resources/team-list-2017.json') as json_data:
        team_test = json.load(json_data)
        for team in team_test:
            name = (' ').join(name.split('%20'))
            if team['name'] == name:
                return jsonify(team)

#--------------------
@app.route("/api/2017/player_names")
def playernames():
    names = []
    with open('static/Resources/player-list_2017.json') as json_data:
        player_test = json.load(json_data)
        for player in player_test:
            names.append(player['Player_Name'])
        return jsonify(names)
#--------------------
@app.route("/api/2017/player")
@app.route("/api/2017/player/<name>")
def player(name=None):
    if not name:
        with open('static/Resources/player-list-full-2017.json') as json_data:
            player_test = json.load(json_data)
            return jsonify(player_test)
    with open('static/Resources/player-list-full-2017.json') as json_data:
            player_test = json.load(json_data)
            for player in player_test:
                name = (' ').join(name.split('%20'))
                if player['name'] == name:
                    return jsonify(player)

################################## ELITE 8 2018 Routes ##################################
@app.route("/api/2018/elite_player_names")
def elite_players():
    with open('static/Resources/player_stats-elite_eight-2018.json') as json_data:
        elite = json.load(json_data)
        names = []
        for player in elite:
            names.append(player['name'])
        return jsonify(names)
#--------------------
@app.route("/api/2018/elite_eight")
@app.route("/api/2018/elite_eight/<name>")
def elite(name=None):
    if not name:
        with open('static/Resources/player_stats-elite_eight-2018.json') as json_data:
            elite = json.load(json_data)
            return jsonify(elite)
    with open('static/Resources/player_stats-elite_eight-2018.json') as json_data:
        elite_player = json.load(json_data)
    for player in elite_player:
        name = (' ').join(name.split('%20'))
        if name == player['name']:
            return jsonify(player)
#--------------------
@app.route("/api/2018/championship")
def champ():
    with open('static/Resources/team_stats-full-2018_championship.json') as json_data:
        elite = json.load(json_data)
        return jsonify(elite)    
#--------------------
####  Team Seeding and Player's Rank till 12/13/2018 ###########
#Region with seeds 
@app.route("/api/2018/Seeds_region/<region>")
#Return a JSON list for all the teams in that region with seeding
def region_result(region):
    # input the region name
    region_name  = region.replace(" ","")
    region_upper =region_name.upper()
    print(region_upper)
    # Read the region
    results = session.query(Seeds.Seed, Seeds.Name).filter(Seeds.Region == region_upper).\
    order_by(Seeds.Seed.asc()).all()
    
    return(jsonify(results))  
#-------------------- 
#Top 254 Player till 12/13/2018: 
@app.route("/api/2018/player_rank/<top_number>")
#Return a JSON list for all the teams in that region with seeding
def top_result(top_number):
    # input and read  the count for top player
    top_rank = int(top_number)
    rank_results = session.query(Ranks.Rank, Ranks.Name, Ranks.PTS).limit(top_rank).all()
    
    return(jsonify(rank_results))   
###################### End #########################
if __name__ == "__main__":
    app.run(debug=True)
