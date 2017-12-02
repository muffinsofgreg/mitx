def sumDigits(N):
    '''
    N: a non-negative integer
    '''

    sum = 0
    if N < 10:
        sum += N
    else:
        sum += N % 10
        sum += sumDigits((N - (N % 10)) // 10)

    return sum
