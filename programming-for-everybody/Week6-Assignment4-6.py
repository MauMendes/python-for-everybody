<<<<<<< HEAD
def computepay(h,r):
    if h<=40:
        pay = h*r
    else:
        pay = 40*r + (h-40)*r*1.5
    return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate Per Hour:")
r = float(rate)

p = computepay(h,r)
=======
def computepay(h,r):
    if h<=40:
        pay = h*r
    else:
        pay = 40*r + (h-40)*r*1.5
    return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate Per Hour:")
r = float(rate)

p = computepay(h,r)
>>>>>>> 23016d10d2185085345ada24602b1839dcc2efb5
print("Pay",p)