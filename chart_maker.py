import matplotlib.pyplot as plt
import json

filename = 'out.json'
graph_title = 'WC112 - 5th'

plt.rcParams['font.size'] = 7
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
activity_label = [
    "Enemy Player Damage",
    "Friendly Player Damage",
    "Enemy Structure,Vehicle Damage",
    "Friendly Structure,Vehicle Damage",
    "Friendly Construction",
    "Friendly Repairing",
    "Friendly Healing",
    "Friendly Revivals",
    "Vehicles Captured By Enemy",
    "Vehicle Self Damage(Neutral)",
    "Vehicle Self Damage(Colonial)",
    "Vehicle Self Damage(Warden)",
    "Materials Submitted",
    "Materials Gathered",
    "Supply Value Delivered",
]
data_cutoff = 0.01

def get_data():
    with open(filename, 'r') as file:
        return json.loads(file.read())
        
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_autopct
    
# receives data, that should be shown on graph, and makes that graph
def make_chart(id, title, labels, data):
    fig, ax = plt.subplots(figsize=(6.2, 6.2), dpi = 200)
    plt.text(-0.15, 1.1, title, ha='left', va='top', transform=ax.transAxes)
    plt.text(-0.15, -0.07, f'Total: {sum(data)}', ha='left', va='top', transform=ax.transAxes)
    patches, labels, pct_texts = ax.pie(data, labels=labels, autopct=make_autopct(data), rotatelabels=True, pctdistance=0.7)
    
    # rotating autopct https://stackoverflow.com/questions/64411633/how-to-rotate-the-percentage-label-in-a-pie-chart-to-match-the-category-label-ro
    for label, pct_text in zip(labels, pct_texts):
        pct_text.set_rotation(label.get_rotation())
    
    # autopct https://stackoverflow.com/questions/6170246/how-do-i-use-matplotlib-autopct
    # try out annotations https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html
    plt.savefig(f'{title}.png')
    #plt.show()

#receives labels, and raw data for a statistic
def chart_handle(id, title, labels, data):
    labels, data = clean_data(labels, data)
    make_chart(id, title, labels, data)

def clean_data(labels, data):
    # sorts labels and data
    labels = [l for _,l in sorted(zip(data, labels))]
    data.sort()
    
    # removes people with 0 of a stat
    ind_remove = []
    for ind, score in enumerate(data):
        if score == 0:
            ind_remove.append(ind)
    for x in ind_remove[::-1]:
        del labels[x]
        del data[x]
        
    # replaces people with X% or less of total sum of all stats with 'other' label
    cutoff = sum(data) * data_cutoff
    ind_remove = []
    other = 0
    for ind, score in enumerate(data):
        if score <= cutoff:
            ind_remove.append(ind)
            other += score
    
    for x in ind_remove[::-1]:
        del labels[x]
        del data[x]
    
    if other >= 1:
        labels.append('Other')
        data.append(other)
    #print(labels, data)
    #print(labels)
    return labels, data

def main():
    
    graph_title = input("Write the file name for the graphs: ")
    
    data = get_data()
    names = [x for x in data.keys()]
    for y in range(len(activity)):
        print(y)
        values = [x[activity[y]] for x in data.values()] #for now, values of enemyplayerdamage
        title = f'{graph_title} - {y} {activity_label[y]}'
        chart_handle(y, title, names, values)

if __name__ == '__main__':
    main()
    exit()


data = get_data()
names = [x for x in data.keys()]
values = [x[activity[12]] for x in data.values()] #for now, values of enemyplayerdamage
title = activity_label[12]
chart_handle(title, names, values)


