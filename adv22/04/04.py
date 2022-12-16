import re
import numpy as np
'''
2-8
3-7
--
6-6
4-6
'''
def one(data):
    numbers = re.findall('\d+',data)
    numbers = [int(x) for x in numbers]
    if (numbers[0] <= numbers[2] and numbers[1] >= numbers[3]) or (numbers[0] >= numbers[2] and numbers[1] <= numbers[3] and numbers[1]>= numbers[2]):
        return 1
    return 0

def two(data):
    numbers = re.findall('\d+', data)
    numbers = [int(x) for x in numbers]
    list_1 = np.arange(numbers[0],numbers[1]+1,1)
    list_2 = np.arange(numbers[2],numbers[3]+1,1)
    for num in list_1:
        if num in list_2:
            return 1
    return 0

if __name__ == '__main__':
    with open('in.txt') as f:
        data = f.read().splitlines()
    score =0
    for record in data:
        score += two(record)

    print(score)