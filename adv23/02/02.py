
file = 'adv23/02/in.txt'

#file = 'adv23/02/test.txt'

with open(file, 'r') as f:
    data = f.read()
    data = data.split('\n')


max_values = {
    'red': 12,
    'green': 13,
    'blue': 14
}


count = 0

for line in data:
    game , line = line.split(':')
    sets = line.split(';')
    for set in sets:
        flag = False 
        cur_values = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for cube in set.split(','):
            _ ,val , color = cube.split(' ')
            cur_values[color] += int(val)
        
        test = [val > max_values[key] for key,val  in  cur_values.items()]
        if max(test):
            flag = True
            break
    
    if not flag:
        print(game)
        count += int(game.split(' ')[-1])
print(count)