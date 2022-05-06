import menu
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

def main():
    try:
        conn = MongoClient(os.environ.get("MONGODB_URI"))
        print("Mongo db Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")
    
    db = conn.moviesDB
    menu.menu(db)

if __name__ == "__main__":
    main()
