from pymongo import MongoClient

def getMoviesbyTag(db, value ):
    id="_id"
    collection = db.tags
    tag="tag"
    query= {tag: value}
    projection={id:0}
    cursor = collection.find(query, projection)
    return cursor

def getTagsbyMovie(db, value ):
    id="_id"
    collection = db.tags
    movieId="movieId"
    query= {movieId: value}
    projection={id:0}
    cursor = collection.find(query, projection)
    return cursor

def getTagsbyUserId(db, value ):
    id="_id"
    collection = db.tags
    userId="userId"
    query= {userId: value}
    projection={id:0}
    cursor = collection.find(query, projection)
    return cursor

