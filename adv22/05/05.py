import re
def one(data):
    num = re.findall('\d+',data)
    num = [int(x) for x in num]
    for _ in range(num[0]):
        d[num[2]].append(d[num[1]].pop())

#TODO missing part 2
#Did part2 away from home
if __name__ == '__main__':
    with open('in.txt') as f:
        d = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
        for _ in range(8):
            value = f.readline()
            value = [value[i + 1] for i in range(0, len(value), 4)]
            for i in range(1, 10):
                try:
                    if value[i - 1] != " ":
                        d[i].insert(0, value[i - 1])
                except: pass
        f.readline()
        f.readline()
        data = f.read().splitlines()
    score= 0
    for rear in data:
        one(rear)
    for i in range(1,10):
        print(d[i])