s = "kjsdfouoaoiasdklldf"  #assume any string of lower case character

##Counts the number of vowels in string s

vowels = ('a', 'e', 'i', 'o', 'u')

vowelCollector = []

for letter in s:
    if letter in vowels:
        vowelCollector.append(letter)

print('Number of vowels: ', len(vowelCollector))
