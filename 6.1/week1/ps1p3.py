#Assume s is s string of lowercase characters
s = 'abcdeflaiydgakjsndfrstuvwxy'


#longLetter = ''
#
#for i in range(len(s)):
#    for x in range(i, len(s)):
#        if s[i] < s[x]:
#            longLetter += s[i]
#            i = x
#            x += 1
#
#
#
#
#print("Longest substring in alphabetical order is: ", longLetter)

groups = []
lastChar = ''
longest = ''

for char in s:
    if lastChar and c < lastChar:
        groups.append(longest)
        longest = char
    else:
        longest += char
    lastChar = char
print(max(groups, key=len))
