import re
file = 'adv23/01/in.txt'
#file = 'adv23/01/test.txt'
with open(file, 'r') as f:
    data = f.read()
    data = data.split('\n')

count = 0

numbers = 'zero one two three four five six seven eight nine'.split(' ')

p = "(?=(" + "|".join(numbers) + "|\\d))"

def decode(x):
    if x in numbers:
        return str(numbers.index(x))
    else:
        return x


for line in data:
    vals = re.findall(p, line)
    values  = [*map(decode, vals)]
    if len(values) == 0:
        continue
    else:
        count += int(values[0] + values[-1])

print(count)