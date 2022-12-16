normalizer = {
    'A': 'R',
    'X': 'R',
    'B': 'P',
    'Y': 'P',
    'C': 'S',
    'Z': 'S',
}
points = {
    'R': 1,
    'P': 2,
    'S': 3
}
list = ['R','P','S','R','P','S']

def logic(input):
    # B Z
    enmy = normalizer[input[0]]
    our = normalizer[input[-1]]
    if enmy == our:  # draw
        return points[our] + 3
    else:
        return comp(enmy, our)

def comp(input1, input2):
    if input1 == 'R':
        if input2 == 'S':
            return points[input2] + 0
        else:
            return points[input2] + 6
    elif input1 == 'P':
        if input2 == 'R':
            return points[input2] + 0
        else:
            return points[input2] + 6
    elif input1 == 'S':
        if input2 == 'P':
            return points[input2] + 0
        else:
            return points[input2] + 6


def calc_outcome(enmy,outcome):
    if outcome == 'X': # lose
        return points[list[list.index(enmy)+2]]+0
    else:
        return points[list[list.index(enmy)+1]]+6

def logic2(input):
    enmy = normalizer[input[0]]
    outcome = input[-1]
    if outcome == 'Y':
        return points[enmy] + 3
    else: return calc_outcome(enmy,outcome)

if __name__ == '__main__':
    with open('in.txt') as f:
        data = f.read().splitlines()
    score = 0
    for record in data:
        #score += logic(record) # 021
        score += logic2(record) # 022
    print(score)
