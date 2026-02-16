weights = [4, 18, 70, -2, 30, 55, 0]

name = input("Enter your full name: ")

L = 0
for i in name:
    if i != " ":
        L = L + 1

PLI = L % 3

very_light = []
normal_load = []
heavy_load = []
overload = []
invalid_entries = []

for w in weights:
    if w < 0:
        invalid_entries.append(w)
    elif w <= 5:
        very_light.append(w)
    elif w <= 25:
        normal_load.append(w)
    elif w <= 60:
        heavy_load.append(w)
    else:
        overload.append(w)

valid_count = 0
for w in weights:
    if w >= 0:
        valid_count = valid_count + 1

affected = 0

if PLI == 0:
    for x in overload:
        invalid_entries.append(x)
        affected = affected + 1
    overload = []

elif PLI == 1:
    for x in very_light:
        affected = affected + 1
    very_light = []

else:
    for x in very_light:
        affected = affected + 1
    for x in overload:
        affected = affected + 1
    for x in invalid_entries:
        affected = affected + 1
    very_light = []
    overload = []
    invalid_entries = []

print("L value:", L)
print("PLI value:", PLI)
print("Total valid weights:", valid_count)
print("Affected items:", affected)

print("Very Light:", very_light)
print("Normal Load:", normal_load)
print("Heavy Load:", heavy_load)
print("Overload:", overload)
print("Invalid Entries:", invalid_entries)
