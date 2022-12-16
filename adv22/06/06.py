def two(string):
    i = 0
    while True:
        t = i
        key = string[i:i + 14]
        for n in key:
            if key.count(n) != 1:
                t += 1
        if t == i:
            return i + 14
        else:
            i += 1

def one(string):
    i = 0
    while True:
        t= i
        key = string[i:i+4]
        for n in key:
            if key.count(n) != 1:
                t+=1
        if t == i:
            return i+4
        else: i+=1



if __name__ == '__main__':
    with open('in.txt') as f:
        data = f.read().splitlines()
    #print (one(data[0]))
    print(two(data[0])) # 1848
    print(data[0][2308-14:2308])