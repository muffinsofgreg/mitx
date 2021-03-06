def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base, b
    '''

    ansList = []
    for ans in range(x):
        if b ** ans <= x:
            ansList.append(ans)
    return max(ansList)
