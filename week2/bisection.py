print("Please think of a number between 1 and 100: ")
low = 0
high = 100
ans = (high + low)//2
guess = False

while not guess:
    print('Is your secret number', ans, '?')
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.", end="")
    feedback = input(' ')
    if feedback == 'l':
        low = ans
        ans = (high + low)//2

    elif feedback == 'h':
        high = ans
        ans = (high + low)//2

    elif feedback == 'c':
        print('Game over. Your secret number was: ', ans)
        guess = True

    else:
        print('Sorry, i didn\'t understand your guess')
