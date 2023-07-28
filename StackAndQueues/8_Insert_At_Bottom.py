def solve(stack,x):
    # Base Condition
    if len(stack) == 0:
        stack.append(x)
        return
    # Store Top
    num = stack.pop()
    # Recursive Call
    solve(stack,x)
    
    stack.append(num)

def nonRecursive(stack,x):
    temp = []
    while len(stack)!=0:
        temp.append(stack.pop())
        
    stack.append(x)
    
    while len(temp) != 0:
        stack.append(temp.pop())
        
    return stack 

def InsertAtBottom(stack,x):
    
    solve(stack,x)
    nonRecursive(stack,x)
    return stack

print(InsertAtBottom([1,2,3,4],10))