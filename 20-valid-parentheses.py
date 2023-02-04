def isValid(s):

    stack = []
    closeToOpen = {}

    closeToOpen[")"] = "("
    closeToOpen["}"] = "{"
    closeToOpen["]"] = "["

    for paremtheses in s:
        # if the parentheses is a closing bracket
        if paremtheses in closeToOpen:
            # if the stack is not empty
            if stack and stack[-1] == closeToOpen[paremtheses]:
                stack.pop()
            else:
                return False
        else:
            stack.append(paremtheses)

    # check if the stack is empty
    if not stack:
        return True
    else:
        return False
