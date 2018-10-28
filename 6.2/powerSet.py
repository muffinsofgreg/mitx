# generate all combinations of N items


def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


items = ['apple', 'musk', 'rats', 'cordoroy', 'four', 'money']

powerSet(items)
