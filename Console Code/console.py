import menu
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://admin:rootpassword@cluster0.xl0um.mongodb.net/moviesDB?retryWrites=true&w=majority"

def main():
    try:
        conn = MongoClient(MONGO_URI)
        print("Mongo db Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")
    
    db = conn.moviesDB
    menu.menu(db)

if __name__ == "__main__":
    main()
