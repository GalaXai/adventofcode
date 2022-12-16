class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.path = [[self.x, self.y]]
        self.tiles = [[self.x, self.y]]

    def update_pos(self, x=0, y=0):
        self.x += x
        self.y += y
        self.path.append([self.x, self.y])
        if ([self.x, self.y] not in self.tiles):
            self.tiles.append([self.x, self.y])

def touching(tail, head):
    if (abs(tail.x - head.x) == 1 or abs(tail.x - head.x) == 0) and (
            abs(tail.y - head.y) == 1 or abs(tail.y - head.y) == 0):
        return True
    else:
        return False

def move(way, obj):
    if way == 'R':
        obj.update_pos(x=1)
    elif way == 'L':
        obj.update_pos(x=-1)
    elif way == 'U':
        obj.update_pos(y=1)
    elif way == 'D':
        obj.update_pos(y=-1)
    return 0

def one(data):
    knots = [Knot() for _ in range(10)]
    for row in data:
        way = row[0]
        times = row[2:]
        for t in range(int(times)):
            move(way, knots[0])
            for i in range(1, 10):
                if touching(knots[i], knots[i - 1]):
                    pass
                else:
                    x, y = 0, 0
                    if abs(knots[i].x - knots[i - 1].x) >= 1:
                        if (knots[i - 1].x - knots[i].x) < 0:
                            x = -1
                        else:
                            x = 1
                    if abs(knots[i].y - knots[i - 1].y) >= 1:
                        if (knots[i - 1].y - knots[i].y) < 0:
                            y = -1
                        else:
                            y = 1
                    knots[i].update_pos(x, y)
    return knots[9].tiles

if __name__ == '__main__':
    with open('in.txt') as f:
        data = f.read().splitlines()

    x = (one(data))
    print(len(x))
    print(x)