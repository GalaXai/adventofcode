import re   
file = 'adv23/05/in.txt'

#file = 'adv23/05/test.txt'

with open(file, 'r') as f:
    target_seeds = list(map(int,re.findall(r'\d+',f.readline().strip('\n'))))

    data = f.read()
    data = data.split('\n')


    
seeds = {seed: 0 for seed in target_seeds}    
[]
status = 0
for line in data[2:]:
    if line == '':
        continue
    if line[0].isalpha():
        status += 1
        #seeds = {value: 0 for key,value in seeds.items() if value == 0 value = key}
        seeds = {key if value == 0 else value for key, value in seeds.items()}
        n_seeds = {}
        for key in seeds:
            n_seeds[key] = 0
        seeds = n_seeds    
        continue
    

    numbers = list(map(int,re.findall(r'\d+',line)))
    source = range(numbers[1],numbers[1] + numbers[2])
    target = range(numbers[0],numbers[0] + numbers[2])
            
    for tar in seeds.keys():
        if tar in source:
            seeds[tar] = target[source.index(tar)]


# final reverse
seeds = {key if value == 0 else value for key, value in seeds.items()}
n_seeds = {}
for key in seeds:
    n_seeds[key] = 0
seeds = n_seeds    

print(min(list(seeds.keys())))
    

    