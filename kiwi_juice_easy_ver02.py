capacities = [14, 35, 86, 58, 25, 62]
bottoles = [6, 34, 27, 38, 9, 60]
fromId = [1, 2, 4, 5, 3, 3, 1, 0]
toId = [0, 1, 2, 4, 2, 5, 3, 1]

for i in range(0, len(fromId)):
    total = bottoles[fromId[i]] + bottoles[toId[i]]
    bottoles[toId[i]] = min(capacities[toId[i]], total)
    bottoles[fromId[i]] = total - bottoles[toId[i]]

print(bottoles)
