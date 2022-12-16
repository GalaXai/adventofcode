alph = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

def one(rucksacks):
    part1 = rucksacks[:len(rucksacks)//2]
    part2 = rucksacks[len(rucksacks)//2:]
    for letter in part1:
        for letter_2 in part2:
            if letter == letter_2:
                if letter.islower():
                    return ord(letter)-96
                else: return ord(letter)-38

#if __name__ == '__main__':
#    with open('in.txt') as f:
#        data = f.read().splitlines()
#    score = 0
#    for ruck in data:
#        score += one(ruck)
#    print(score)

def two(line1,line2,line3):
    for let in line1:
        if line2[line2.find(let)] == line3[line3.find(let)]:
            if let.islower():
                return ord(let) - 96
            else:
                return ord(let) - 38





if __name__ == '__main__':
    with open('in.txt') as f:
        data = f.read().splitlines()
    i=0
    score = 0
    while i< len(data):
        score += two(data[i],data[i+1],data[i+2])
        i+=3
    print(score)