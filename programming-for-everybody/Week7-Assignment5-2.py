<<<<<<< HEAD
largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == "done" : 
        break

    try:
        ival = int(num)
    except:
        print("Invalid input")

    if largest is None:
    	largest = ival
    elif largest < ival:
        largest = ival

    if smallest is None:
    	smallest = ival
    elif smallest > ival:
        smallest = ival

print('Maximum is', largest)
=======
largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == "done" : 
        break

    try:
        ival = int(num)
    except:
        print("Invalid input")

    if largest is None:
    	largest = ival
    elif largest < ival:
        largest = ival

    if smallest is None:
    	smallest = ival
    elif smallest > ival:
        smallest = ival

print('Maximum is', largest)
>>>>>>> 23016d10d2185085345ada24602b1839dcc2efb5
print('Minimum is', smallest)