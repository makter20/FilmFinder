import pymongo
from pymongo import MongoClient

#userId,movieId,rating,timestamp
#1,307,3.5,1256677221

def getRating(db, movieId, startTime, endTime):
    collection = db.ratings
    query = {"movieId": movieId, "timestamp": {"$gte": startTime, "$lte": endTime}}
    projection = {"_id": 0}
    cursor = collection.find(query, projection)
    for record in cursor:
        print(record)

def delRating(db, userId, movieId):
    collection = db.ratings
    query = {"userId": userId, "movieId": movieId}
    collection.delete_one(query)

#this combines add and update
def putRating(db, userId, movieId, rating, timestamp):
    collection = db.ratings
    query = {"userId": userId, "movieId": movieId}

    #if userId,movieId already exists, update
    if collection.count_documents(query, limit = 1) != 0:
        newValues = {"$set": {"rating": rating, "timestamp": timestamp}}
        collection.update_one(query, newValues)

    else: #insert
        newValues = {
            "userId": userId, 
            "movieId": movieId, 
            "rating": rating, 
            "timestamp": timestamp}
        collection.insert_one(newValues)
    
def main():
    try:
        conn = MongoClient("mongodb+srv://admin:rootpassword@cluster0.xl0um.mongodb.net/moviesDB?retryWrites=true&w=majority")
        print("Mongo db Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")
    
    db = conn.moviesDB
    putRating(db, 1, 2, "good", 18932)
    putRating(db, 1, 2, "good enough", 18932)
    putRating(db, 2, 2, "fantastic", 18932)
    putRating(db, 1, 3, "great", 18934)
    getRating(db, 2, 18930, 18934)
    # delRating(db, 1, 2)

if __name__ == "__main__":
    main()