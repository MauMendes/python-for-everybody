fname = "mbox-short.txt"
fh = open(fname)
lst = list()
for line in fh:
    if line.startswith("From "):
        header = line.split()
        lst.append(header[1])

for item in lst:
    print(item)

count = len(lst)
print("There were", count, "lines in the file with From as the first word")