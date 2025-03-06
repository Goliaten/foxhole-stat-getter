# type: ignore
import json
from pprint import pprint


def dict_to_list(dict):

    out = []
    for x in dict:
        dct = {"Name": x}
        dct |= dict[x]
        out.append(dct)

    return out


def get_top_data(stat_index, top_num):

    data.sort(key=search_key[stat_index], reverse=True)

    top = [
        {"Name": x["Name"], activity[stat_index]: x[activity[stat_index]]}
        for x in data[:top_num]
    ]

    out = f"{activity[stat_index]}"
    for x in range(top_num):
        out += f'\n{x+1}. {top[x]["Name"]} - {top[x][activity[stat_index]]}'

    return out
    # return [ {'Name': x['Name'], activity[stat_index]: x[activity[stat_index]]} for x in data[:top_num]]


file = "out.json"
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
search_key = [
    lambda inp: inp[activity[0]],
    lambda inp: inp[activity[1]],
    lambda inp: inp[activity[2]],
    lambda inp: inp[activity[3]],
    lambda inp: inp[activity[4]],
    lambda inp: inp[activity[5]],
    lambda inp: inp[activity[6]],
    lambda inp: inp[activity[7]],
    lambda inp: inp[activity[8]],
    lambda inp: inp[activity[9]],
    lambda inp: inp[activity[10]],
    lambda inp: inp[activity[11]],
    lambda inp: inp[activity[12]],
    lambda inp: inp[activity[13]],
    lambda inp: inp[activity[14]],
]


with open(file, "r") as file:

    data = file.read()

data = json.loads(data)
data = dict_to_list(data)

out = []

for x in range(len(activity)):
    out.append(get_top_data(x, 5))
pprint(out)
with open("top_stats.txt", "w") as file:
    file.write(json.dumps(out, indent=1))
