fhand = open('mbox-short.txt')

time_dict = dict()

for line in fhand:
    if line.startswith("From"):
        data = line.split()
        if(len(data)>3):
            #print(data[5])
            time = data[5].split(':')
            time_dict[time[0]] = time_dict.get(time[0], 0) + 1

#print(time_dict)
#print(sorted(time_dict))
#print (sorted([(k,v) for k,v in time_dict.items()]))

lst = list()
for k,v in time_dict.items():
    lst.append((k,v))
#print(lst)
lst.sort()
#print(lst)
for key, val in lst:
    print(key,val)