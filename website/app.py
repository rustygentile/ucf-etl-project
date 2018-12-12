from flask import Flask, render_template, redirect  
import os
import pymongo
import json
from flask_pymongo import PyMongo
#import scrape_costa

# Create an instance of Flask
app = Flask(__name__, static_url_path='/static')


east_team = json.load(open('east_team_logos.json'))
# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.team_mascot_db
collection_south = db.teams_south
collection_east = db.teams_east
collection_west = db.teams_west
collection_midwest = db.teams_midwest

#east_team= list(db.teams_east.find())


# Route to render index.html template using data from Mongo
@app.route("/")

def home():
    
    # Return template and data
    return render_template("index.html")

@app.route("/east")
def region():
    
    return render_template("east.html",east_team=east_team)
# Route that will trigger the scrape function
#@app.route("/scrape")
#def scrape():

    # Run the scrape function
    #ncaa_data = scrape_ncaa.scrape_info()

    # Update the Mongo database using update and upsert=True
   # mongo.db.collection.update({}, ncaa_data, upsert=True)

    # Redirect back to home page
   # return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
