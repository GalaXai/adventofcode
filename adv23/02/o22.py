
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
    cur_values = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for set in sets:
        flag = False 
        for cube in set.split(','):
            _ ,val , color = cube.split(' ')
            cur_values[color] = max(int(val),cur_values[color])
        
    
    
    # get max values and * them up
    sesion_count = 1
    for key,val in cur_values.items():
        sesion_count *= val
    count += sesion_count 
print(count)