def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    Revursive bisection search
    '''
    mid = len(aStr) // 2
    end = len(aStr) + 1
    aStr = sorted(aStr)
    
    if (len(aStr) == 1 and char != aStr[0]) or len(aStr) == 0:
        return False
    
    if char == aStr[mid]: 
        return True
    
    if char < aStr[mid]: 
        return isIn(char, aStr[:mid])
        
    elif char > aStr[mid]:
        return isIn(char, aStr[mid:end])
    
#Some sample test cases - it works

s6 = 'bbdghjllmmmqvx'

print(isIn('d', s6))
