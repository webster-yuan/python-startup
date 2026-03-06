def isValid(s: str) -> bool:
    """
    使用栈来判定
    """
    stack = []
    bracket_map = {'(':')', '[':']', '{':'}'}
    for char in s:
        if char in bracket_map:
            # 左括号入栈
            stack.append(char)
        else:
            # 右括号
            if not stack:
                return False
            
            top = stack.pop()
            if char != bracket_map[top]:
                return False
        
    return not stack

print(isValid("()[]{}"))  # True
print(isValid("(]"))      # False