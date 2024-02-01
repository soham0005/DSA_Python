# leetcode 1963

'''
Approach:-
Set a maxCount;
everytime increment count by 1when closed bracket and decrement 1 when open bracket
return max count + 1 // 2
'''

def minSwaps(s):
    maxCount = count = 0
    for i in s:
        if  i == ']':
            count += 1
        else:
            count -= 1
        maxCount = max(count,maxCount)
    return (maxCount + 1) // 2 