<<<<<<< HEAD
text = "X-DSPAM-Confidence:    0.8475"
colonPos = text.find(':')
sNumber = text[colonPos+1:]

#option strip, since float is capable to deal with spaces 
sNumber.strip() 

fNumber = float(sNumber)
=======
text = "X-DSPAM-Confidence:    0.8475"
colonPos = text.find(':')
sNumber = text[colonPos+1:]

#option strip, since float is capable to deal with spaces 
sNumber.strip() 

fNumber = float(sNumber)
>>>>>>> 21776b9fadd437428c9fbf1b550d7669b8d9631d
print(fNumber)