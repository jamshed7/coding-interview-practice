#Checks is a string of parentheses is balanced
def balance_check(s):

    if len(s)%2 != 0:
        return False

    opening = ['{', '[', '(']
    stack = []

    for bracket in s:
        if bracket in opening:
            stack.append(bracket)
        else:
            if bracket == '}' and stack[-1] == '{':
                stack.pop()
            elif bracket == ']' and stack[-1] == '[':
                stack.pop()
            elif bracket == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return len(stack) == 0
