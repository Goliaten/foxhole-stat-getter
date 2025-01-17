import json
from pprint import pprint

file = 'out.json'
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
    lambda inp : inp[activity[0]],
    lambda inp : inp[activity[1]],
    lambda inp : inp[activity[2]],
    lambda inp : inp[activity[3]],
    lambda inp : inp[activity[4]],
    lambda inp : inp[activity[5]],
    lambda inp : inp[activity[6]],
    lambda inp : inp[activity[7]],
    lambda inp : inp[activity[8]],
    lambda inp : inp[activity[9]],
    lambda inp : inp[activity[10]],
    lambda inp : inp[activity[11]],
    lambda inp : inp[activity[12]],
    lambda inp : inp[activity[13]],
    lambda inp : inp[activity[14]],
]


with open(file, 'r') as file:
    
    data = file.read()

data = json.loads(data)

out = {}

for key, item in data.items():
    
    stat_sum = sum(item.values())
    if stat_sum == 0:
        out[key] = stat_sum
    
pprint(out)
with open('no_stats.txt', 'w') as file:
    file.write(json.dumps(out, indent=1))


