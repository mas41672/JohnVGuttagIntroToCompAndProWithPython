
numXs = int(input('How many times should I print the letter x?'))
toPrint = '#'
#concatenate x to toPrint numX
ans = 0
itersLeft = numXs
aTempString = ''
while ( itersLeft != 0):
    aTempString =aTempString + toPrint 
    itersLeft = itersLeft - 1
toPrint = aTempString
print(toPrint)