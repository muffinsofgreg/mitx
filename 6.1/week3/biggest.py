animals = { 'a': ['aardvark'], 'b': ['baboob'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: a dictionary, where all of the values are lists.

    reutrns: The key with the largest number of values associated with it
    '''

    dictOfValues = {}
    for key in aDict:
        dictOfValues[key] = len(aDict[key])

    best = max(dictOfValues.values())
    list = []
    for key in dictOfValues:
        if dictOfValues[key] == best:
            list.append((key, best))
        else:
            pass

    return list[0][0]
