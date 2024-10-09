def matchingBrackets(string):
    starters = "[{("
    finishers = "]})"
    matches = {"]": "[", ")": "(", "}": "{"}
    stack = []
    for char in string:
        if char in starters:
            stack.append(char)
        elif char in finishers:
            if len(stack) == 0:
                return False
            elif stack[-1] == matches[char]:
                stack.pop()
        else:
            print("invalid char: "+char)
            return False
    return True


string = "([{}]{}())"


test = matchingBrackets(string)
