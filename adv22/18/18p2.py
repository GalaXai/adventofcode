from collections import deque

cubes = [eval(x) for x in open('in.txt').read().splitlines()]

# cord are cubes in 3 plane

# given cube_1 (,1,1)
# offset cube_1 (1.5,1,1)
# given cube_2 (2,1,1)
# offset cube_2 (1.5,1,1)
#               ------- we see they have common face
offsets = [(0.5, 0, 0), (0, 0.5, 0), (0, 0, 0.5), (-0.5, 0, 0), (0, -0.5, 0), (0, 0, -0.5)]

faces = {}

min_x = float("inf")
min_y = float("inf")
min_z = float("inf")

max_x = -float("inf")
max_y = -float("inf")
max_z = -float("inf")

droplet = set()
for x_side, y_side, z_side in cubes:
    cube = (x_side, y_side, z_side)
    droplet.add(cube)

    min_x = min(min_x, x_side)
    min_y = min(min_y, y_side)
    min_z = min(min_z, z_side)

    max_x = max(max_x, x_side)
    max_y = max(max_y, y_side)
    max_z = max(max_z, z_side)

    for o_x, o_y, o_z in offsets:
        k = (o_x + x_side, o_y + y_side, o_z + z_side)
        if k not in faces:
            faces[k] = 0
        faces[k] += 1

# To ensure we are not inside a droplet
min_x -= 1
min_y -= 1
min_z -= 1
max_x += 1
max_y += 1
max_z += 1

air = {(min_x, min_y, min_z)}

q = deque([(min_x, min_y, min_z)])
while q:
    x, y, z = q.popleft()
    for o_x, o_y, o_z in offsets:
        n_x, n_y, n_z = k = (x + o_x * 2, y + o_y * 2, z + o_z * 2)

        if min_x > n_x or n_x > max_x or min_y > n_y or max_y < n_y or min_z > n_z or max_z < n_z:
            continue
        if k in droplet or k in air:
            continue

        air.add(k)
        q.append(k)

free = set()

for x, y, z in air:

    for o_x, o_y, o_z in offsets:
        k = (o_x + x, o_y + y, o_z + z)
        if k not in free:
            free.add(k)

total = 0

for key in faces:
    if key in free:
        total +=1

print(total)