x = int(input("I'll output the cube of a number between 1 and 100: "))
epsilon = .01
low = 1.0
high = 100
ans = (high + low)/2
guess = 0

while abs(ans**2 - x) > epsilon:
    print('low: ', low, 'high: ', high, 'guess: ', guess)
    guess += 1
    if ans**2 < x:
        low = ans

    else:
        high = ans

    ans = (high + low)/2

print(ans)
