def top(x, y):
    global np_data
    if x == 0 or y == 0:
        return 1
    elif data[x][y] > np_data.T[y][0:x].max():
        return 1
    return 0


def bot(x, y):
    global np_data
    if x == 0 or y == 0:
        return 1
    elif data[x][y] > np_data.T[y][x + 1:].max():
        return 1
    return 0


def left(x, y):
    global np_data
    if x == 0 or y == 0:
        return 1
    elif data[x][y] > np_data[x][0:y].max():
        return 1
    return 0


def right(x, y):
    global np_data
    if x == 0 or y == 0:
        return 1
    elif data[x][y] > np_data[x][y + 1:].max():
        return 1
    return 0


def one(array):
    count = 0
    for i in range(len(array)):  # range 0 - 99
        for j in range(len(array)):
            # print(data[j][i - len(data)])
            value = data[i][j]
            flag = False
            if j == len(data) - 1 or i == len(data) - 1:
                count += 1  # top and bot
            elif top(i, j) == 1:
                count += 1
            elif bot(i, j) == 1:
                count += 1
            elif left(i, j) == 1:
                count += 1
            elif right(i, j) == 1:
                count += 1

    return count


def two(array):
    count = 0

    for i in range(len(array)):  # range 0 - 99
        for j in range(len(array)):
            value = data[i][j]
            tmp = up(i, j) * down(i, j) * lef(i, j) * rig(i, j)
            if tmp > count:
                count = tmp
                tmp = 0
    return count


def up(i, j):
    global np_data
    if j == 0:
        return 0
    else:
        count = 0
        for num in np_data.T[j][0:i][::-1]:
            if num < data[i][j]:
                count += 1
            else:
                count += 1
                break
        return count


def down(i, j):
    global np_data
    if j == len(np_data):
        return 0
    else:
        count = 0
        for num in np_data.T[j][i + 1:]:
            if num < data[i][j]:
                count += 1
            else:
                count += 1
                break
        return count


def lef(i, j):
    global np_data
    if i == 0:
        return 0
    else:
        count = 0
        for num in np_data[i][0:j][::-1]:
            if num < data[i][j]:
                count += 1
            else:
                count += 1
                break
        return count


def rig(i, j):
    global np_data
    if i == len(np_data):
        return 0
    else:
        count = 0
        for num in np_data[i][j + 1:]:
            if num < data[i][j]:
                count += 1
            else:
                count += 1
                break
        return count


if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt

    data = []
    with open('in.txt') as f:
        for line in f:
            data.append([int(x) for x in list(line.strip())])
    np_data = np.array(data)
    print(np_data.shape)
    # print(one(np_data))
    # print(two(np_data))
    plt.scatter(np.arange(0, 99), np_data)
    plt.show()
