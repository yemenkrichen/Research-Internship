import json

with open("boston_user_transitions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for user, activities in data.items():
    for act in activities:
        tweet_text = act.get("text")
        print(tweet_text)
