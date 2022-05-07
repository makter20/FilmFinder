from pymongo import MongoClient

def getMoviesbyTag(db, value,limit ):
    id="_id"
    collection = db.tags
    tag="tag"
    query= {tag: value}
    projection={id:0}
    cursor = collection.find(query, projection).limit(limit)
    return cursor

def getTagsbyMovie(db, value,limit ):
    id="_id"
    collection = db.tags
    movieId="movieId"
    query= {movieId: value}
    projection={id:0}
    cursor = collection.find(query, projection).limit(limit)
    return cursor

def getTagsbyUserId(db, value,limit ):
    id="_id"
    collection = db.tags
    userId="userId"
    query= {userId: value}
    projection={id:0}
    cursor = collection.find(query, projection).limit(limit)
    return cursor


def deleteOneTag(db,userId,movieId,tag):
    collection = db.tags
    query = {"userId":userId,"movieId":movieId,"tag":tag}
    delRes= collection.delete_one(query)
    print("Deleted this value", delRes)
    projection = {"_id": 0}
    cursor = collection.find(query, projection)
    return cursor


def writeTag(db,userId,movieId,tag,timestamp):
    collection = db.tags
    query = {"userId":userId,"movieId":movieId,"tag":tag}

    if collection.count_documents(query, limit = 1) != 0:
        newTag = {"$set": {"tag": tag, "timestamp": timestamp}}
        insRes = collection.update_one(query, newTag)
        print("Updated this value", insRes)
    else:
        insRes = collection.insert_one({"userId":userId,"movieId":movieId,"tag":tag,"timestamp":timestamp})
        print("Inserted this value", insRes)
    projection = {"_id": 0}
    cursor = collection.find(query, projection)
    return cursor

def updateTag(db,userId,movieId,tag):
    collection = db.tags
    query = {"userId":userId,"movieId":movieId}
    insRes = collection.update_one(query,{"$set":{"tag":tag}})
    print("Updated this value", insRes)
    query = {"userId":userId,"movieId":movieId,"tag":tag}
    projection = {"_id": 0}
    cursor = collection.find(query, projection)
    return cursor

