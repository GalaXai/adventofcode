import re   
file = 'adv23/04/in.txt'

#  file = 'adv23/04/test.txt'

with open(file, 'r') as f:
    data = f.read()
    data = data.split('\n')

count = 0
for card in data:
    c = 0
    card , numbers = card.split('|')
    winning_numbers = re.findall(r'\d+', card)[1:]
    available_numbers = re.findall(r'\d+', numbers)
    
    for number in available_numbers:
        if number in winning_numbers:
            c += 1
    print(2**c)
    if c == 0:
        continue
    else:count += 2**(c-1)
print(count)