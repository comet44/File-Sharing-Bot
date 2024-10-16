#(©)CodeXBotz




import pymongo, os
from config import DB_URI, DB_NAME
import time

dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]


user_data = database['users']



async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    if found:
        return True
    else:
        return False

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return

async def update_cooldown(user_id: int):
    cooldown_time = time.time()  # Set the current timestamp
    user_data.update_one(
        {'_id': user_id},
        {'$set': {'cooldown': cooldown_time}}  # Store the timestamp for the cooldown
    )
    return

# Retrieve the current cooldown timestamp for the user
async def get_cooldown(user_id: int):
    user = user_data.find_one({'_id': user_id})
    if user and 'cooldown' in user:
        return user['cooldown']
    return 0  # If no cooldown is found, return 0 (no cooldown active)

# Function to check if the user is within the cooldown period
async def is_user_on_cooldown(user_id: int):
    cooldown_time = await get_cooldown(user_id)
    current_time = time.time()

    if current_time - cooldown_time < 60:  # Check if less than 60 seconds have passed
        remaining_time = 60 - (current_time - cooldown_time)
        return True, remaining_time
    else:
        return False, 0
