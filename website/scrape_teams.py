import pymongo

# Setup connection to mongodb
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.team_mascot_db
collection = db.teams