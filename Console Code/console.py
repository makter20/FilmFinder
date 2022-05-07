import menu
from pymongo import MongoClient

def main():
    try:
        conn = MongoClient("mongodb://172.31.3.57:27021")
        print("Mongo db Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")
    
    db = conn.moviesDB
    menu.menu(db)

if __name__ == "__main__":
    main()
