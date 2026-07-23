import json

with open("boston_user_transitions.json", "r", encoding="utf-8") as f:
    transitions = json.load(f)

with open("boston_users_database.json", "r", encoding="utf-8") as f:
    users_db = json.load(f)

for user, activities in transitions.items():
    if len(activities) == 0:
        for element,act in users_db.items():
            if user  == element:
                for el in act:
                    if el['type']!= "source":
                        for e,a in users_db.items():
                            for b in a:
                                if b['type']== 'source' and b['thread_id']==el['thread_id']:
                                    print(user, b['text'], " : ", el["text"])









