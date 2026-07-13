import os

rumours_path = "data/aug-rnr-data_full/bostonbombings/rumours"

rumor_sizes = []

for rumor_id in os.listdir(rumours_path):
    rumor_path = os.path.join(rumours_path, rumor_id)

    if not os.path.isdir(rumor_path):
        continue

    reactions_path = os.path.join(rumor_path, "reactions")

    if os.path.exists(reactions_path):
        number_of_reactions = len(os.listdir(reactions_path))
    else:
        number_of_reactions = 0

    rumor_sizes.append((rumor_id, number_of_reactions))


rumor_sizes.sort(key=lambda x: x[1], reverse=True)

print("Top 20 largest rumor cascades:")
for rumor_id, size in rumor_sizes[:20]:
    print(rumor_id, size)
