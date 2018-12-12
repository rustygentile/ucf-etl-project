from flask import Flask, render_template, redirect  
import os
import json


# Create an instance of Flask
app = Flask(__name__, static_url_path='/static')

# Read all the data for all 4 regions
east_team = json.load(open('static/Resources/east_teams.json'))
west_team = json.load(open('static/Resources/west_teams.json'))
midwest_team = json.load(open('static/Resources/midwest_teams.json'))
south_team = json.load(open('static/Resources/south_teams.json'))

######################
@app.route("/")
def home():

    return render_template("index.html")
#--------------------
@app.route("/east")
def east_region():
    
    return render_template("east.html",east_team=east_team)
#--------------------
@app.route("/west")
def west_region():
    
    return render_template("west.html",west_team=west_team)
#--------------------
@app.route("/south")
def south_region():
    
    return render_template("south.html",south_team=south_team)
#--------------------
@app.route("/midwest")
def midwest_region():
    
    return render_template("midwest.html",midwest_team=midwest_team)

######################

if __name__ == "__main__":
    app.run(debug=True)
