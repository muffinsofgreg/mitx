#Assume s is s string of lowercase characters
s = 'iykjhasdfnasdopunasdbaiwuabdcourys'

longest = []

for i in range(len(s)):
    for x in range(len(s)):
        if s[i] < s[x]:
            longest.append(s[i])
            break
        else:
            break

print(longest)

