def validParanthesis(s):
    stack = []
    data = {"(":")","{":"}","[":"]"}
    
    for char in s:
        if char in data:
            stack.append(char)
        elif len(stack) == 0 or data[stack.pop()] != char:
            return False
    return len(stack) == 0
    
    # for char in s:
    #     if char == '(' or char == '{' or char == '[':
    #         stack.append(char)
    #     elif char == ')' and stack and stack[-1] == '(':
    #         stack.pop()
    #     elif char == '}' and stack and stack[-1] == '{':
    #         stack.pop()
    #     elif char == ']' and stack and stack[-1] == '[':
    #         stack.pop()
    # print(len(stack) == 0)
    
print(validParanthesis("]"))