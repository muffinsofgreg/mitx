def lessThan4(aList):
    '''
    aList: a list of strings
    '''

    newList = []
    for each in aList:
        if len(each) < 4:
            newList.append(each)

    return newList
