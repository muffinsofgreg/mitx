s = input('Enter palindrome test string: ')

def ispal(s):
    """
    for string s, return True if palindrome, else false
    """

    if len(s) <= 1:
        return True

    return s[0] == s[-1] and ispal(s[1:-1])

print(ispal(s))
