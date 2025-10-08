import json
import os.path
from pprint import pprint

# FIXME: names may not always match due to how OCR performs

activity = [
    "EnemyPlayerDamage",
    "FriendlyPlayerDamage",
    "EnemyStructure/VehicleDamage",
    "FriendlyStructure/VehicleDamage",
    "FriendlyConstruction",
    "FriendlyRepairing",
    "FriendlyHealing",
    "FriendlyRevivals",
    "VehiclesCapturedByEnemy",
    "VehicleSelfDamage(Neutral",
    "VehicleSelfDamage(Colonial",
    "VehicleSelfDamage(Warden",
    "MaterialsSubmitted",
    "MaterialsGathered",
    "SupplyValueDelivered",
]


def get_data(filename):
    with open(filename, "r") as file:
        return json.loads(file.read())


def previous_war_stats(data, backup):
    if backup == None:
        return data
    if len(data.keys()) == 0:
        return data

    backup = {key.lower(): value for key, value in backup.items()}
    backup_keys = backup.keys()
    stat_len = len(activity)
    out = {}

    for key in data.keys():
        key_t = key.lower()
        if key_t in backup_keys:
            counter = 0
            for ind in range(stat_len):
                if data[key][activity[ind]] == backup[key_t][activity[ind]]:
                    counter += 1

            # print(counter)
            if counter == stat_len:
                out[key] = -1

            if counter == 15 and False:
                print(key)
                print(data[key])
                input("a")
    return out


def main():
    global total_data_length

    graph_title = input("Write the file name of the source file: ")

    if not os.path.isfile(graph_title):
        print("File not found")
        return

    backup_json = input(
        "Write filename of a last war json(used to eliminate last war stats)(optional): "
    )

    data = get_data(graph_title)

    if not os.path.isfile(backup_json):
        print("Couldn't load secondary json")
        backup_data = None
        exit()
    else:
        print("Found secondary json, cleaning data.")
        backup_data = get_data(backup_json)
        out = previous_war_stats(data, backup_data)
        pprint(out)
        print(f"Number of those with stats copied from past war: {len(out)}")

    with open("no_stats_prev_war.txt", "w") as file:
        file.write(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
    exit()
