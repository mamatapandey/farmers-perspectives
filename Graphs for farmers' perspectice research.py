import matplotlib.pyplot as plt
import numpy as np

# Ocupational categories pie chart
# Importing data for making a pie-chart
labels = ['Full-time farming', 'Part-time farming', 'Full-time farming and ranching', 'Part-time farming and ranching']
sizes = [20.8, 8.3, 58.3, 12.5]
colors = ['#4C88C7', '#E87E38', '#A0A0A0', '#F1C40F']
explode = (0, 0, 0, 0)

# Creating figure
fig, ax = plt.subplots(figsize=(6, 4), dpi=300)  # More compact figure
wedges, texts, autotexts = ax.pie(
    sizes, labels=None, autopct='%1.0f%%', colors=colors, explode=explode,
    startangle=140, wedgeprops={'edgecolor': 'white'}
)
ax.legend(labels, loc="center left", bbox_to_anchor=(1, 0.5))
plt.savefig("occupational_categories_pie_chart.png", bbox_inches='tight', dpi=300)
plt.show()

# Major crop prodcution
# Data
crops = ['Cotton', 'Wheat', 'Grain Sorghum', 'Alfalfa', 'Peanut', 'Others']
participants = [19, 19, 4, 3, 2, 3]

# Creating figure
fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
bars = ax.barh(crops, participants, color='#4C88C7', height=0.5)  # Blue color

ax.set_xlabel("Number of Participants", fontsize=12)
ax.set_ylabel("Major Crop Production", fontsize=12)
ax.invert_yaxis() 
ax.set_xticks(np.arange(0, max(participants) + 5, 4))
plt.savefig("major_crop_prodcution.png", bbox_inches='tight', dpi=300)
plt.show()

# Irrigation types
# Data
irrigation_types = ['Center Pivot', 'Drip','Flood', 'Others']
participants = [12, 11,9, 2]

# Creating figure
fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
bars = ax.bar(irrigation_types, participants, color='#4C88C7', width=0.5)
ax.set_xlabel("Irrigation System", fontsize=12)
ax.set_ylabel("Number of Participants", fontsize=12)
plt.savefig("irrigation_types.png", bbox_inches='tight', dpi=300)
plt.show()

# Technology adoption
# Data
categories = ['Visual Observation', 'Soil Moisture Sensors', 'Smartphone Application', 'Consulting company']
willing = [5, 6, 2, 4]
reluctant = [2, 0, 0, 0]  # Only Visual Observation has reluctant participants

# Matching pie chart colors
colors = {
    'Visual Observation': '#a5a5a5',
    'Soil Moisture Sensors': '#4f81bd',
    'Smartphone Application': '#f1c232',
    'Consulting company': '#e69138'
}

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 4))
bar_width = 0.5
left = 0
for cat, val in zip(categories, willing):
    ax.barh('Willing', val, left=left, height=bar_width, color=colors[cat], label=cat)
    ax.text(left + val / 2, -0.1, str(val), va='center', ha='center', color='black', fontsize=10)
    left += val
if reluctant[0] > 0:
    bar = ax.barh('Reluctant', reluctant[0], height=bar_width, color=colors['Visual Observation'])
    ax.text(reluctant[0] / 2, 1, str(reluctant[0]), va='center', ha='center', color='black', fontsize=10)
    
ax.set_xlim(0, 20)
ax.set_xticks(range(0, 21, 4))  # Interval of 4
ax.set_xlabel("Number of Participants")
ax.set_ylabel("Participant's Perspective")
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.savefig("Technology adoption.png", bbox_inches='tight', dpi=300)
plt.show()

# Water use by farming type 
# Data
categories = ['Irrigation', 'Dryland']
values = {
    'Surface Only': [2, 0],
    'Groundwater Only': [8, 0],
    'Both Sources': [6, 0],
    'Rainfed (Dryland)': [0, 8]
}
colors = {
    'Surface Only': '#1f77b4',
    'Groundwater Only': '#ff7f0e',
    'Both Sources': '#2ca02c',
    'Rainfed (Dryland)': '#d3d3d3'
}

fig, ax = plt.subplots(figsize=(10, 4))
y_pos = range(len(categories))
bar_width = 0.5
left = [0, 0] 

# Plotting each water source
for label in ['Surface Only', 'Groundwater Only', 'Both Sources', 'Rainfed (Dryland)']:
    ax.barh(y_pos, values[label], left=left, color=colors[label], height=bar_width, label=label)
    for i in range(len(categories)):
        if values[label][i] > 0:
            ax.text(left[i] + values[label][i]/2, i, str(values[label][i]),
                    va='center', ha='center', color='black')
    left = [left[i] + values[label][i] for i in range(len(categories))]

ax.set_yticks(y_pos)
ax.set_yticklabels(categories)
ax.set_xlabel('Number of Participants')
ax.set_ylabel('Farming Type')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.savefig("water_use_by_farming_type_final.png", bbox_inches='tight', dpi=300)
plt.show()