def deleteMiddleOfStack(inputStack,N):
    stack = []
    mid = int(N/2)
    
    for i in range(mid+1):
        stack.append(inputStack.pop())
    
    stack = stack[::-1]
    
    for i in range(1,len(stack)):
        inputStack.append(stack[i])
        
    return inputStack

print(deleteMiddleOfStack([1,2,4,5],5))