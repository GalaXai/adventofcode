import re   
from collections import defaultdict

file = 'adv23/04/in.txt'

#  file = 'adv23/04/test.txt'

with open(file, 'r') as f:
    data = f.read()
    data = data.split('\n')

cards_map = defaultdict(int)

# create the map
for card in data:
    c = 0
    game , codes = card.split(': ')
    winning_codes , available_codes = codes.split(' | ')
    game_number = int(re.findall(r'\d+', game)[0])
    winning_codes = re.findall(r'\d+', winning_codes)
    available_codes = re.findall(r'\d+', available_codes)

    for number in available_codes:
        if number in winning_codes:
            c +=1
    cards_map[game_number] = c

queue = list(range(1,len(data)+1))
c = 0 
created = []
def create_geme(value):
    if value == 0 or cards_map[value] == 0:
        return
    for num in range(value+1, cards_map[value]+1 + value):
        created.append(num)
        create_geme(num)
while queue:
    current = queue.pop(0)
    c+=1
    for num in range(current+1, cards_map[current]+1 + current):
        created.append(num)
        create_geme(num)

    # queue.sort()

print(c+len(created))