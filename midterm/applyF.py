def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """

    newL = []
    newnewL = []

    if len(L) == 0:
        return -1

    for i in L:
        newL.append(f(i))

    for i in newL:
        if g(i) is True:
            newnewL.append(i)

    L = newnewL

    return max(L)
    return L


L = [1, 2, 0, 3, 4, 99, 25, 12, 16, 76, 99, 100]


def f(i):
    return i + 2


def g(i):
    return i > 5


print(applyF_filterG(L, f, g))
print(L)
