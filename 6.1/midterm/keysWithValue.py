def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    newList = []
    for key in aDict:
        if aDict[key] == target:
            newList.append(key)

    return sorted(newList)
