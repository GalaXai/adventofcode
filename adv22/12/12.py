from collections import deque

grid = [list(x) for x in open('in.txt').read().strip().splitlines()]
if __name__ == '__main__':
    ays = []
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if item == 'S':
                sy = y
                sx = x
                grid[y][x] = "a"
            if item == 'E':
                ey = y
                ex = x
                grid[y][x] = "z"
            if item == "a":
                ays.append([y, x])
    print(sy, sx, ey, ex)  # prints the cords of S and E

    # pop left , append left
    # pop append | on the right
    outputs = []
    for sy, sx in ays:

        q = deque()

        q.append((0, sy, sx))

        visited = {(sy, sx)}

        while q:  # is not empty
            d, y, x = q.popleft()
            #            | up      down     right   left  |
            for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if ny < 0 or nx < 0 or ny >= len(grid) or nx >= len(grid[0]):
                    continue
                if (ny, nx) in visited:
                    continue
                if ord(grid[ny][nx]) - ord(
                        grid[y][x]) > 1:  # ord() Return the Unicode code point for a one-character string
                    continue
                if ny == ey and nx == ex:
                    print(d + 1)
                    outputs.append(d + 1)
                    exit()
                visited.add((ny, nx))
                q.append((d + 1, ny, nx))
        print("Min : ", min(outputs))