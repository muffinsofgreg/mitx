s = "asdbasdoasdfbasdfbobgbobobgbobbob"      #assume any string of lower case character

bobString = ('bob')

n=0
for i in range(len(s)):
    if s[i:i+3] == bobString:
        n+=1

print('Number of times bob occurs is: ', n)
