import json
with open("boston_users_database.json", "r", encoding="utf-8") as f:
    users = json.load(f)
count = 0
for user in users.items():
    count +=1
print(count)
