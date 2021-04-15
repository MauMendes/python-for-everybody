fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    newline = line.strip()
    print(newline.upper())