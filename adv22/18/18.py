cubes = [eval(x) for x in open('in.txt').read().splitlines()]

# cord are cubes in 3 plane

# given cube_1 (,1,1)
# offset cube_1 (1.5,1,1)
# given cube_2 (2,1,1)
# offset cube_2 (1.5,1,1)
#               ------- we see they have common face
offsets = [(0.5, 0, 0), (0, 0.5, 0), (0, 0, 0.5), (-0.5, 0, 0), (0, -0.5, 0), (0, 0, -0.5)]

faces = {}

for x_side, y_side, z_side in cubes:
    cube = (x_side, y_side, z_side)

    for o_x, o_y, o_z in offsets:
        k = (o_x + x_side, o_y + y_side, o_z + z_side)
        if k not in faces:
            faces[k] = 0
        faces[k] += 1

print(list(faces.values()).count(1))
