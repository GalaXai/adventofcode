import re   
file = 'adv23/06/in.txt'
#file = 'adv23/06/test.txt'

f = open(file, 'r')
time = list(map(int,re.findall(r'\d+',f.readline())))
distance = list(map(int,re.findall(r'\d+',f.readline())))

t = []
for i in range(len(time)):
    winning_time = []
    for j in range(time[i]):
        # 0 -> 7
        current_speed = j
        time_left = time[i] - j 
        if current_speed * time_left > distance[i]:
            winning_time.append(j)
    t.append(len(winning_time))

sum = 1
for v in t:
    sum *=v
print(sum)
