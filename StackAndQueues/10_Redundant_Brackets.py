def redundant_bracket(s):
    stack = []
    for ele in s:
        if ele in "+-*/(":
            stack.append(ele)
        elif ele == ')':
            flag = True
            while stack[-1] != '(':
                if stack[-1] in "+-*/":
                    flag = False
                stack.pop()
            stack.pop()
            
            if flag:
                return 1
    return 0

print(redundant_bracket("(a+()b)"))