import re


def dfs(bp, maxspend, cache, time, bots, mats):
    if time == 0:
        return mats[3]
    k = tuple([time, *bots, *mats])
    if k in cache:
        return cache[k]

    maxval = mats[3] + bots[3] * time

    for bot_type, recipe in enumerate(bp):

        if bot_type != 3 and bots[bot_type] >= maxspend[bot_type]:
            continue

        wait = 0
        for mats_amount, mats_type in recipe:
            if bots[mats_type] == 0:
                break
            wait = max(wait, -(-(mats_amount - mats[mats_type]) // bots[mats_type]))
        else:
            rem_time = time - wait - 1
            if rem_time <= 0:
                continue
            bots_ = bots[:]
            mats_ = [x + y * (wait + 1) for x, y in zip(mats, bots)]
            for mats_amount, mats_type in recipe:
                mats_[mats_type] -= mats_amount
            bots_[bot_type] += 1
            for i in range(3):
                mats_[i] = min(mats_[i], maxspend[i] * rem_time)
            maxval = max(maxval, dfs(bp, maxspend, cache, rem_time, bots_, mats_))

    cache[k] = maxval
    return maxval


total = 0

#Part 1
for i, line in enumerate(open('in.txt').readlines()):
    bp = []
    maxspend = [0, 0, 0]
    for section in line.split(": ")[1].split(". "):
        recipe = []
        for x, y in re.findall(r"(\d+) (\w+)", section):
            x = int(x)
            y = ["ore", "clay", "obsidian"].index(y)
            recipe.append((x, y))
            maxspend[y] = max(maxspend[y], x)
        bp.append(recipe)
    v = dfs(bp, maxspend, {}, 24, [1, 0, 0, 0], [0, 0, 0, 0])
    total += (i + 1) * v

print(total)

#Part 2
total_p2 = 1
for line in open('in2.txt').readlines():
    bp = []
    maxspend = [0, 0, 0]
    for section in line.split(": ")[1].split(". "):
        recipe = []
        for x, y in re.findall(r"(\d+) (\w+)", section):
            x = int(x)
            y = ["ore", "clay", "obsidian"].index(y)
            recipe.append((x, y))
            maxspend[y] = max(maxspend[y], x)
        bp.append(recipe)
    v = dfs(bp, maxspend, {}, 32, [1, 0, 0, 0], [0, 0, 0, 0])
    total_p2 *= v

print(total_p2)