class Head:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.path = [[self.x,self.y]]

    def updatePos(self,x=0,y=0):
        self.x += x
        self.y += y
        self.path.append([self.x,self.y])


class Tail:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tiles = [[self.x, self.y]]


    def updatePos(self,tile = [0,0]):
        self.x = tile[0]
        self.y = tile[1]
        if([self.x,self.y] not in self.tiles):
            self.tiles.append([self.x,self.y])

def touching(Tail,Head):
    if (abs(Tail.x - Head.x) == 1 or abs(Tail.x - Head.x) == 0)and (abs(Tail.y - Head.y) == 1 or abs(Tail.y - Head.y) == 0):
        return True
    else : return False

def move(way,obj):
    if way =='R':
        obj.updatePos(x=1)
    elif way =='L':
        obj.updatePos(x=-1)
    elif way=='U':
        obj.updatePos(y=1)
    elif way=='D':
        obj.updatePos(y=-1)
    return 0


def one(data):
    H = Head()
    T = Tail()
    for row in data:
        way = row[0]
        times = row[2:]
        for t in range(int(times)):
            move(way,H)
            if touching(T,H):pass
            else:
                T.updatePos(H.path[-2])
    return len(T.tiles)

if __name__ == '__main__':
    with open('in.txt') as f:
        data = f.read().splitlines()
    print(one(data))