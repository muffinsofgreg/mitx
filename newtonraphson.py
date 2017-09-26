epsilon = .01
y = 100
guess = y/2.0
numguess = 0

while abs(guess*guess - y) >= epsilon:
        numguess += 1
        guess = guess - (((guess**2) - y) / (2*guess))

print('NumGuess = ' + str(numguess))
print('Square root of ' + str(y) + ' is about ' + str(guess))
