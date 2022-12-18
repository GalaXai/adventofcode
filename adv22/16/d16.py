import re
from collections import deque

data = open('in.txt').read().splitlines()
data = [re.findall("[A-Z]{2}|\d+", row) for row in data]

valves = {}
tunnels = {}
for line in data:
    valve = line[0]
    flow_rate = int(line[1])
    targets = line[2:]
    valves[valve] = flow_rate
    tunnels[valve] = targets

# print(valves)
# print(tunnels)

dists = {}
nonempty = []
for valve in valves:
    if valve != "AA" and not valves[valve]:
        continue
    if valve != "AA":
        nonempty.append(valve)
    dists[valve] = {valve: 0, "AA": 0}
    visited = {valve}

    queue = deque([(0, valve)])

    while queue:
        distance, position = queue.popleft()
        for neighbor in tunnels[position]:
            if neighbor in visited:
                continue
            visited.add(neighbor)

            if valves[neighbor]:
                dists[valve][neighbor] = distance + 1
            queue.append((distance + 1, neighbor))

    del dists[valve][valve]
    if valve != "AA":
        del dists[valve]["AA"]

print(dists)

indices = {}

for index, element in enumerate(nonempty):
    indices[element] = index

cache = {}


def dfs(time, valve, bitmask):
    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]
    maxval = 0

    for neighbor in dists[valve]:
        bit = 1 << indices[neighbor]
        if bitmask & bit:
            continue
        remtime = time - dists[valve][neighbor] - 1
        if remtime <= 0:
            continue

        maxval = max(maxval, dfs(remtime, neighbor, bitmask | bit) + remtime * valves[neighbor])

    cache[(time, valve, bitmask)] = maxval
    return maxval


print(dfs(30, "AA", 0))  # Part 1

# Whole part 2
b = (1 << len(nonempty)) - 1
# n 1111111111

m = 0

for i in range((b + 1) // 2):
    m = max(m, dfs(26, "AA", i) + dfs(26, "AA", b - i))

print(m)
