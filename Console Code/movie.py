from pymongo import MongoClient

def getMoviesbyID(db, value ):
    id="_id"
    collection = db.movies
    movieId="movieId"
    query= {movieId: value}
    projection={id:0}
    cursor = collection.find(query, projection)
    return cursor

def getMoviesbyTitle(db, value, limitValue ):
    collection = db.movies
    id="_id"
    title="title"
    regex = '$regex'
    query= {title: { regex: value}}
    projection={id:0}
    cursor = collection.find(query, projection).limit(limitValue)
    return cursor

def getMoviesbyGenre(db, value, limitValue ):
    collection = db.movies
    id="_id"
    genres="genres"
    query= {genres: value}
    projection={id:0}
    cursor = collection.find(query, projection).limit(limitValue)
    return cursor

def getMoviesbyYear(db, value, limitValue ):
    collection = db.movies
    id="_id"
    title="title"
    regex = '$regex'
    query= {title: { regex: value}}
    projection={id:0}
    cursor = collection.find(query, projection).limit(limitValue)
    return cursor

def addMovie(db, titleValue, genreValue ):
    collection = db.movies
    id="_id"
    title="title"
    movieId = "movieId"
    genres = 'genres'
    genreValue = genreValue.split(",")
    movieIdValue = 0
    
    cursor = collection.find(sort=[("movieId", pymongo.DESCENDING)]).limit(1)
    for record in cursor:
        movieIdValue = int(record["movieId"]) + 1
    
    insertValue ={
        movieId : movieIdValue,
        title : titleValue,
        genres : genreValue
    }
    insertRes = collection.insert_one(insertValue)
    print("Inserted this value", insertRes)
    query= {movieId: movieIdValue}
    projection={id:0}
    cursor = collection.find(query, projection)
    return cursor

def getMoviesbyUserId(db, value , limitValue):
    collection = db.tags
    id="_id"
    userid="userId"
    movieId='movieId'
    title="title"
    movieIdList = []
    query= {userid: value}
    projection={id:0, movieId :1}
    cursor = collection.find(query, projection).limit(limitValue)
    for record in cursor:
        movieIdList.append(record['movieId'])
    ink = '$in'
    query = {movieId: { ink: movieIdList}}
    projection={id:0, title: 1}
    collection = db.movies
    cursor = collection.find(query, projection).limit(5)
    return cursor

def getHighlyRatedMovies(db, limitValue ):
    collection = db.ratings
    rating='rating'
    gte='$gte'
    id="_id"
    movieId="movieId"
    title="title"
    movieIdList = []
    query= {rating:{gte:5}}
    projection={movieId:1,id:0}
    cursor = collection.find(query, projection).limit(limitValue)
    for record in cursor:
        movieIdList.append(record['movieId'])
    ink = '$in'
    query = {movieId: { ink: movieIdList}}
    projection={id:0, title: 1}
    collection = db.movies
    cursor = collection.find(query, projection)
    return cursor

def getLowlyRatedMovies(db, limitValue ):
    collection = db.ratings
    rating='rating'
    lte='$lte'
    id="_id"
    movieId="movieId"
    title="title"
    movieIdList = []
    query= {rating:{lte:0.5}}
    projection={movieId:1,id:0}
    cursor = collection.find(query, projection).limit(limitValue)
    for record in cursor:
        movieIdList.append(record['movieId'])
    ink = '$in'
    query = {movieId: { ink: movieIdList}}
    projection={id:0, title: 1}
    collection = db.movies
    cursor = collection.find(query, projection)
    return cursor

def getMoviesbyRating(db, value, limitValue ):
    collection = db.ratings
    rating='rating'
    id="_id"
    movieId="movieId"
    title="title"
    movieIdList = []
    query= {rating: value}
    projection={movieId:1,id:0}
    cursor = collection.find(query, projection).limit(limitValue)
    for record in cursor:
        movieIdList.append(record['movieId'])
    ink = '$in'
    query = {movieId: { ink: movieIdList}}
    projection={id:0, title: 1}
    collection = db.movies
    cursor = collection.find(query, projection)
    return cursor
