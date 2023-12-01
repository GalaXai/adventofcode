### PART 1

import re   
with open('adv23/01/in.txt', 'r') as f:
    data = f.read()
    data = data.split('\n')

count = 0
for line in data:
    vals = re.findall(r'\d', line)
    print(vals)
    if len(vals) == 0:
        continue
    else:
        count += int(vals[0]+vals[-1])
print(count)
#54968