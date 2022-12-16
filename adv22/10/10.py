# The CPU has a single register, X, which starts with the value 1.
# addx V takes 2 cycles and the X register is increased by the Value V V can be negative
# noop take 1 cycle no efect # wait


def cycling(cycle, x):
    if (cycle + 1) in [20, 60, 100, 140, 180, 220]:
        print(f'Cycle : {cycle + 1} singal : {(cycle + 1) * x} , {x}')
    return cycle + 1


def one(data):
    x = 1
    cycle = 1
    for d in data:
        d = d.split()
        if d[0] == 'noop':
            cycle = cycling(cycle, x)
        else:
            cycle = cycling(cycle, x)
            x += int(d[1])
            cycle = cycling(cycle, x)



def is_visable(cycle,sprite):
    if abs(sprite - cycle) <=1:
        return '#'
    else:
        return '.'


def two(data):
    sprite = 1
    cycle = 0
    image = []
    for d in data:
        d = d.split()
        if d[0] == 'noop':
            image.append(is_visable(cycle,sprite))
            if cycle + 1 >= 40:
                cycle = 0
            else:
                cycle += 1
        else:
            for i in range(2):
                image.append(is_visable(cycle,sprite))
                if cycle + 1 >= 40:
                    cycle = 0
                else:
                    cycle +=1

            sprite += int(d[1])
    return image


if __name__ == '__main__':
    with open('in.txt') as f:
        data = f.read().splitlines()
    #one(data)
    img = two(data)
    print(img[0:40])
    print(img[40:80])
    print(img[80:120])
    print(img[120:160])
    print(img[160:200])
    print(img[200:240])
