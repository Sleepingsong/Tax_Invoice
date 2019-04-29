from pymongo import MongoClient



client = MongoClient("mongodb+srv://AtAdmin:admin@seniorproject-yv211.gcp.mongodb.net/test?retryWrites=true")

db = client['MyDatabase']
mycol = db['Customer']

mydoc = mycol.find_one()
print(mydoc)
