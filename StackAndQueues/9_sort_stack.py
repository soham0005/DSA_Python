def sortStack(stack):
    #Brute Force
    # temp = []
    # while len(stack)!=0:
    #     temp.append(stack.pop())
        
    # temp.sort(reverse=True)
    # while len(temp) != 0:
    #     stack.append(temp.pop())
    # print(temp,stack)
    
    #optimized
    ''''
    Use Another Stack and compare both's top and insert
    '''
    temp = []
    while stack:
        ele = stack.pop()
        while temp and temp[-1] > ele:
            stack.append(temp.pop())
        temp.append(ele)
    print(temp)
    
sortStack([11,2,32,3,41])
    
    