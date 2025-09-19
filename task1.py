def closedBrackets(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in pairs.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

print(closedBrackets("()"))        # True
print(closedBrackets("()[]{}"))    # True
print(closedBrackets("(]"))        # False
print(closedBrackets("([])"))      # True
print(closedBrackets("([)]"))      # False