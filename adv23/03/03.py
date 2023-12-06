import copy

file = 'adv23/03/in.txt'

file = 'adv23/03/test.txt'

with open(file, 'r') as f:
    data = f.read()
    data = data.split('\n')




symbols  = ['@','#','$','%','&','*','-','+','=','{','}','[',']','|','\\',';',':',',','<','>','/','?','~','`']
# map this
from collections import defaultdict
numbers_map = defaultdict(list)
symbols_map = defaultdict(list)

for i,line in enumerate(data):
    for j, char in enumerate(line):
        if char.isdigit():
            numbers_map[i].append(j)
        elif char in symbols:
            symbols_map[i].append(j)
        else:pass

numbers_map_copy = copy.deepcopy(numbers_map)
numbers_mapped = defaultdict(list)


for key,value in numbers_map.items():
    for val in value:
        number = data[key][val]
        index = [val]
        while val+1 in value:
            number += str(data[key][val+1])
            index.append(val+1)
            value.pop(value.index(val+1))
            val+=1
        numbers_mapped[key].append((number,index))

#print(numbers_mapped)
sum = 0
# check if simbol in the same line
for key,value in numbers_mapped.items():
        for number, indexes in value:
            # Checks same line
            flag = False
            min_index = max(min(indexes) -1,0) # max to ensure it is not negative
            max_index = min(max(indexes) +1,140) # to ensure we are in bounds
            if min_index in symbols_map[key] or max_index in symbols_map[key]:
                sum += int(number)
                flag = True

            # Checks above line
            if key!= 0 and not flag:
                for index in range(min_index,max_index+1):
                    if index in symbols_map[key-1]:
                        sum += int(number)
                        flag = True
                        break
            # checks below line
            if key!= 140 and not flag:
                for index in range(min_index,max_index+1):
                    if index in symbols_map[key+1]:
                        sum += int(number)
                        break

print(sum)


### PART 2 of day 3
numbers_map = numbers_map_copy.copy()

true_count = 0
for key,values in symbols_map.items():
    for val in values:
        gear_count = 0
        gear_numbers = []
        
        # check adjacent numbers
        if val-1 in numbers_map[key]:
            gear_count +=1
            gear_numbers.append(data[key][val-1])
        if val+1 in numbers_map[key]:
            gear_count +=1
            gear_numbers.append(data[key][val+1])
        
        # check above line
        if key!= 0:
            if val in numbers_map[key-1]:
                gear_count +=1
                gear_numbers.append(data[key-1][val])
            if val-1 in numbers_map[key-1]:
                gear_count +=1
                gear_numbers.append(data[key-1][val-1])
            if val+1 in numbers_map[key-1]:
                gear_count +=1
                gear_numbers.append(data[key-1][val+1])
        if key!= 140:
            if val in numbers_map[key+1]:
                gear_count +=1
                gear_numbers.append(data[key+1][val])
            if val-1 in numbers_map[key+1]:
                gear_count +=1
                gear_numbers.append(data[key+1][val-1])
            if val+1 in numbers_map[key+1]:
                gear_count +=1
                gear_numbers.append(data[key+1][val+1])
        if gear_count >= 2:
            print(gear_numbers)
            true_count += int(gear_numbers[0])*int(gear_numbers[-1])

print(true_count)


        
        



