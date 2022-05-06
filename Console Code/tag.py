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
    collection.find(query)
    print("Tag is deleted")
def writeTag(db,userId,movieId,tag,timestamp):
    collection = db.tags
    query = {"userId":userId,"movieId":movieId,"tag":tag}

    if collection.count_documents(query, limit = 1) != 0:
        newTag = {"$set": {"tag": tag, "timestamp": timestamp}}
        collection.update_one(query, newTag)

    else:
        collection.insert_one({"userId":userId,"movieId":movieId,"tag":tag,"timestamp":timestamp})
def updateTag(db,userId,movieId,tag):
    collection = db.tags
    query = {"userId":userId,"movieId":movieId}
    cursor = collection.update_one(query,{"$set":{"tag":tag}})
    return cursor

    
