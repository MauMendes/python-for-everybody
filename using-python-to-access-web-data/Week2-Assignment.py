import re

sum = 0
#fhand = open('regex_sum_42.txt')
fhand = open('regex_sum_1206133.txt')

for line in fhand:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)
    if (len(y) > 0 ):
        #print(y)  
        for item in y:
            sum += int(item)

print(sum)