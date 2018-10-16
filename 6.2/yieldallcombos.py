def powerset(items):
    """
    PowerSet is all possible combinations of N;
    (O)**n"""

    N = len(items)

    # enumerate the n**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def yieldall(items):
    N = len(items)

    for i in range(3**N):
        bag1 = []
        bag2 = []

        for j in range(N):
            if (i // 3**j) % 3 == 1:
                bag1.append(items[j])
            if (i // 3**j) % 3 == 2:
                bag2.append(items[j])

        yield (bag1, bag2)


if __name__ == "__main__":

    items = ['apple', 'bacon', 'tulip', 'box', 'jumbo', 'micro',
             'chair', 'hat']

#    test = powerset(items)
#
#    for item in test:
#        print(item)

    test = yieldall(items)

    for item in test:
        print(item)
