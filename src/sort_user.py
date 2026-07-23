import os
import json
from datetime import datetime
data="boston_users_database.json"
user_act ={}
users_id=[]
with open("bostonbombings_clean.json", "r", encoding="utf-8") as f:
    conversation_trees = json.load(f)
for thread, tweets in conversation_trees.items():
    for tweet in tweets:
        user = tweet.get("user_id")
        if user not in user_act:
            user_act[user]=[]
        activity = {
            "thread_id": thread,
            "tweet_id": tweet.get("tweet_id"),
            "type": tweet.get("type"),
            "created_at": tweet.get("created_at"),
            "seconds_since_t0": tweet.get("seconds_since_t0"),
            "text": tweet.get("text")
        }
        user_act[user].append(activity)
with open(data, "w", encoding="utf-8") as out:
    json.dump(user_act, out, indent=4)

print("done")
