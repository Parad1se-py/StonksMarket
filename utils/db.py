import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

cluster = MongoClient(os.getenv('MONGO_CLUSTER'))
db = cluster['stonks']
collection = db['users']


def register(email, password, username) -> list:
    """Registers a user into the StonkMarket game."""
    post = {
        "email": email,
        "password": password,
        "username": username,
        "joined_at": datetime.datetime.now(),
        "money": 500,
        "stocks": {},
        "lootboxes": {}
    }
    collection.insert_one(post)
    return [True, collection.find_one({"email": email})]

def check_for_account(*args) -> bool:
    """Checks if an account is already registered in the StonkMarket game."""
    if bool(collection.find_one({"email": args[0]})):
        return True
    elif bool(collection.find_one({"username": args[0]})):
        return True
    return False

def update_cash(_id, mode, amount) -> bool:
    collection.update_one({"_id": _id}, {"$inc": {mode: amount}})
    return True

def update_stocks(_id, share, amount) -> bool:
    collection.update_one({"_id": _id}, {"$inc": {f"stocks.{share}": amount}})
    return True
