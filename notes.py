#def hello( x ):
#    print('Hello World' + x )

#hello(' Mais Argumento')

#def myreturn(x):
#    return x + 1
#print(myreturn(1))
#import this
#x=2
#if x==1:
#   print('test')
#elif x==2:
#    print(str(2))

#n = 5
#while n>=0:
#    print(n)

#while True:
#    strIn = raw_input(">")
#    print(strIn)
#   if strIn == 'done':
#        break
#print('Done')

#friends = ['Caio', 'Dani', 'Gustavo']
#for friend in friends:
#    print(friend)


#for i in [1,2,3,4,5]:
#    print(i)

#for i in range(3):
#    print(i)

    
#for i in range(2,6):
#    print(i)
    
#print('done') 

#def mymax(numbers):
#    max = numbers[0]
#    for number in numbers:
#        if number>max:
#            max = number
#    print(max)
#mymax([1,22,42,45,78,0])

#counter = 0
#total = 0
#for thing in [10, 10, 10, 10, 10]:
#    counter += 1
#    total += thing
#    avg = float(total)/float(counter)

#print(str(counter) + " elements" + " Total: " + str(total) + " AVg: " + str(avg) )
#found = False

#smallest = None
#numbers = [5,6,7,8,9,33,3]
#for number in numbers:
#    if smallest is None:
#        smallest = number
#    if number < smallest:
#        smallest = number
#print(smallest)

#largest = None
#smallest = None
#while True:
#    num = raw_input('Enter a number: ')
#    if num == "done" : 
#        break

#   try:
#        ival = int(num)
#    except:
#        print("Invalid input")

#    if largest is None:
#    	largest = ival
#    elif largest < ival:
#       largest = ival

#    if smallest is None:
#    	smallest = ival
#    elif smallest > ival:
#        smallest = ival

#print ('Maximum is ' +  str(largest))
#print ('Minimum is '+ str(smallest))

#hello = "Hello World"
#print(hello[:5])
#print(hello[1:5])
#print(hello[6:])

#if 'llo' in hello:
#    print('True'.lower())

#pos = hello.find('z')
#print(pos)
#nstr = hello.replace('l', 'x')
#print(nstr)

#x = 'From marquard@uct.ac.za'
#print(x[14:17])

#dir(x)

#data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#pos = data.find('.')
#rint(data[pos:pos+3])



#print ('Hello World!')
# Use words.txt as the file name
#fname = raw_input("Enter file name: ")
#fh = open(fname)
#for line in fh:
#    newline = line.strip()
#    print(newline.upper())
# Use the file name mbox-short.txt as the file name

#acc = 0.0
#items = 0
#fname = raw_input("Enter file name: ")
#fh = open(fname)
#for line in fh:
#    if not line.startswith("X-DSPAM-Confidence:") : 
#        continue
#    else :
#        pos = line.find(':')
#        snumber = line[pos+1:].strip()
#        acc += float(snumber)
#        items += 1
#    print(snumber)
#avg = acc/items
#print('Average spam confidence: ' + str(avg))

#list = [ 'joe', 1, 2, 3]
#print(len(list[0]))

#friends = ['Lucia', 'Caio', 'Dani']
#for friend in friends:
#    print(friend)

#for i in range(len(friends)):
#    print(friends[i])

#fname = "romeo.txt" #input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
#    print(line.rstrip())
#    words = line.split()
#    for word in words:
#        if word not in lst:
#        	lst.append(word)

#lst.sort()
#print(lst)

#fname = "mbox-short.txt"
#fh = open(fname)
#lst = list()
#for line in fh:
#    if line.startswith("From "):
#        header = line.split()
#        lst.append(header[1])

#for item in lst:
#    print(item)

#count = len(lst)
#print("There were", count, "lines in the file with From as the first word")

#purse  = dict()
#purse["money"] = 12
#purse["candy"] = 3
#purse["tissues"] = 75
#print(purse)

#student = dict()
#student['Name'] = 'Mauricio'
#student['Age'] = 34
#lst = list()
#lst.append(student)
#student2 = dict()
#student2['Name'] = 'Lucia'
#student2['Age'] = 33
#lst.append(student2)
#print(lst)

#Name = 'Mauricio'
#student[Name]= student.get(Name, 0 ) + 1
#print(student)
#Name = 'Lucia'
#student[Name]= student.get(Name, 0 ) + 1
#print(student)

#counts = dict()
#print('enter a line of text:')
#line = raw_input('')
#line = "Hello Hello Mauricio Mendes Hello Mauricio"

#words = line.split()
#print('Words:', words)

#print('Counting....')
#for word in words:
#    counts[word] = counts.get(word,0)+1

#print('Counts:', counts)

#for key in counts:
#    print(key, counts[key])

#print(counts.keys())
#print(counts.values())
#print(counts.items())

#for key,value in counts.items():
#   print(key, value)

#fname = "mbox-short.txt"
#fh = open(fname)
#emails = dict()
#for line in fh:
#    if line.startswith("From "):
#        header = line.split()
#        emails[header[1]] = emails.get(header[1], 0) + 1
#print(emails)

#email_address = None
#email_counter = None

#for key,value in emails.items():
#    if email_counter is None or email_counter<value:
#        email_counter = value
#        email_address = key

#print(email_address, email_counter)


#max_num=max(emails)
#for i,j in emails.items():
#    if j==max_num:
#        print(i,str(int(j/2)))

#### TUPLES

#x = ('Mauricio', 'Lucia', 'Gordo')
#print(x)

#print(x[0])
#x[0] = 'Lucia' #tuple are not mutable 

#y = (1, 9, 3)
#print(y)

#(x, y) = ('Mauricio', 'Lucia')
#print(x,y)

#print((0, 1, 2)>(0,4,5))

#d = { 'a':10, 'b':1 , 'c':22}
#t = sorted(d.items())
#print(t)

# sorted by key
#for k,v in sorted(d.items()):
#    print(k,v)

#sorted use the first element to sort, so if we create a list with the (v,k) tuples, where value is in the first element
#d = { 'a':10, 'b':1 , 'c':22}
#tmp = list()
#for k,v in d.items():
#    tmp.append((v,k))
#print(tmp)
#print(sorted(tmp))

#### THE TOP 10 MOST COMMON WORDS 
#fhand = open('romeo.txt')
#counts = dict()

#for line in fhand:
#    words = line.split()
#    for word in words:
#        counts[word] = counts.get(word, 0) + 1

#print(counts)

#lst = list()
#for (key,val) in counts.items():
#    lst.append((val,key))
##print(sorted(lst, reverse=True))
#for val, key in lst[:10]:
#    print(key,val)


#print (sorted([(v,k) for k,v in counts.items()], reverse=True))

#x = (5, 1, 3)
#print( (0, 1000, 2000)  > x )
#print( (6, 0, 0)   > x )
#print( (4, 100, 200) > x )
#print( (5, 0, 300) > x )
#days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
#print(days[2])



#dir(list())
#dir(tuple())


#fhand = open('mbox-short.txt')

#time_dict = dict()

#for line in fhand:
#    if line.startswith("From"):
#        data = line.split()
#        if(len(data)>3):
#            #print(data[5])
#            time = data[5].split(':')
#            time_dict[time[0]] = time_dict.get(time[0], 0) + 1

#print(time_dict)
#print(sorted(time_dict))
#print (sorted([(k,v) for k,v in time_dict.items()]))

#lst = list()
#for k,v in time_dict.items():
#    lst.append((k,v))
#print(lst)
#lst.sort()
#print(lst)
#for key, val in lst:
#     print(key,val)

#x = 281474976710655
#y = 312390042100017


#if ( y > x ):
#    print( 'y is bigger')
#else:
#    print('x is bigger')

#Python Regular Expression Quick Guide

#^        Matches the beginning of a line
#$        Matches the end of the line
#.        Matches any character
#\s       Matches whitespace
#\S       Matches any non-whitespace character
#*        Repeats a character zero or more times
#*?       Repeats a character zero or more times 
#         (non-greedy)
#+        Repeats a character one or more times
#+?       Repeats a character one or more times 
#         (non-greedy)
#[aeiou]  Matches a single character in the listed set
#[^XYZ]   Matches a single character not in the listed set
#[a-z0-9] The set of characters can include a range
#(        Indicates where string extraction is to start
#)        Indicates where string extraction is to end

#import re

#fhand = open('mbox-short.txt')
#for line in fhand:
#    line = line.rstrip()
#    #if re.search('^From', line):
#    #if re.search('^X.*:', line):
#    if re.search('^X-\S+:', line):
#        print(line)

#x = 'X-Plane is behind schedule: two weeks'
#x = 'X-DSPAM-Result: Innocent'

#if (re.search('^X-\S+:', x)):
#    print('True')
#else: 
#    print('False')

#x = 'My 2 favorite numbers are 19 and 42'
#y = re.findall('[0-9]', x)
#print(y)

#x = 'From: Using the : character'
#y = re.findall('^F.+?:', x) #greed as large as possible (* and +), ? not be greedy
#print(y)

#x = 'From: mauricio.eletrica@gmail.com Sat Jan 5 09:14:00'
#y = re.findall('\S+@\S+', x)
#print(y)

#x = 'From: mauricio.eletrica@gmail.com Sat Jan 5 09:14:00'
#y = re.findall('^From: (\S+@\S+)', x)
#print(y)

#x = 'From: mauricio.eletrica@gmail.com Sat Jan 5 09:14:00'
#y = re.findall('@([^ ]*)', x)
#print(y)

#x = 'From: mauricio.eletrica@gmail.com Sat Jan 5 09:14:00'
#y = re.findall('\S+?@\S+', x)
#print(y)


#import re

#sum = 0
##fhand = open('regex_sum_42.txt')
#fhand = open('regex_sum_1206133.txt')
#
#for line in fhand:
#    line = line.rstrip()
#    y = re.findall('[0-9]+', line)
#    if (len(y) > 0 ):
#        print(y)  
#        for item in y:
#            sum += int(item)

#print(sum)

#import socket
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#mysock.send(cmd)

#while True:
#    data = mysock.recv(512)
#    if len(data) < 1:
#        break
#    print(data.decode())
#mysock.close()