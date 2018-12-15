# This application does not run in the actual app. This API is for building and testing
# the API routes.

import numpy as np
import pandas as pd
import json
from pprint import pprint
import datetime as dt
from jsonify import convert

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, redirect, url_for
from sqlalchemy.pool import StaticPool

# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
session = 'player-list-full-2017.csv'
#Base.prepare(engine, reflect=True)
# Save references to each table
#Measurement = Base.classes.measurement
#Station = Base.classes.station
# Create our session (link) from Python to the DB
#session = Session(engine)

app = Flask(__name__)
@app.route("/")
def main():
    return redirect("/api", code=302)

@app.route("/api")
def mainapi():
    title = 'List all available api routes.'
    """List all available api routes."""
    return (
        f"<h1 class = 'text-primary'>NCAA API Team and Player Search</h1>"
        f"<br>"
        f"<br>"
        f"Available API Routes:<br>"
        f"<br>"
        f"<br>" 
        f"<strong>/api/2017/team_names</strong><br>"
        f"- Display all of the team names for easy reference to search."
        f"<br>"
        f"<br>" 
        f"<strong>/api/2017/team</strong><br>"
        f"- Display all teams and available stats."
        f"<br>"
        f"<br>" 
        f"<strong>/api/2017/team/(name)</strong><br>"
        f"- Search for one particular team. Example: /api/v1.0/team/Florida%20St"
        f"<br>"
        f"<br>"       
        f"<strong>/api/2017/player_names</strong><br>"
        f"- Display all player names for easy reference to search."
        f"<br>"
        f"<br>"
        f"<strong>/api/2017/player</strong><br>"
        f"- Show all player stats." 
        f"<br>"
        f"<br>"
        f"<strong>/api/2017/player/name</strong><br>"
        f"- Search for one particular player. Example: http://127.0.0.1:5000/api/v1.0/player/Nigel%20Hayes."
        f"<br>"
        f"<br>" 
        f"<strong>/api/2018/elite_player_names</strong><br>"
        f"- Display player names for the 2018 elite 8."
        f"<br>"
        f"<br>"
        f"<strong>/api/2018/elite_eight</strong><br>"
        f"- Display all players in the elite 8 teams."
        f"<br>"
        f"<br>"
        f"<strong>/api/2018/elite_eight/(name)</strong><br>" 
        f"- Search for one particular player in one of the elite 8 teams"
        f"<br>"
        f"<br>"
        f"<strong>/api/2018/championship</strong><br>"
        f"<- display the team data for the championship final."
    )

@app.route("/api/2017/team_names")
def teamname():
    teams = []
    with open('team-list-2017.json') as json_data:
        team_test = json.load(json_data)
        for team in team_test:
            teams.append(team['name'])
        return jsonify(teams)


@app.route("/api/2017/team")
@app.route("/api/2017/team/<name>")
def team(name=None):
    if not name:
        with open('team-list-2017.json') as json_data:
            team_test = json.load(json_data)
            return jsonify(team_test)
    with open('team-list-2017.json') as json_data:
        team_test = json.load(json_data)
        for team in team_test:
            name = (' ').join(name.split('%20'))
            if team['name'] == name:
                return jsonify(team)


@app.route("/api/2017/player_names")
def playernames():
    names = []
    with open('player-list_2017.json') as json_data:
        player_test = json.load(json_data)
        for player in player_test:
            names.append(player['Player_Name'])
        return jsonify(names)

@app.route("/api/2017/player")
@app.route("/api/2017/player/<name>")
def player(name=None):
    if not name:
        with open('player-list-full-2017.json') as json_data:
            player_test = json.load(json_data)
            return jsonify(player_test)
    with open('player-list-full-2017.json') as json_data:
            player_test = json.load(json_data)
            for player in player_test:
                name = (' ').join(name.split('%20'))
                if player['name'] == name:
                    return jsonify(player)

################################## ELITE 8 2018 Routes ##################################
@app.route("/api/2018/elite_player_names")
def elite_players():
    with open('player_stats-elite_eight-2018.json') as json_data:
        elite = json.load(json_data)
        names = []
        for player in elite:
            names.append(player['name'])
        return jsonify(names)

@app.route("/api/2018/elite_eight")
@app.route("/api/2018/elite_eight/<name>")
def elite(name=None):
    if not name:
        with open('player_stats-elite_eight-2018.json') as json_data:
            elite = json.load(json_data)
            return jsonify(elite)
    with open('player_stats-elite_eight-2018.json') as json_data:
        elite_player = json.load(json_data)
    for player in elite_player:
        name = (' ').join(name.split('%20'))
        if name == player['name']:
            return jsonify(player)

@app.route("/api/2018/championship")
def champ():
    with open('team_stats-full-2018_championship.json') as json_data:
        elite = json.load(json_data)
        return jsonify(elite)    

if __name__ == "__main__":
    app.run(debug=True)