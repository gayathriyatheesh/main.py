readings = [160, 170, 180, 190, 50, 40]

data = {
    "efficient": [],
    "moderate": [],
    "high": [],
    "invalid": []
}

for e in readings:
    if e < 0:
        data["invalid"].append(e)
    elif e <= 50:
        data["efficient"].append(e)
    elif e <= 150:
        data["moderate"].append(e)
    else:
        data["high"].append(e)

total = sum([x for x in readings if x > 0])
count = len(readings)

summary = (total, count)

high_count = len(data["high"])
eff_count = len(data["efficient"])
mod_count = len(data["moderate"])

if high_count > 3:
    result = "Overconsumption"
elif abs(eff_count - mod_count) <= 1:
    result = "Balanced Usage"
elif total > 600:
    result = "Energy Waste Detected"
else:
    result = "Moderate Usage"

print("Categorized Data:", data)
print("Total Consumption:", summary[0])
print("Number of Buildings:", summary[1])
print("Result:", result)