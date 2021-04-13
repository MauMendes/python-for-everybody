acc = 0.0
items = 0

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    else :
        pos = line.find(':')
        snumber = line[pos+1:].strip()
        acc += float(snumber)
        items += 1

avg = acc/items
print('Average spam confidence:', avg)