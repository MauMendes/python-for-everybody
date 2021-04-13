text = "X-DSPAM-Confidence:    0.8475"
colonPos = text.find(':')
sNumber = text[colonPos+1:]

#option strip, since float is capable to deal with spaces 
sNumber.strip() 

fNumber = float(sNumber)
print(fNumber)