from flask import Flask, render_template, redirect, make_response,request, jsonify
import os
import json
from flask_pymongo import PyMongo
import scrape_four



# Create an instance of Flask
app = Flask(__name__, static_url_path='/static')


# Route to render index.html
@app.route("/")
def home():

   return render_template("index.html")
#--------------------
@app.route("/API")
def mainapi():
    """List all available api routes."""
    return render_template("api_home.html")

@app.route("/api/2017/team_names")
def teamname():
    teams = []
    print('start the api')
    with open('team-list-2017.json') as json_data:
        team_test = json.load(json_data)
        for team in team_test:
            teams.append(team['name'])
    print(team)
    return jsonify(teams)



#--------------------
#error handler
@app.errorhandler(404)
def not_found(error):
   return make_response(jsonify({'error': 'Not found'}), 404)
#--------------------


######################

if __name__ == "__main__":
    app.run(debug=True)
