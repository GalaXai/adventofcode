import re   
file = 'adv23/06/in.txt'
#file = 'adv23/06/test.txt'

f = open(file, 'r')
time = int(''.join(re.findall(r'\d+',f.readline())))
distance = int(''.join(re.findall(r'\d+',f.readline())))
t = []

winning_time = []
for j in range(time):
    # 0 -> 7
    current_speed = j
    time_left = time - j 
    if current_speed * time_left > distance:
        winning_time.append(j)
t.append(len(winning_time))

sum = 1
for v in t:
    sum *=v
print(sum)
