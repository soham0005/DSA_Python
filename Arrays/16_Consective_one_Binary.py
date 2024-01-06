# Longest Consective One - GFG

def maxConsectiveOnes(N):
    N = bin(N)[2:]
    count = 0 
    maxCount = 0
    for ele in N:
        if ele == '1':
            count+=1
            maxCount = max(count,maxCount)
        else:
            count = 0
    print(maxCount)
    
maxConsectiveOnes(222)
    