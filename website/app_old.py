from flask import Flask, render_template, redirect, request, url_for
import os
from flask_pymongo import PyMongo
#import scrape_costa

# Create an instance of Flask
app = Flask(__name__, static_url_path='/static')
resource_folder = os.path.join('static', 'Images')
app.config['resource'] = resource_folder
# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/ETL_NCAA_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    image_path = os.path.join(app.config['resource'],'ncaa_hlogo.png')
    # Return template and data
    return render_template("index.html",Resources = image_path)


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
