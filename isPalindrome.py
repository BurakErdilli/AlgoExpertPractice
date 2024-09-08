def isPalindrome(string, i=0):

    if i >= len(string)-i-1:
        return True

    if string[i] == string[len(string)-i-1]:
        return isPalindrome(string, i+1)

    return False


string = "/: traşnedenşart :/"

a = isPalindrome(string)
