from flask import Flask, render_template, redirect, make_response,request, jsonify
import os
import json
from flask_pymongo import PyMongo
import scrape_four



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
    final_four_data = mongo.db.collection.find_one()

    return render_template("final_four.html",final_four_data=final_four_data)
#--------------------
# Route to render final.html template using csv data
@app.route("/finals")
def finals():

    return render_template("finals.html")
#--------------------
# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    four_data = scrape_four.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, four_data, upsert=True)

    # Redirect back to home page
    return redirect("/final_four")

#--------------------
#error handler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
######################

if __name__ == "__main__":
    app.run(debug=True)